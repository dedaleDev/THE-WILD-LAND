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
        imgTemp0 = pygame.image.load("data/tuiles/1Terre0.png").convert_alpha()
        imgTemp0=pygame.transform.scale(imgTemp0, (150, 150))
        
        imgTemp1 = pygame.image.load("data/tuiles/1Terre1.png").convert_alpha()
        imgTemp1=pygame.transform.scale(imgTemp1, (150, 150))
        
        imgTemp2 = pygame.image.load("data/tuiles/1Terre2.png").convert_alpha()
        imgTemp2=pygame.transform.scale(imgTemp2, (150, 150))
        
        imgTemp3 = pygame.image.load("data/tuiles/1Terre3.png").convert_alpha()
        imgTemp3=pygame.transform.scale(imgTemp3, (150, 150))
        
        imgTemp4 = pygame.image.load("data/tuiles/1Terre4.png").convert_alpha()
        imgTemp4=pygame.transform.scale(imgTemp4, (150, 150))
        
        listeImg.append((imgTemp0, imgTemp1, imgTemp2, imgTemp3, imgTemp4))
    #Roche
        imgTemp0 = pygame.image.load("data/tuiles/2Roche0.png").convert_alpha()
        imgTemp0=pygame.transform.scale(imgTemp0, (150, 150))
        
        imgTemp1 = pygame.image.load("data/tuiles/2Roche1.png").convert_alpha()
        imgTemp1=pygame.transform.scale(imgTemp1, (150, 150))
        
        imgTemp2 = pygame.image.load("data/tuiles/2Roche2.png").convert_alpha()
        imgTemp2=pygame.transform.scale(imgTemp2, (150, 150))
        
        imgTemp3 = pygame.image.load("data/tuiles/2Roche3.png").convert_alpha()
        imgTemp3=pygame.transform.scale(imgTemp3, (150, 150))
        
        listeImg.append((imgTemp0, imgTemp1, imgTemp2, imgTemp3))
    #eau
        imgTemp0 = pygame.image.load("data/tuiles/3Eau0.png").convert_alpha()
        imgTemp0=pygame.transform.scale(imgTemp0, (150, 150))
        
        imgTemp1 = pygame.image.load("data/tuiles/3Eau1.png").convert_alpha()
        imgTemp1=pygame.transform.scale(imgTemp1, (150, 150))
        
        imgTemp2 = pygame.image.load("data/tuiles/3Eau2.png").convert_alpha()
        imgTemp2=pygame.transform.scale(imgTemp2, (150, 150))
        
        imgTemp3 = pygame.image.load("data/tuiles/3Eau3.png").convert_alpha()
        imgTemp3=pygame.transform.scale(imgTemp3, (150, 150))

        imgTemp4 = pygame.image.load("data/tuiles/3Eau4.png").convert_alpha()
        imgTemp4=pygame.transform.scale(imgTemp4, (150, 150))
        listeImg.append((imgTemp0, imgTemp1, imgTemp2, imgTemp3,imgTemp4))
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
        imgTemp4 = pygame.image.load("data/tuiles/6Desert3.png").convert_alpha()
        imgTemp4 =pygame.transform.scale(imgTemp4, (150, 150))
        imgTemp5 = pygame.image.load("data/tuiles/6Desert4.png").convert_alpha()
        imgTemp5 =pygame.transform.scale(imgTemp5, (150, 150))
        listeImg.append((imgTemp, imgTemp2, imgTemp3, imgTemp4, imgTemp5))
    #Barriere
        imgTemp0 = pygame.image.load("data/tuiles/7Barriere0.png").convert_alpha()
        imgTemp0=pygame.transform.scale(imgTemp0, (150, 150))
        
        imgTemp1 = pygame.image.load("data/tuiles/7Barriere1.png").convert_alpha()
        imgTemp1=pygame.transform.scale(imgTemp1, (150, 150))
        
        imgTemp2 = pygame.image.load("data/tuiles/7Barriere2.png").convert_alpha()
        imgTemp2=pygame.transform.scale(imgTemp2, (150, 150))
        
        imgTemp3 = pygame.image.load("data/tuiles/7Barriere3.png").convert_alpha()
        imgTemp3=pygame.transform.scale(imgTemp3, (150, 150))
        listeImg.append((imgTemp0, imgTemp1, imgTemp2, imgTemp3))
        
        return listeImg

    
    def loadImgO(self):
        #fonction pour charger la bonne image
# si exploration
            listeImgO=[]
            imgTemp = Image.open("data/tuiles/0exploration.png").convert('RGBA')
            imgTemp = imgTemp.resize((150, 150))
            listeImgO.append(imgTemp)
# si Terre
            imgTemp0 = Image.open("data/tuiles/1Terre0.png").convert('RGBA')
            imgTemp0 = imgTemp0.resize((150, 150))
            
            imgTemp1 = Image.open("data/tuiles/1Terre1.png").convert('RGBA')
            imgTemp1 = imgTemp1.resize((150, 150))
            
            imgTemp2 = Image.open("data/tuiles/1Terre2.png").convert('RGBA')
            imgTemp2 = imgTemp2.resize((150, 150))
            
            imgTemp3 = Image.open("data/tuiles/1Terre3.png").convert('RGBA')
            imgTemp3 = imgTemp3.resize((150, 150))
            
            imgTemp4 = Image.open("data/tuiles/1Terre4.png").convert('RGBA')
            imgTemp4 = imgTemp4.resize((150, 150))
            listeImgO.append((imgTemp0, imgTemp1, imgTemp2, imgTemp3, imgTemp4))
#Roche  
            imgTemp0 = Image.open("data/tuiles/2Roche0.png").convert('RGBA')
            imgTemp0 = imgTemp0.resize((150, 150))
            
            imgTemp1 = Image.open("data/tuiles/2Roche1.png").convert('RGBA')
            imgTemp1 = imgTemp1.resize((150, 150))
            
            imgTemp2 = Image.open("data/tuiles/2Roche2.png").convert('RGBA')
            imgTemp2 = imgTemp2.resize((150, 150))
            
            imgTemp3 = Image.open("data/tuiles/2Roche3.png").convert('RGBA')
            imgTemp3 = imgTemp3.resize((150, 150))
            
            
            listeImgO.append((imgTemp0, imgTemp1, imgTemp2, imgTemp3))
#eau
            imgTemp0 = Image.open("data/tuiles/3Eau0.png").convert('RGBA')
            imgTemp0 = imgTemp0.resize((150, 150))
            
            imgTemp1 = Image.open("data/tuiles/3Eau1.png").convert('RGBA')
            imgTemp1 = imgTemp1.resize((150, 150))
            
            imgTemp2 = Image.open("data/tuiles/3Eau2.png").convert('RGBA')
            imgTemp2 = imgTemp2.resize((150, 150))
            
            imgTemp3 = Image.open("data/tuiles/3Eau3.png").convert('RGBA')
            imgTemp3 = imgTemp3.resize((150, 150))

            imgTemp4 = Image.open("data/tuiles/3Eau4.png").convert('RGBA')
            imgTemp4 = imgTemp4.resize((150, 150))
            
            listeImgO.append((imgTemp0, imgTemp1, imgTemp2, imgTemp3,imgTemp4))
            
            
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
            imgTemp4 = Image.open("data/tuiles/6Desert3.png").convert('RGBA')
            imgTemp4 = imgTemp4.resize((150, 150))
            imgTemp5 = Image.open("data/tuiles/6Desert4.png").convert('RGBA')
            imgTemp5 = imgTemp5.resize((150, 150))
            listeImgO.append((imgTemp, imgTemp2, imgTemp3, imgTemp4, imgTemp5))
#Barriere
            imgTemp0 = Image.open("data/tuiles/7Barriere0.png").convert('RGBA')
            imgTemp0 = imgTemp0.resize((150, 150))
            
            imgTemp1 = Image.open("data/tuiles/7Barriere1.png").convert('RGBA')
            imgTemp1 = imgTemp1.resize((150, 150))
            
            imgTemp2 = Image.open("data/tuiles/7Barriere2.png").convert('RGBA')
            imgTemp2 = imgTemp2.resize((150, 150))
            
            imgTemp3 = Image.open("data/tuiles/7Barriere3.png").convert('RGBA')
            imgTemp3 = imgTemp3.resize((150, 150))
            
            listeImgO.append((imgTemp0,imgTemp1, imgTemp2,imgTemp3))

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
        if type==6 or type==3 :
            rand = random.randint(0,4)
            return self.listeImgO[type][rand]
        if  type==4 or type==2 or type==7:
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
        if type==1:
            rand= random.randint(0,12)
            if rand in [0,1, 10]:
                rand = 0
            if rand in [2,3,8, 11]:
                rand = 1
            if rand in [4,5,7,12]:
                rand =2
            if rand in [6]:
                rand = 3
            if rand ==9:
                rand = 4

            return self.listeImgO[type][rand]
        return self.listeImgO[type]

    def returnImg(self, type):
        if type==6 or type ==3:
            rand = random.randint(0,4)
            return self.listeImg[type][rand] 
        if  type==4 or type==2 or type==7:
            rand = random.randint(0, 3)
            return self.listeImg[type][rand]  
        if type==5:
            rand = random.randint(0,8)
            if rand>1:
                rand=2
            return self.listeImg[type][rand]
        if type==1:
            rand= random.randint(0,12)
            if rand in [0,1, 9, 10]:
                rand = 0
            if rand in [2,3,8, 11]:
                rand = 1
            if rand in [4,5,7,12]:
                rand =2
            if rand in [6]:
                if random.randint(0,1):
                    rand = 3
                else :
                    rand = 2
            if rand ==9:
                if random.randint(0,1):
                    rand = 4
                else :
                    rand = 2
            return self.listeImg[type][rand]
        return self.listeImg[type]

             


    def returnImItem(self, nom):

        for elem in self.listeImgItem:
            if elem[0]==nom:
                return elem[1]
        assert(1==2)
        #Pas d'image d'item trouvé
        return False
