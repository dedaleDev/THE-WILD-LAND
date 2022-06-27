import imp
import pygame
import random
from PIL import Image
class ImageLoad():
    def __init__(self):
        self.listeImg = self.loadImg()
        self.listeImgO = self.loadImgO()
        
        
    def loadImg(self):
        
        listeImg = []

        #fonction pour charger la bonne image
    # si exploration
        imgTemp = pygame.image.load("data/tuiles/0exploration.png").convert_alpha()
        imgTemp=pygame.transform.scale(imgTemp, (150, 150))
        listeImg.append(imgTemp)
    # si Terre
        imgTemp = pygame.image.load("data/tuiles/1Terre.png").convert_alpha()
        imgTemp=pygame.transform.scale(imgTemp, (150, 150))
        listeImg.append(imgTemp)
    #Roche
        imgTemp = pygame.image.load("data/tuiles/2Roche.png").convert_alpha()
        imgTemp=pygame.transform.scale(imgTemp, (150, 150))
        listeImg.append(imgTemp)
    #eau
        imgTemp = pygame.image.load("data/tuiles/3EauProfonde.png").convert_alpha()
        imgTemp=pygame.transform.scale(imgTemp, (150, 150))
        listeImg.append(imgTemp)
    #Foret
        imgTemp = pygame.image.load("data/tuiles/4Foret.png").convert_alpha()
        imgTemp=pygame.transform.scale(imgTemp, (150, 150))
        listeImg.append(imgTemp)
    #neige
        imgTemp = pygame.image.load("data/tuiles/5Neige.png").convert_alpha()
        imgTemp=pygame.transform.scale(imgTemp, (150, 150))
        listeImg.append(imgTemp)
    #Desert
        imgTemp = pygame.image.load("data/tuiles/6Desert.png").convert_alpha()
        imgTemp=pygame.transform.scale(imgTemp, (150, 150))
        imgTemp2 = pygame.image.load("data/tuiles/6desertCatus.png").convert_alpha()
        imgTemp2 =pygame.transform.scale(imgTemp2, (150, 150))
        listeImg.append((imgTemp, imgTemp2))
    #Barriere
        imgTemp = pygame.image.load("data/tuiles/7Barriere.png").convert_alpha()
        imgTemp=pygame.transform.scale(imgTemp, (150, 150))
        listeImg.append(imgTemp)
        return listeImg

    
    def loadImgO(self):
        #fonction pour charger la bonne image
# si exploration
            listeImgO=[]
            imgTemp = Image.open("data/tuiles/0exploration.png").convert('RGBA')
            imgTemp = imgTemp.resize((150, 150))
            listeImgO.append(imgTemp)
# si Terre
            imgTemp = Image.open("data/tuiles/1Terre.png").convert('RGBA')
            imgTemp = imgTemp.resize((150, 150))
            listeImgO.append(imgTemp)
#Roche  
            imgTemp = Image.open("data/tuiles/2Roche.png").convert('RGBA')
            imgTemp = imgTemp.resize((150, 150))
            listeImgO.append(imgTemp)
#eau
            imgTemp = Image.open("data/tuiles/3EauProfonde.png").convert('RGBA')
            imgTemp = imgTemp.resize((150, 150))
            listeImgO.append(imgTemp)
#Foret
            imgTemp = Image.open("data/tuiles/4Foret.png").convert('RGBA')
            imgTemp = imgTemp.resize((150, 150))
            listeImgO.append(imgTemp)
 #neige
            imgTemp = Image.open("data/tuiles/5Neige.png").convert('RGBA')
            imgTemp = imgTemp.resize((150, 150))
            listeImgO.append(imgTemp)
 #Desert

            imgTemp = Image.open("data/tuiles/6Desert.png").convert('RGBA')
            imgTemp = imgTemp.resize((150, 150))
            imgTemp2 = Image.open("data/tuiles/6desertCatus.png").convert('RGBA')
            imgTemp2 = imgTemp2.resize((150, 150))
            listeImgO.append((imgTemp, imgTemp2))
#Barriere
            imgTemp = Image.open("data/tuiles/7Barriere.png").convert('RGBA')
            imgTemp = imgTemp.resize((150, 150))
            listeImgO.append(imgTemp)
            
            return listeImgO

    def returnImgO(self, type):
        if type==6:
            rand = random.randint(0,1)
            return self.listeImgO[type][rand]
        return self.listeImgO[type]

    def returnImg(self, type):
        if type==6:
            rand = random.randint(0,1)
            return self.listeImg[type][rand]        
        return self.listeImg[type]



