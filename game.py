from email import feedparser
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
modeFacile=True
modeNormal = False
modeDifficile=False

if modeFacile:
    pvKraken = 50
    pvDragon = 300
    pvOursin = 100
    pvMage = 50
    pvGolem = 75
    
    vitesseKraken = 2
    vitesseOursin = 3 
    vitesseMage = 2
    vitesseGolem = 2
    vitesseDragon = 2
    
elif modeNormal :
    pvKraken = 100
    pvDragon = 400
    pvOursin = 125
    pvMage = 100
    pvGolem = 100
    
    vitesseKraken = 2
    vitesseOursin = 3
    vitesseMage =2
    vitesseGolem =3
    vitesseDragon = 3

elif modeDifficile :
    pvKraken = 150
    pvDragon = 500
    pvOursin = 150
    pvMage = 150
    pvGolem = 125
    
    vitesseKraken = 2
    vitesseOursin = 4
    vitesseMage = 3
    vitesseGolem = 3
    vitesseDragon = 4

    


premierPAss=True
class Game(pygame.sprite.Sprite):
    def __init__(self, infoObject, fenetre, mapChoisie, pointSpawn):
        posRectChargement = infoObject.current_w*1/4, infoObject.current_h*3/4
        self.infoObject=infoObject
        diagonalEcran = math.sqrt(infoObject.current_w**2 + infoObject.current_h**2)
        taillePolice = round(3/100*diagonalEcran)
        font = pygame.font.Font("data/menu/font.ttf", taillePolice//2)
        
        self.updateBar(fenetre, 0, posRectChargement, "chargement des images...", font)
        
        
        """self.tailleEcran = [(3840, 2160), (2560, 1440), (1920, 1080),(1536,864),(1280, 720), (800, 600), (640, 480)]
        self.affichageTuile = [(0.19, 2.77), (0.19, 2.77), (0.19, 2.77),(0.19, 4),(0.19, 2.77), (0.19, 2.77), (0, 0)]
        self.affichagePersonalise = self.affichage()"""
        self.images = ImageLoad()
        self.updateBar(fenetre, 25, posRectChargement, "chargement des sons...", font)
        self.son = Sound()
        self.updateBar(fenetre, 75, posRectChargement, "chargement de la carte...", font)
        
        self.imCollision = self.images.getImCollision()
        self.map = 0
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
        if not mapChoisie:
            self.taille_matriceY = int(aideCSV.valCorrespondante("taille_matriceY"))
            self.taille_matriceX = int(aideCSV.valCorrespondante("taille_matriceX"))
        else:
            self.taille_matriceY = len(mapChoisie)
            self.taille_matriceX = len(mapChoisie[0])
            
            
        self.groupMob = pygame.sprite.Group()
        self.groupProjectile = pygame.sprite.Group()
        self.groupDefense = pygame.sprite.Group()
        self.groupCoffre = pygame.sprite.Group()
        self.groupLoot = pygame.sprite.Group()
        
        self.genererMatrice(mapChoisie)
        self.updateBar(fenetre, 100, posRectChargement, "preparez vous...", font)
        self.joueur = Player(self,"joueur0", 5, pointSpawn)
        self.groupJoueur=pygame.sprite.Group()
        self.groupJoueur.add(self.joueur)
        
        self.probaGolemForet = 2
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
        
        self.tempsMort = 0 #compte les millisecondes de temps passe dans le menu etc
        self.lastPause = 0
        
    def openImageRessource(self):
        im = pygame.image.load("data/menu/alerteRessource.png").convert_alpha()
        im = pygame.transform.scale(im, (592*0.75, 155*0.75))
        return im
    
    def tempsJeu(self):
        return pygame.time.get_ticks()- self.tempsMort
    
    def updateBar(self, fenetre, valeurChargement, posRectChargement, texte, font):
        valeurChargement = valeurChargement/100

        texte = font.render(texte, True, "White")
        pygame.draw.rect(fenetre, (70,70,70), (posRectChargement, (100*self.infoObject.current_w*0.005 , 3)))
        pygame.draw.rect(fenetre, (255,255,255), (posRectChargement, (100*self.infoObject.current_w*0.005*valeurChargement , 3)))
        
        pygame.draw.rect(fenetre, (0,0,0), ((posRectChargement[0], posRectChargement[1]+10), (1000 , 1000))) #actualisation du texte
        fenetre.blit(texte, (posRectChargement[0], posRectChargement[1]+10))
        pygame.display.flip()
    
    def majCata(self):
        if self.joueur.indiceEcolo>50 and len(self.listeCaseBatiment)>0 and self.tempsJeu()-self.incendieDelay > 6000 : #INCENDIE
            if not random.randint(0,2) or True: #quand on tombe sur un 0, donc incendie toute les 3 min environ
                indice=random.randint(0, len(self.listeCaseBatiment)-1)
                tuile = self.listeCaseBatiment[indice]
                self.listeCaseBatiment.pop(indice)
                self.incendie=True
                self.incendieDelay=self.tempsJeu()
                return tuile


        
        
        
        
        
    
    
    def augmenterMob(self):
        
        if self.tempsJeu() > 120000*6: #12min 
            self.probaDragon = 4
            self.probaGolemForet = 5
            self.probaOursin = 4
            self.probaKraken = 4
            self.probaMage = 4
            self.probaYeti = 4
            
        elif self.tempsJeu() > 120000*5: #10min 
            self.probaDragon = 1
            self.probaGolemForet = 4
            self.probaOursin = 2
            self.probaKraken = 2
            self.probaMage = 3
            self.probaYeti = 0
        elif self.tempsJeu() > 120000*4 and not self.huitMin: #8min 
            self.probaDragon = 0
            self.probaGolemForet = 4
            self.probaOursin = 2
            self.probaKraken = 1
            self.probaMage = 2
            self.probaYeti = 0
            self.huitMin=True
            #pygame.mixer.Sound.play(self.son.musique4)
        
        elif self.tempsJeu() > 120000*2.75 and not self.cinqMin : #5min30secondes 
            self.cinqMin=True
            #pygame.mixer.Sound.play(self.son.musique3)
        elif self.tempsJeu() > 120000*2 : #4min
            self.probaDragon = 0
            self.probaGolemForet = 4
            self.probaOursin = 1
            self.probaKraken = 1
            self.probaMage = 1
            self.probaYeti = 0
        elif self.tempsJeu() > 120000*1.5 and not self.troisMin: #3min 
            self.probaDragon = 0
            self.probaGolemForet = 3
            self.probaOursin = 0
            self.probaKraken = 1
            self.probaMage = 0
            self.probaYeti = 0
            self.troisMin=True
            
            #pygame.mixer.Sound.play(self.son.musique2)
            
        elif self.tempsJeu() > 120000: #2min
            self.probaDragon = 0
            self.probaGolemForet = 2
            self.probaOursin = 0
            self.probaKraken = 0
            self.probaMage = 0
            self.probaYeti = 0

    def verifierCo(self, x, y):
        return  x<self.taille_matriceX and x >=0 and y < self.taille_matriceY and y>=0
        
    def genererMatrice(self, mapChoisie):
        if not mapChoisie:
            self.map = generation.generation_matrice(self)
        else :
            self.map = generation.typeToTuile(mapChoisie, self)
        self.mapMontagneMer, self.mapMer, self.mapVide, self.listeCaseMer, self.listeCaseForet, self.listeCasePlaine, self.listeCaseMontagne  = generation.generation_matriceMontagneMer(self.map, self)
        
    def checkCollision(self, joueur, listeMob):
        listeColide=[]
        now = self.tempsJeu()
        for mob in listeMob :
            #colide = mob.rect.colliderect(joueur.rect)
            colide = pygame.sprite.spritecollide(joueur, listeMob, False, pygame.sprite.collide_mask)
            if colide and now-joueur.lastDamage>joueur.cooldownDamage:
                joueur.takeDamage(mob.attack)
                joueur.lastDamage=now
                listeColide.append(colide)
            if mob.name=="mage" or mob.name=="yeti": 
                mob.lunchProjectile()
                
        return listeColide
                

    """def affichage(self):
        for i in range(len(self.tailleEcran)):
            if self.tailleEcran[i][0] == self.infoObject.current_w and self.tailleEcran[i][1] == self.infoObject.current_h:
                return i
        return 2"""
    
    """def getAffichageTuile(self):
        return self.affichageTuile"""

    def avoirTuileJoueur(self, joueur):
        return self.map[joueur.posY][joueur.posX]
    
    
    def spawMob(self):
        for y in range(-5, 5):
            for x in range(-5,5):
                if self.verifierCo(self.joueur.posX+x, self.joueur.posY+y) and (y!=0 or x!=0):
                    tuile = self.map[self.joueur.posY+y][self.joueur.posX+x]
                    if tuile.type==2:
                        rand = random.randint(1,400)
                        if rand <= self.probaDragon:
                            self.groupMob.add(Mob(self, "dragon", 300, 2, tuile, 700,aerien=True))   
                            pygame.mixer.Sound.play(self.son.dragonSpawn)
                    if tuile.estForet():
                        rand = random.randint(1,400)
                        if rand <= self.probaGolemForet:
                            self.groupMob.add(Mob(self, "golem_des_forets", 75, 2, tuile, 100))
                            pygame.mixer.Sound.play(self.son.golem_des_foretsSpawn)
                        rand = random.randint(1,400)
                        if rand<= self.probaMage:
                            self.groupMob.add(Mob(self, "mage", 50, 1, tuile, 125))
                            pygame.mixer.Sound.play(self.son.mageSpawn)
                    if tuile.estPlaine():
                        rand = random.randint(1,400)
                        if rand <= self.probaOursin:
                            self.groupMob.add(Mob(self, "oursin", 100, 3, tuile, 150, pique=True))
                            pygame.mixer.Sound.play(self.son.oursinSpawn)
                    if tuile.estMer():
                        rand = random.randint(1,400)
                        if rand <= self.probaKraken:
                            self.groupMob.add(Mob(self, "kraken", 50, 1,tuile, 100, aquatique=True))
                            pygame.mixer.Sound.play(self.son.krakenSpawn)
                    if tuile.type==5:
                        rand = random.randint(1,400)
                        if rand <= self.probaYeti:
                            self.groupMob.add(Mob(self, "yeti", 300, 2, tuile, 500))
                            pygame.mixer.Sound.play(self.son.yetiSpawn)
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
                
        
