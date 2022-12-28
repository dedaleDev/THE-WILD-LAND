
import math
from multiprocessing.util import info
import random
import pygame
import generation
from imageLoad import ImageLoad
#from PIL import Image
from mob import Mob
from joueur import Player
from sound import Sound

import aideCSV

premierPAss=True
class Game(pygame.sprite.Sprite):
    def __init__(self, infoObject, fenetre, mapChoisie, pointSpawn):
        super().__init__()
        posRectChargement = infoObject[0]*1/4, infoObject[1]*3/4
        self.infoObject=infoObject
        self.diagonalEcran = math.sqrt(infoObject[0]**2 + infoObject[1]**2)
        taillePolice = round(3/100*self.diagonalEcran)
        font = pygame.font.Font("data/menu/font.ttf", taillePolice//2)
        
        self.updateBar(fenetre, 0, posRectChargement, "chargement des images...", font)
        
        self.text=None
        
        self.images = ImageLoad(self.infoObject)
        self.backgroundMonde = self.images.loadImgBackMonde(self.infoObject)
        self.backgroundArene = self.images.loadImgBackArene(self.infoObject)
        self.updateBar(fenetre, 25, posRectChargement, "chargement des sons...", font)
        self.son = Sound()
        self.updateBar(fenetre, 75, posRectChargement, "chargement de la carte...", font)
        
        self.imCollision = self.images.getImCollision()
        self.map = 0
        self.mapWorld = 0
        self.mapBoss=0
        self.mapMontagneMer = 0
        self.imageFog2 = self.openFog2()
        self.imageErreurRessource = self.openImageRessource()
        self.mapImg = 0
        
        self.mapImgO = 0
        self.mapImgO_superpose = 0
        self.mapMer = 0
        self.mapVide = 0
        self.listeCaseMer = 0
        self.listeCaseForet = 0
        self.listeCasePlaine=0
        self.listeCaseMontagne=0
        self.fenetre = fenetre
        self.listeCaseBatiment=[]
        self.nbAnnimaux=0
        
        if not mapChoisie:
            self.taille_matriceY = int(aideCSV.valCorrespondante("taille_matriceY"))
            self.taille_matriceX = int(aideCSV.valCorrespondante("taille_matriceX"))
        else:
            self.taille_matriceY = len(mapChoisie)
            self.taille_matriceX = len(mapChoisie[0])
            
        
        
        self.police=pygame.font.Font("data/menu/Avenir.ttc", 20)
        self.infoMortAnnimal = 0
        self.groupMob = pygame.sprite.Group()
        self.groupProjectile = pygame.sprite.Group()
        self.groupDefense = pygame.sprite.Group()
        self.groupCoffre = pygame.sprite.Group()
        self.groupLoot = pygame.sprite.Group()
        self.groupTuileBoost = pygame.sprite.Group() #liste des tuiles boosté avec un batiment present 
        
        self.genererMatrice(mapChoisie)
        self.updateBar(fenetre, 100, posRectChargement, "preparez vous...", font)
        self.joueur = Player(self,"joueur0", 5, pointSpawn)
        self.groupJoueur=pygame.sprite.Group()
        self.groupJoueur.add(self.joueur)
        self.groupBuild=pygame.sprite.Group()
        self.probaGolemForet = 0
        self.probaOursin = 0
        self.probaKraken = 0
        self.probaMage = 0
        self.probaDragon = 0
        self.probaYeti = 0
        self.incendieDelay=0
        self.troisMin = False
        self.septMin = False
        self.cinqMin=False
        self.huitMin=False
        self.incendie=False
        self.listeDebug = []
        self.tempsMort = 0 #compte les millisecondes de temps passe dans le menu etc
        self.lastPause = 0
        self.stat = False
        self.moveX, self.moveY = 0,0
        self.boss=False
        self.theBoss = 0
        self.queueMob=[]
        self.tempsSansMob={"golem":-2, "mage":-2, "dragon":-1,"yeti":-1, "oursin":-1, "kraken":-1}
        
        
        self.pvKraken =0
        self.pvDragon = 0
        self.pvOursin = 0
        self.pvMage =0
        self.pvGolem =0
        self.pvYeti = 0
        
        self.vitesseKraken =0
        self.vitesseOursin =0
        self.vitesseMage =0
        self.vitesseGolem= 0
        self.vitesseDragon =0
        self.vitesseYeti=0
        
        self.modeFacile=False
        self.modeNormal=False
        self.modeDifficile=False
        self.modeExtreme=False
        self.initDiffitulte()
        
    
    def initDiffitulte(self):
        diff=aideCSV.valCorrespondante("difficulte")
        if diff=="facile":
            self.pvKraken = 60
            self.pvDragon = 300
            self.pvOursin = 75
            self.pvMage = 70
            self.pvGolem = 40
            self.pvYeti = 500
            
            self.vitesseKraken = 1
            self.vitesseOursin = 3 
            self.vitesseMage = 1
            self.vitesseGolem = 2
            self.vitesseDragon = 2
            self.vitesseYeti=2
            
            self.attaqueKraken = 5
            self.attaqueOursin=3
            self.attaqueMage =5
            self.attaqueDragon =15
            self.attaqueYeti=20
            self.attaqueGolem=7
            self.modeFacile=True
        if diff=="normal":
            self.pvKraken = 100
            self.pvDragon = 450
            self.pvOursin = 125
            self.pvMage = 100
            self.pvGolem = 75
            self.pvYeti = 600
            
            self.vitesseKraken = 1
            self.vitesseOursin = 3 
            self.vitesseMage = 2
            self.vitesseGolem = 2
            self.vitesseDragon = 2
            self.vitesseYeti=2
            
            self.attaqueKraken = 7
            self.attaqueOursin=5
            self.attaqueMage =8
            self.attaqueDragon =20
            self.attaqueYeti=25
            self.attaqueGolem=12
            self.modeNormal=True
        if diff=="difficile":
            self.pvKraken = 100
            self.pvDragon = 450
            self.pvOursin = 125
            self.pvMage = 100
            self.pvGolem = 75
            self.pvYeti = 600
            
            self.vitesseKraken = 1
            self.vitesseOursin = 3 
            self.vitesseMage = 2
            self.vitesseGolem = 2
            self.vitesseDragon = 2
            self.vitesseYeti=2
            
            self.attaqueKraken = 7
            self.attaqueOursin=5
            self.attaqueMage =8
            self.attaqueDragon =20
            self.attaqueYeti=25
            self.attaqueGolem=12
            self.modeDifficile=True
        if diff=="extreme":
            self.pvKraken = 100
            self.pvDragon = 500
            self.pvOursin = 150
            self.pvMage = 150
            self.pvGolem = 110
            self.pvYeti = 800
            
            self.vitesseKraken = 2
            self.vitesseOursin = 3 
            self.vitesseMage = 2
            self.vitesseGolem = 2
            self.vitesseDragon = 2
            self.vitesseYeti=2
            
            self.attaqueKraken = 10
            self.attaqueOursin=10
            self.attaqueMage = 15
            self.attaqueDragon = 25
            self.attaqueYeti=35
            self.attaqueGolem=15
            self.modeExtreme=True
    def bonusTempsSansMob(self, nom):
        if self.modeExtreme:
            return abs(self.tempsSansMob[nom]*2)
        return self.tempsSansMob[nom]

    def fonctionGolem(self):
        temps = self.tempsJeuMinute()
        if self.modeExtreme:
            if temps>15:
                re= -temps/2.5+10
                if re <1:
                    return 1
                return re
            return temps/4+1+self.bonusTempsSansMob("golem")
        #if self.modeFacile:
        if temps<2:
            return 0
        if temps>15:
            re= -temps/2.5+10
            if re <1:
                return 1
            return re
        return temps/6+1+self.bonusTempsSansMob("golem")
    

    def fonctionOursin(self):
        temps = self.tempsJeuMinute()
        if self.modeExtreme:
            return temps/8+self.bonusTempsSansMob("oursin")
        #if self.modeFacile:
        if temps<4:
            return 0
        return temps/9+self.bonusTempsSansMob("oursin")


    def fonctionKraken(self): 
        temps = self.tempsJeuMinute()
    
        #if self.modeFacile:
        return temps/9+self.bonusTempsSansMob("kraken")


    def fonctionMage(self):
        temps = self.tempsJeuMinute()
        if self.modeExtreme:
            
            return (temps)/5+self.bonusTempsSansMob("mage")
        if temps<3:
            return 0
        return (temps-3)/6+self.bonusTempsSansMob("mage")


    def fonctionDragon(self):
        temps = self.tempsJeuMinute()
        if self.modeExtreme:
            if temps<4:
                return 0
            re = (temps-5)/3+self.bonusTempsSansMob("dragon")
            if re>6:
                return 6
            return re
        if temps<8:
            return 0
        re = (temps-8)/3+self.bonusTempsSansMob("dragon")
        if re>4:
            return 4
        return re

    def fonctionYeti(self):
        temps = self.tempsJeuMinute()
        if self.modeFacile:
            return 0
        if self.modeExtreme:
            if temps<6:
                return 0
            return (temps-6)/3+self.bonusTempsSansMob("yeti")
        if temps<10:
            return 0
        return (temps-10)/4+self.bonusTempsSansMob("yeti")

    
    def openImageRessource(self):
        im = pygame.image.load("data/menu/alerteRessource.png").convert_alpha()
        im = pygame.transform.scale(im, (592*0.75, 155*0.75))
        return im
    
    def tempsJeu(self):
        return pygame.time.get_ticks()- self.tempsMort
    
    def tempsJeuMinute(self):
        return (pygame.time.get_ticks()- self.tempsMort)/1000/60 
    
    def updateBar(self, fenetre, valeurChargement, posRectChargement, texte, font):
        valeurChargement = valeurChargement/100

        texte = font.render(texte, True, "White")
        pygame.draw.rect(fenetre, (70,70,70), (posRectChargement, (100*self.infoObject[0]*0.005 , 3)))
        pygame.draw.rect(fenetre, (255,255,255), (posRectChargement, (100*self.infoObject[0]*0.005*valeurChargement , 3)))
        
        pygame.draw.rect(fenetre, (0,0,0), ((posRectChargement[0], posRectChargement[1]+10), (1000 , 1000))) #actualisation du texte
        fenetre.blit(texte, (posRectChargement[0], posRectChargement[1]+10))
        pygame.display.flip()
    
    def majCata(self):
        if self.joueur.indiceEcolo>0.50 and len(self.listeCaseBatiment)>0 and self.tempsJeu()-self.incendieDelay > 15:#000 : #INCENDIE
            if not random.randint(0,2) or True: #quand on tombe sur un 0, donc incendie toute les 3 min environ
                indice=random.randint(0, len(self.listeCaseBatiment)-1)
                tuile = self.listeCaseBatiment[indice]
                self.listeCaseBatiment.pop(indice)
                self.incendie=True
                self.incendieDelay=self.tempsJeu()
                return tuile
    
    
    def majMob(self):
        self.probaGolemForet=self.fonctionGolem()
        self.probaDragon=self.fonctionDragon()
        self.probaKraken=self.fonctionKraken()
        self.probaOursin=self.fonctionOursin()
        self.probaYeti=self.fonctionYeti()
        self.probaMage=self.fonctionMage()

    def verifierCo(self, x, y):
        return  x<self.taille_matriceX and x >=0 and y < self.taille_matriceY and y>=0
        
    def genererMatrice(self, mapChoisie):
        if not mapChoisie:
            self.map = generation.generation_matrice(self)
            self.mapWorld=self.map
        else :
            self.map = generation.typeToTuile(mapChoisie, self)
            self.mapWorld=self.map
        self.mapBoss = generation.mapBoss(self)
        self.mapMontagneMer, self.mapMer, self.mapDesert, self.mapVide, self.listeCaseMer, self.listeCaseForet, self.listeCasePlaine, self.listeCaseMontagne  = generation.generation_matriceMontagneMer(self.map, self)

    def spawnAnnimal(self, spawnChameau=10, spawnOiseau=1, spawnLapin = 3, spawnOiseau2 = 2):
        for y in range(self.taille_matriceY):
            for x in range(self.taille_matriceX):
                if self.map[y][x].type==6:
                    rand = random.randint(0,100)
                    if rand<spawnChameau :
                        self.groupMob.add(Mob(self,"chameau", 100, 1, tuile=self.map[y][x], score=0, desertique=True, annimal=True, attaque=0))
                        self.nbAnnimaux+=1
                rand = random.randint(0,200)
                if rand<spawnOiseau :
                    self.groupMob.add(Mob(self,"oiseau", 100, 1, tuile=self.map[y][x], score=0, annimal=True, attaque=0, aerien=True))
                    self.nbAnnimaux+=1
                if self.map[y][x].type==1:
                    rand = random.randint(0,100)
                    if rand<spawnLapin :
                        self.groupMob.add(Mob(self,"lapin", 100, 2, tuile=self.map[y][x], score=0, annimal=True, attaque=0))
                        self.nbAnnimaux+=1
                if self.map[y][x].type==4:
                    rand = random.randint(0,25)
                    if rand<spawnOiseau2 :
                        if random.randint(0,1):
                            self.groupMob.add(Mob(self,"oiseau2", 100, 1, tuile=self.map[y][x], score=0, annimal=True, attaque=0))
                            self.nbAnnimaux+=1
                        else:
                            self.groupMob.add(Mob(self,"renard", 100, 1, tuile=self.map[y][x], score=0, annimal=True, attaque=0))
                            self.nbAnnimaux+=1
        
    def checkCollision(self, joueur, listeMob):
        listeColide=[]
        now = self.tempsJeu()
        for mob in listeMob :
            if mob.attack>0:
                
                colide = pygame.sprite.collide_mask(joueur, mob)
                if colide and now-joueur.lastDamage>joueur.cooldownDamage:
                    joueur.takeDamage(mob.attack)
                    joueur.dictioDegatMob[mob.name]+=mob.attack
                    joueur.lastDamage=now
                    listeColide.append(colide)
                if mob.name=="mage" or mob.name=="yeti": 
                    mob.lunchProjectile()
        return listeColide

    def avoirTuileJoueur(self, joueur):
        return self.map[joueur.posY][joueur.posX]



    def addTuileAutour(self,d ,rayon:int):
        if d=={}:
            for x in range(15):
                if not (x in d):
                    d[x] = []
            for y in range(-rayon, rayon+1):
                for x in range(-rayon,rayon+1):
                    if self.verifierCo(self.joueur.posX+x, self.joueur.posY+y) and (y!=0 or x!=0):
                        tuile=self.map[self.joueur.posY+y][self.joueur.posX+x]

                        d[tuile.type].append(tuile)
            
                    
        
            
        return d
                       



    def spawMob(self):
        """fonction qui gere le spawn des mobs"""
        randGolem = random.randint(1,150)
        randOursin = random.randint(1,150)
        randDragon = random.randint(1,150)
        randKraken = random.randint(1,150)
        randMage = random.randint(1,150)
        randYeti = random.randint(1,150)
        tuileAutourJoueur={}
        
        
        self.tempsSansMob["golem"]+=1/60
        self.tempsSansMob["mage"]+=1/60
        self.tempsSansMob["oursin"]+=1/60
        self.tempsSansMob["yeti"]+=1/60
        self.tempsSansMob["kraken"]+=1/60
        self.tempsSansMob["dragon"]+=1/60
        
        #print("randGolem:",randGolem," proba=",self.fonctionGolem()-self.bonusTempsSansMob("golem"), "et ", self.bonusTempsSansMob("golem")," de bonus")
        if randGolem<self.fonctionGolem():
            tuileAutourJoueur=self.addTuileAutour(tuileAutourJoueur, 5)
            if tuileAutourJoueur[4]!=[]:
                self.groupMob.add(Mob(self, "golem_des_forets", self.pvGolem, self.vitesseGolem, random.choice(tuileAutourJoueur[4]), 100, attaque=self.attaqueGolem))
                pygame.mixer.Sound.play(self.son.golem_des_foretsSpawn)
                self.tempsSansMob["golem"]=-1
            
        if randOursin<self.fonctionOursin():
            tuileAutourJoueur=self.addTuileAutour(tuileAutourJoueur, 5)
            if tuileAutourJoueur[1]!=[]:
                self.groupMob.add(Mob(self, "oursin", self.pvOursin, self.vitesseOursin, random.choice(tuileAutourJoueur[1]), 150, pique=True, attaque=self.attaqueOursin))
                pygame.mixer.Sound.play(self.son.oursinSpawn)
                self.tempsSansMob["oursin"]=-1.5
        if randMage<self.fonctionMage():
            tuileAutourJoueur=self.addTuileAutour(tuileAutourJoueur, 5)
            if tuileAutourJoueur[4]!=[]:
                self.groupMob.add(Mob(self, "mage", self.pvMage, self.vitesseMage, random.choice(tuileAutourJoueur[4]), 125, attaque=self.attaqueMage))
                pygame.mixer.Sound.play(self.son.mageSpawn)
                self.tempsSansMob["mage"]=-1
        if randKraken<self.fonctionKraken():
            tuileAutourJoueur=self.addTuileAutour(tuileAutourJoueur, 5)
            if tuileAutourJoueur[3]!=[]:
                self.groupMob.add(Mob(self, "kraken", self.pvKraken, self.vitesseKraken,random.choice(tuileAutourJoueur[3]), 100, aquatique=True, attaque=self.attaqueKraken))
                pygame.mixer.Sound.play(self.son.krakenSpawn)
                self.tempsSansMob["kraken"]=-1
        if randDragon<self.fonctionDragon():
            tuileAutourJoueur=self.addTuileAutour(tuileAutourJoueur, 5)
            if tuileAutourJoueur[2]!=[]:
                self.groupMob.add(Mob(self, "dragon", self.pvDragon, self.vitesseDragon, random.choice(tuileAutourJoueur[2]), 700,aerien=True, attaque=self.attaqueDragon))  
                pygame.mixer.Sound.play(self.son.dragonSpawn) 
                self.tempsSansMob["dragon"]=-1
        
        if randYeti<self.fonctionYeti():
            tuileAutourJoueur=self.addTuileAutour(tuileAutourJoueur, 5)
            if tuileAutourJoueur[5]!=[]:
                self.groupMob.add(Mob(self, "yeti", self.pvYeti, self.vitesseYeti, random.choice(tuileAutourJoueur[5]), 500, attaque=self.attaqueYeti))
                pygame.mixer.Sound.play(self.son.yetiSpawn)
                self.tempsSansMob["yeti"]=-1

    def afficherText(self, text):
        text = self.police.render(str(text), True, (255, 255, 0))
        self.fenetre.blit(text, (400,400))
        self.text=text
    def displayTxt(self):
        self.fenetre.blit(self.text, (400,400))

    """
    def genererImg(self):
        global background_pil, premierPAss
        modification=False
        for y in range(generation.taille_matriceY):
            for x in range(generation.taille_matriceX):
                if self.map[y][x].aEteModifie:        

                    if self.map[y][x].isExplored:
                        if premierPAss:
                            background_pil.paste(self.map[y][x].imageO, (self.map[y][x].Xoriginal, self.map[y][x].Yoriginal), self.map[y][x].imageO)
                        else:
                            background_pil_superpose.paste(self.map[y][x].imageO, (self.map[y][x].Xoriginal, self.map[y][x].Yoriginal), self.map[y][x].imageO)
                    else :
                        if premierPAss:
                            background_pil.paste(self.imageFog, (self.map[y][x].Xoriginal, self.map[y][x].Yoriginal), self.imageFog)
                        else:
                            background_pil_superpose.paste(self.imageFog, (self.map[y][x].Xoriginal, self.map[y][x].Yoriginal), self.imageFog)
                            
                            
                    self.map[y][x].aEteModifie=False
                    modification=True                    
        if modification:

            if premierPAss:
                self.mapImg = pygame.image.frombuffer(background_pil.tobytes(), background_pil.size, "RGBA").convert_alpha()
                premierPAss=False
            else:
                
                a=background_pil_superpose.tobytes()
                #pygame.image.frombuffer(a, background_pil.size, "RGBA").convert_alpha()
                #self.mapImgSuperpose = pygame.image.frombuffer(background_pil_superpose.tobytes(), background_pil.size, "RGBA").convert_alpha()
            self.mapImgO = background_pil
            self.mapImgO_superpose = background_pil_superpose""" 
  

 
    def collerImageBackground(self, tuile):
        
        if tuile.isExplored:
            self.mapImgO.paste(tuile.imageO, (tuile.Xoriginal, tuile.Yoriginal), tuile.imageO)
        else:
            self.mapImgO.paste(self.imageFog, (tuile.Xoriginal, tuile.Yoriginal), self.imageFog)
        self.mapImg = pygame.image.frombuffer(self.mapImgO.tobytes(),self.mapImgO.size,'RGBA').convert_alpha()
            
    def openFog2(self):
        imgTemp = pygame.image.load("data/tuiles/0exploration.png").convert_alpha()
        imgTemp = pygame.transform.scale(imgTemp, (244, 142))
        
        return imgTemp

    def deleteFog(self,x,y):
        modification = False
        if self.verifierCo(x, y):
            if not self.map[y][x].isExplored:
                self.map[y][x].setExplored(True)
                modification=True
        return modification
                
        
