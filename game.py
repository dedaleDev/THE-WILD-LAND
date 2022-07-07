import random
import pygame
import generation
from imageLoad import ImageLoad
from PIL import Image
from mob import Mob
from joueur import Player
from sound import Sound
background_pil = Image.new('RGBA',(170*generation.taille_matriceX,170*generation.taille_matriceY), 0)
premierPAss=True
class Game(pygame.sprite.Sprite):
    def __init__(self, infoObject, fenetre):
        self.infoObject=infoObject
        self.tailleEcran = [(3840, 2160), (2560, 1440), (1920, 1080),(1536,864),(1280, 720), (800, 600), (640, 480)]
        self.affichageTuile = [(0.19, 2.77), (0.19, 2.77), (0.19, 2.77),(0.19, 4),(0.19, 2.77), (0.19, 2.77), (0, 0)]
        self.affichagePersonalise = self.affichage()
        self.decalageMontagneX = self.getAffichageTuile()[self.affichagePersonalise][0]/100*self.infoObject.current_w
        self.decalageMontagneY = self.affichageTuile[self.affichagePersonalise][1]/100*self.infoObject.current_h
        self.images = ImageLoad()
        self.son = Sound()
        
        self.imCollision = self.images.getImCollision()
        self.map = 0
        self.mapMontagneMer = 0
        self.imageFog = self.openFog()
        self.imageErreurRessource = self.openImageRessource()
        self.mapImg = 0
        self.mapImgO = 0
        self.mapMer = 0
        self.mapVide = 0
        self.listeCaseMer = 0
        self.listeCaseForet = 0
        self.listeCasePlaine=0
        self.listeCaseMontagne=0
        self.fenetre = fenetre
        self.listeCaseBatiment=[]
        self.taille_matriceY = generation.taille_matriceY
        self.taille_matriceX = generation.taille_matriceX
        
        self.groupMob = pygame.sprite.Group()
        self.groupProjectile = pygame.sprite.Group()
        self.groupDefense = pygame.sprite.Group()
        self.genererMatrice()
        self.joueur = Player(self,"joueur_1", 5)
        self.groupJoueur=pygame.sprite.Group()
        self.groupJoueur.add(self.joueur)
        
        self.probaGolemForet = 2
        self.probaOursin = 8
        self.probaKraken = 0
        self.probaMage = 0
        self.probaDragon = 0
        self.debutDePartie=0
        self.incendieDelay=0
        self.incendie=False
    def openImageRessource(self):
        im = pygame.image.load("data/menu/alerteRessource.png")
        im = pygame.transform.scale(im, (592*0.75, 155*0.75))
        return im
    
    def majCata(self):
        if self.joueur.indiceEcolo>60 and len(self.listeCaseBatiment)>0 and pygame.time.get_ticks()-self.incendieDelay >5000 and False: #INCENDIE
            indice=random.randint(0, len(self.listeCaseBatiment)-1)
            tuile = self.listeCaseBatiment[indice]
            self.listeCaseBatiment.pop(indice)
            self.incendie=True
            self.incendieDelay=pygame.time.get_ticks()
            return tuile


        
        
        
        
    
    
    def augmenterMob(self):
        if pygame.time.get_ticks()-self.debutDePartie > 120000*6: #12min 

            self.probaDragon = 2
            self.probaGolemForet = 5
            self.probaOursin = 3
            self.probaKraken = 4
            self.probaMage = 4
        elif pygame.time.get_ticks()-self.debutDePartie > 120000*5: #10min 
            self.probaDragon = 1
            self.probaGolemForet = 4
            self.probaOursin = 2
            self.probaKraken = 2
            self.probaMage = 3
        elif pygame.time.get_ticks()-self.debutDePartie > 120000*3.5: #7min 
            self.probaDragon = 0
            self.probaGolemForet = 4
            self.probaOursin = 2
            self.probaKraken = 1
            self.probaMage = 2
        elif pygame.time.get_ticks()-self.debutDePartie > 120000*2: #4min 
            self.probaDragon = 0
            self.probaGolemForet = 4
            self.probaOursin = 1
            self.probaKraken = 1
            self.probaMage = 1
        elif pygame.time.get_ticks()-self.debutDePartie > 120000*1.5: #3min 
            self.probaDragon = 0
            self.probaGolemForet = 3
            self.probaOursin = 0
            self.probaKraken = 1
            self.probaMage = 0
        elif pygame.time.get_ticks()-self.debutDePartie > 120000: #2min 
            self.probaDragon = 0
            self.probaGolemForet = 2
            self.probaOursin = 0
            self.probaKraken = 0
            self.probaMage = 0

    def verifierCo(self, x, y):
        return  x<generation.taille_matriceX and x >0 and y < generation.taille_matriceY and y>0
        
    def genererMatrice(self):
        self.map = generation.generation_matrice(self)
        self.mapMontagneMer, self.mapMer, self.mapVide, self.listeCaseMer, self.listeCaseForet, self.listeCasePlaine, self.listeCaseMontagne  = generation.generation_matriceMontagneMer(self.map)
        
    def checkCollision(self, joueur, listeMob):
        listeColide=[]
        now = pygame.time.get_ticks()
        for mob in listeMob :
            
            colide = mob.rect.colliderect(joueur.rect)
            if colide and now-joueur.lastDamage>joueur.cooldownDamage:
                joueur.takeDamage(mob.attack)
                joueur.lastDamage=now
                listeColide.append(colide)
            if mob.name=="mage":
                mob.lunchProjectile()
        return listeColide
                

    def affichage(self):
        for i in range(len(self.tailleEcran)):
            if self.tailleEcran[i][0] == self.infoObject.current_w and self.tailleEcran[i][1] == self.infoObject.current_h:
                return i
        return 2
    
    def getAffichageTuile(self):
        return self.affichageTuile

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
                            self.groupMob.add(Mob(self, "dragon", 100, 1, tuile, aerien=True))   
                    if tuile.estForet():
                        rand = random.randint(1,400)

                        if rand <= self.probaGolemForet:
                            self.groupMob.add(Mob(self, "golem_des_forets", 75, 2, tuile))
                        
                        rand = random.randint(1,400)
                        if rand<= self.probaMage:
                            self.groupMob.add(Mob(self, "mage", 50, 1, tuile))
                    if tuile.estPlaine():
                        rand = random.randint(1,400)
                        if rand <= self.probaOursin:
                            self.groupMob.add(Mob(self, "oursin", 150, 3, tuile, pique=True))
                    if tuile.estMer():
                        rand = random.randint(1,400)
                        if rand <= self.probaKraken:
                            self.groupMob.add(Mob(self, "kraken", 50, 1,tuile, aquatique=True))
                
    def genererImg(self):
        global background_pil, premierPAss
        modification=False
        for y in range(generation.taille_matriceY):
            for x in range(generation.taille_matriceX):
                if self.map[y][x].aEteModifie:        

                    if self.map[y][x].isExplored:
                        background_pil.paste(self.map[y][x].imageO, (self.map[y][x].Xoriginal, self.map[y][x].Yoriginal), self.map[y][x].imageO)
                    else :
                        background_pil.paste(self.imageFog, (self.map[y][x].Xoriginal, self.map[y][x].Yoriginal), self.imageFog)
                    self.map[y][x].aEteModifie=False
                    modification=True                    
        if modification:

            if premierPAss:
                self.mapImg = pygame.image.frombuffer(background_pil.tobytes(), background_pil.size, "RGBA").convert_alpha()

            self.mapImgO = background_pil


    def collerImageBackground(self, tuile):
        
        if tuile.isExplored:
            self.mapImgO.paste(tuile.imageO, (tuile.Xoriginal, tuile.Yoriginal), tuile.imageO)
        else:
            self.mapImgO.paste(self.imageFog, (tuile.Xoriginal, tuile.Yoriginal), self.imageFog)
        self.mapImg = pygame.image.frombuffer(self.mapImgO.tobytes(),self.mapImgO.size,'RGBA').convert_alpha()
            

    def openFog(self):
        imgTemp = Image.open("data/tuiles/0exploration.png").convert('RGBA')
        imgTemp = imgTemp.resize((150, 150))
        return imgTemp
    

    def deleteFog(self,x,y):
        modification = False
        if self.verifierCo(x, y):
            if not self.map[y][x].isExplored:
                self.map[y][x].setExplored(True)
                modification=True
        return modification
                
        
