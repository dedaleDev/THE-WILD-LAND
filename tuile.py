import pygame
import random
from PIL import Image
class Tuile(pygame.sprite.Sprite):
    def __init__(self, type, posX, posY, game):
        super().__init__()
        self.game = game
        
        self.type = type
        self.canon = False
        
        
        self.probaSup_mer = 0
        self.probaSup_roche = 0
        self.probaSup_foret = 0
        self.probaSup_desert = 0
        self.probaSup_neige = 0
        
        self.autoriserNeige = False
        self.autoriserDesert = True
        
        self.posX = posX
        self.posY = posY
        
        self.image=self.loadImg(self.type)
        
        self.imageO=self.openImg(self.type)
        
        self.rect = self.image.get_rect()
        
        self.rect.x = self.avoirX(self.posY)
        self.rect.y = self.avoirY(self.posX, self.posY)

        self.estSelect = False
        self.isExplored = False
        
        self.masque = pygame.mask.from_surface(self.image)
        
    def getExplored(self):
        return self.isExplored
    def setExplored(self, bool):
        self.isExplored = bool

    def getRectX(self):
        return  self.rect.x

    def setSelect(self, bool):
        self.estSelect = bool

    def getRectY(self):
        return  self.rect.y

    def avoirX(self, posY, socle=False):
        if self.type == 2 or self.type==7:
            return posY*88 - (self.game.getAffichageTuile()[self.game.affichagePersonalise][0]/100*self.game.infoObject.current_w)
        else :
            return posY*88


    def avoirY(self, posX, posY, socle=False):
        if self.type == 2 or self.type==7:
            return posX*135+posY*6-self.game.affichageTuile[self.game.affichagePersonalise][1]/100*self.game.infoObject.current_h
        else:
            return posX*135+posY*6


    def setType(self, entier):
        self.type=entier

    
    def loadImg(self, type):
        #fonction pour charger la bonne image
        if type == 0:  # si exploration
            imgTemp = pygame.image.load("data/tuiles/0exploration.png").convert_alpha()
            imgTemp=pygame.transform.scale(imgTemp, (150, 150))
            return imgTemp
        if type == 1:  # si Terre
            imgTemp = pygame.image.load("data/tuiles/1Terre.png").convert_alpha()
        elif type == 2:#Roche
            imgTemp = pygame.image.load("data/tuiles/2Roche.png").convert_alpha()
        elif type == 3:#eau
                imgTemp = pygame.image.load("data/tuiles/3EauProfonde.png").convert_alpha()
        elif type == 4:#Foret
            imgTemp = pygame.image.load("data/tuiles/4Foret.png").convert_alpha()
        elif type == 5: #neige
            imgTemp = pygame.image.load("data/tuiles/5Neige.png").convert_alpha()
        elif type == 6: #Desert
            if random.randint(1,2) ==1:
                imgTemp = pygame.image.load("data/tuiles/6Desert.png").convert_alpha()
            else :
                imgTemp = pygame.image.load("data/tuiles/6desertCatus.png").convert_alpha()
        elif type == 7: #Barriere
            imgTemp = pygame.image.load("data/tuiles/7Barriere.png").convert_alpha()
            
        if self.type == 2 or self.type==7:
            imgTemp = pygame.transform.scale(imgTemp, (150, 190))
        else :
            imgTemp = pygame.transform.scale(imgTemp, (150, 150))
        return imgTemp
    
    def openImg(self, type):
        #fonction pour charger la bonne image
        if type ==0: # si exploration
            imgTemp = Image.open("data/tuiles/0exploration.png").convert('RGBA')
            imgTemp = imgTemp.resize((150, 150))
            return imgTemp
        if type == 1:  # si Terre
            imgTemp = Image.open("data/tuiles/1Terre.png").convert('RGBA')
        elif type == 2:#Roche
            imgTemp = Image.open("data/tuiles/2Roche.png").convert('RGBA')
        elif type == 3:#eau
                imgTemp = Image.open("data/tuiles/3EauProfonde.png").convert('RGBA')
        elif type == 4:#Foret
            imgTemp = Image.open("data/tuiles/4Foret.png").convert('RGBA')
        elif type == 5: #neige
            imgTemp = Image.open("data/tuiles/5Neige.png").convert('RGBA')
        elif type == 6: #Desert
            if random.randint(1,2) ==1:
                imgTemp = Image.open("data/tuiles/6Desert.png").convert('RGBA')
            else :
                imgTemp = Image.open("data/tuiles/6desertCatus.png").convert('RGBA')
        elif type == 7: #Barriere
            imgTemp = Image.open("data/tuiles/7Barriere.png").convert('RGBA')
            
        if self.type == 2 or self.type==7:
            imgTemp = imgTemp.resize((150, 190))
        else :
            imgTemp = imgTemp.resize((150, 150))
        return imgTemp


    def getType(self):
        return self.type

    def getProbaMer(self):
        return self.probaSup_mer
    
    def getProbaDesert(self):
        return self.probaSup_desert

    def getProbaRoche(self):
        return self.probaSup_roche

    def getProbaNeige(self):
        return self.probaSup_neige

    def getProbaForet(self):
        return self.probaSup_foret

    def getCanon(self):
        return self.canon

    def getAutoriserNeige(self):
        return self.autoriserNeige
    
    def getAutoriserDesert(self):
        return self.autoriserDesert
    
    def setInterdireDesert(self):
        self.autoriserDesert = False
    
    def setAutoriserNeige(self):
        self.autoriserNeige = True
    
    def interdireNeige(self):
        self.autoriserNeige = False
    
    def augmenterProbaMer(self, entier):
        self.probaSup_mer += entier

    def augmenterProbaRoche(self, entier):
        self.probaSup_roche += entier

    def augmenterProbaForet(self, entier):
        self.probaSup_foret += entier
    def augmenterProbaDesert(self, entier):
        self.probaSup_desert += entier
    def augmenterProbaNeige(self, entier):
        self.probaSup_neige += entier

    def estMontagne(self):
        return self.type==2
    
    def estMer(self):
        return self.type==3

    def decalerX(self, valeur):
        self.rect.x+=valeur
        
    def decalerY(self, valeur):
        self.rect.y+=valeur

