import imp
import pygame
import random
from PIL import Image
class ImageLoad():
    def __init__(self):
        self.listeImg = self.loadImg()
        self.listeImgO = self.loadImgO()
        self.listeImgItem = self.loadImgItem()
        
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
        imgTemp = pygame.image.load("data/tuiles/2Roche0.png").convert_alpha()
        imgTemp=pygame.transform.scale(imgTemp, (150, 150))
        listeImg.append(imgTemp)
    #eau
        imgTemp0 = pygame.image.load("data/tuiles/3Eau0.png").convert_alpha()
        imgTemp0=pygame.transform.scale(imgTemp0, (150, 150))
        
        imgTemp1 = pygame.image.load("data/tuiles/3Eau1.png").convert_alpha()
        imgTemp1=pygame.transform.scale(imgTemp1, (150, 150))
        
        imgTemp2 = pygame.image.load("data/tuiles/3Eau2.png").convert_alpha()
        imgTemp2=pygame.transform.scale(imgTemp2, (150, 150))
        
        imgTemp3 = pygame.image.load("data/tuiles/3Eau3.png").convert_alpha()
        imgTemp3=pygame.transform.scale(imgTemp3, (150, 150))
        listeImg.append((imgTemp0, imgTemp1, imgTemp2, imgTemp3))
    #Foret
        imgTemp0 = pygame.image.load("data/tuiles/4Foret0.png").convert_alpha()
        imgTemp0=pygame.transform.scale(imgTemp0, (150, 150))
        
        imgTemp1 = pygame.image.load("data/tuiles/4Foret1.png").convert_alpha()
        imgTemp1=pygame.transform.scale(imgTemp1, (150, 150))
        
        imgTemp2 = pygame.image.load("data/tuiles/4Foret2.png").convert_alpha()
        imgTemp2=pygame.transform.scale(imgTemp2, (150, 150))
        
        imgTemp3 = pygame.image.load("data/tuiles/4Foret3.png").convert_alpha()
        imgTemp3=pygame.transform.scale(imgTemp3, (150, 150))
        listeImg.append((imgTemp0, imgTemp1, imgTemp2, imgTemp3))
    #neige
        imgTemp0 = pygame.image.load("data/tuiles/5Neige0.png").convert_alpha()
        imgTemp0=pygame.transform.scale(imgTemp, (150, 150))
        
        
        imgTemp1 = pygame.image.load("data/tuiles/5Neige1.png").convert_alpha()
        imgTemp1=pygame.transform.scale(imgTemp1, (150, 150))
        
        imgTemp2 = pygame.image.load("data/tuiles/5Neige2.png").convert_alpha()
        imgTemp2=pygame.transform.scale(imgTemp2, (150, 150))
        listeImg.append((imgTemp0, imgTemp1, imgTemp2))
    #Desert
        imgTemp = pygame.image.load("data/tuiles/6Desert0.png").convert_alpha()
        imgTemp=pygame.transform.scale(imgTemp, (150, 150))
        imgTemp2 = pygame.image.load("data/tuiles/6Desert1.png").convert_alpha()
        imgTemp2 =pygame.transform.scale(imgTemp2, (150, 150))
        imgTemp3 = pygame.image.load("data/tuiles/6Desert2.png").convert_alpha()
        imgTemp3 =pygame.transform.scale(imgTemp3, (150, 150))
        listeImg.append((imgTemp, imgTemp2, imgTemp3))
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
            imgTemp = Image.open("data/tuiles/2Roche0.png").convert('RGBA')
            imgTemp = imgTemp.resize((150, 150))
            listeImgO.append(imgTemp)
#eau
            imgTemp0 = Image.open("data/tuiles/3Eau0.png").convert('RGBA')
            imgTemp0 = imgTemp0.resize((150, 150))
            
            imgTemp1 = Image.open("data/tuiles/3Eau1.png").convert('RGBA')
            imgTemp1 = imgTemp1.resize((150, 150))
            
            imgTemp2 = Image.open("data/tuiles/3Eau2.png").convert('RGBA')
            imgTemp2 = imgTemp2.resize((150, 150))
            
            imgTemp3 = Image.open("data/tuiles/3Eau3.png").convert('RGBA')
            imgTemp3 = imgTemp3.resize((150, 150))
            
            listeImgO.append((imgTemp0, imgTemp1, imgTemp2, imgTemp3))
            
            
#Foret
            imgTemp0 = Image.open("data/tuiles/4Foret0.png").convert('RGBA')
            imgTemp0 = imgTemp0.resize((150, 150))
            
            imgTemp1 = Image.open("data/tuiles/4Foret1.png").convert('RGBA')
            imgTemp1 = imgTemp1.resize((150, 150))
            
            imgTemp2 = Image.open("data/tuiles/4Foret2.png").convert('RGBA')
            imgTemp2 = imgTemp2.resize((150, 150))
            
            imgTemp3 = Image.open("data/tuiles/4Foret3.png").convert('RGBA')
            imgTemp3 = imgTemp3.resize((150, 150))
            
            listeImgO.append((imgTemp0, imgTemp1, imgTemp2, imgTemp3))
 #neige
            imgTemp0 = Image.open("data/tuiles/5Neige0.png").convert('RGBA')
            imgTemp0= imgTemp0.resize((150, 150))
            
            imgTemp1 = Image.open("data/tuiles/5Neige1.png").convert('RGBA')
            imgTemp1= imgTemp1.resize((150, 150))
            
            imgTemp2 = Image.open("data/tuiles/5Neige2.png").convert('RGBA')
            imgTemp2= imgTemp2.resize((150, 150))
            listeImgO.append((imgTemp0, imgTemp1, imgTemp2))
 #Desert

            imgTemp = Image.open("data/tuiles/6Desert0.png").convert('RGBA')
            imgTemp = imgTemp.resize((150, 150))
            imgTemp2 = Image.open("data/tuiles/6Desert1.png").convert('RGBA')
            imgTemp2 = imgTemp2.resize((150, 150))
            imgTemp3 = Image.open("data/tuiles/6Desert2.png").convert('RGBA')
            imgTemp3 = imgTemp3.resize((150, 150))
            listeImgO.append((imgTemp, imgTemp2, imgTemp3))
#Barriere
            imgTemp = Image.open("data/tuiles/7Barriere.png").convert('RGBA')
            imgTemp = imgTemp.resize((150, 150))
            listeImgO.append(imgTemp)

            return listeImgO

    def loadImgItem(self):
        listeImgItem = []
        imgTemp = pygame.image.load("data/batiments/icon/icon_forge.png").convert_alpha()
        imgTemp = pygame.transform.scale(imgTemp, (60,60))
        listeImgItem.append(("forge", imgTemp))
        
        imgTemp = pygame.image.load("data/batiments/icon/icon_moulin.png").convert_alpha()
        imgTemp = pygame.transform.scale(imgTemp, (60,60))
        listeImgItem.append(("moulin", imgTemp))
        
        imgTemp = pygame.image.load("data/batiments/icon/icon_scierie.png").convert_alpha()
        imgTemp = pygame.transform.scale(imgTemp, (60,60))
        listeImgItem.append(("scierie", imgTemp))
        
        imgTemp = pygame.image.load("data/batiments/icon/icon_port.png").convert_alpha()
        imgTemp = pygame.transform.scale(imgTemp, (60,60))
        listeImgItem.append(("port", imgTemp))
        return listeImgItem


    def returnImgO(self, type):
        if type==6:
            rand = random.randint(0,2)
            return self.listeImgO[type][rand]
        if type==3 or type==4:
            rand = random.randint(0, 3)
            return self.listeImgO[type][rand]
        if type==5:
            rand = random.randint(0,6)
            if rand%2==0:
                rand=2
            if rand==1 or rand == 3:
                rand = 0
            if rand == 5:
                rand=1

            return self.listeImgO[type][rand]
        return self.listeImgO[type]

    def returnImg(self, type):
        if type==6:
            rand = random.randint(0,2)
            return self.listeImg[type][rand] 
        if type==3 or type==4:
            rand = random.randint(0, 3)
            return self.listeImg[type][rand]  
        if type==5:
            rand = random.randint(0,8)
            if rand>1:
                rand=2
            return self.listeImg[type][rand]
        return self.listeImg[type]

             


    def returnImItem(self, nom):

        for elem in self.listeImgItem:
            if elem[0]==nom:
                return elem[1]
        assert(1==2)
        #Pas d'image d'item trouvé
        return False
