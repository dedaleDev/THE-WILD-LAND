import pygame
import random
#from PIL import Image

class ImageLoad():
    def __init__(self):
        infoObject = pygame.display.Info()
        self.listeImg = self.loadImg()
        #self.listeImgO = self.loadImgO()
        self.listeImgItem = self.loadImgItem()
        self.imgFleche = self.loadImgFleche()
        self.imgAcide = self.loadImgAcide()
        self.imgPotion = self.loadImgPotion()
        self.imgBouleDeNeige =self.loadImgBouleDeNeige()
        self.ville = self.loadImgVille()
        self.mort = pygame.image.load("data/menu/defaite.png").convert_alpha()
        self.mort = pygame.transform.scale(self.mort,(infoObject.current_w,infoObject.current_h))
        self.victoire = pygame.image.load("data/menu/victoire.png").convert_alpha()
        self.victoire = pygame.transform.scale(self.victoire,(infoObject.current_w,infoObject.current_h))
        self.coffre = pygame.image.load("data/ressources/coffre.png")
        self.coffre = pygame.transform.scale(self.coffre, (self.coffre.get_height()*0.15,self.coffre.get_width()*0.15))
        self.etoile = pygame.image.load("data/ressources/etoile.png")
        self.etoile = pygame.transform.scale(self.etoile, (self.etoile.get_height()*0.05,self.etoile.get_width()*0.05))
        
        self.moulinAnnim = self.loadAnnimMoulin()
        
    def loadAnnimMoulin(self):
        liste = []
        for i in range(1, 23):    
            if i != 6:
                im = pygame.image.load("data/tuiles/moulin/Moulin_"+str(i)+".png").convert_alpha()
                liste.append(im)
            #im = pygame.transform.scale(im, (164, 351))  
        return liste
    def loadImgVille(self):
        im = pygame.image.load("data/batiments/ville.png")
        im = pygame.transform.scale(im, (164, 351))    
        return im
    
    
    def loadImg(self):
        
        listeImg = []

        #fonction pour charger la bonne image
    # si exploration
        imgTemp = pygame.image.load("data/tuiles/debug.png").convert_alpha()
        imgTemp=pygame.transform.scale(imgTemp, (246, 144))
        listeImg.append(imgTemp)
    # si Terre
        imgTemp0 = pygame.image.load("data/tuiles/1Terre0.png").convert_alpha()
        imgTemp0=pygame.transform.scale(imgTemp0, (246, 144))
        
        imgTemp1 = pygame.image.load("data/tuiles/1Terre1.png").convert_alpha()
        imgTemp1=pygame.transform.scale(imgTemp1, (246, 144))
        
        imgTemp2 = pygame.image.load("data/tuiles/1Terre2.png").convert_alpha()
        imgTemp2=pygame.transform.scale(imgTemp2, (246, 144))
        
        imgTemp3 = pygame.image.load("data/tuiles/1Terre3.png").convert_alpha()
        imgTemp3=pygame.transform.scale(imgTemp3, (246, 144))
        
        imgTemp4 = pygame.image.load("data/tuiles/1Terre4.png").convert_alpha()
        imgTemp4=pygame.transform.scale(imgTemp4, (246, 144))
        
        listeImg.append((imgTemp0, imgTemp1, imgTemp2, imgTemp3, imgTemp4))
    #Roche
        imgTemp0 = pygame.image.load("data/tuiles/2Roche0.png").convert_alpha()
        imgTemp0=pygame.transform.scale(imgTemp0, (246, 144))
        
        imgTemp1 = pygame.image.load("data/tuiles/2Roche1.png").convert_alpha()
        imgTemp1=pygame.transform.scale(imgTemp1, (246, 144))
        
        imgTemp2 = pygame.image.load("data/tuiles/2Roche2.png").convert_alpha()
        imgTemp2=pygame.transform.scale(imgTemp2, (246, 144))
        
        imgTemp3 = pygame.image.load("data/tuiles/2Roche3.png").convert_alpha()
        imgTemp3=pygame.transform.scale(imgTemp3, (246, 144))
        
        listeImg.append((imgTemp0, imgTemp1, imgTemp2, imgTemp3))
    #eau
        imgTemp0 = pygame.image.load("data/tuiles/3Eau0.png").convert_alpha()
        imgTemp0=pygame.transform.scale(imgTemp0, (246, 144))
        
        imgTemp1 = pygame.image.load("data/tuiles/3Eau1.png").convert_alpha()
        imgTemp1=pygame.transform.scale(imgTemp1, (246, 144))
        
        imgTemp2 = pygame.image.load("data/tuiles/3Eau2.png").convert_alpha()
        imgTemp2=pygame.transform.scale(imgTemp2, (246, 144))
        
        imgTemp3 = pygame.image.load("data/tuiles/3Eau3.png").convert_alpha()
        imgTemp3=pygame.transform.scale(imgTemp3, (246, 144))

        imgTemp4 = pygame.image.load("data/tuiles/3Eau4.png").convert_alpha()
        imgTemp4=pygame.transform.scale(imgTemp4, (246, 144))
        listeImg.append((imgTemp0, imgTemp1, imgTemp2, imgTemp3,imgTemp4))
    #Foret
        imgTemp0 = pygame.image.load("data/tuiles/4Foret0.png").convert_alpha()
        imgTemp0=pygame.transform.scale(imgTemp0, (246, 144))
        
        imgTemp1 = pygame.image.load("data/tuiles/4Foret1.png").convert_alpha()
        imgTemp1=pygame.transform.scale(imgTemp1, (246, 144))
        
        imgTemp2 = pygame.image.load("data/tuiles/4Foret2.png").convert_alpha()
        imgTemp2=pygame.transform.scale(imgTemp2, (246, 144))
        
        imgTemp3 = pygame.image.load("data/tuiles/4Foret3.png").convert_alpha()
        imgTemp3=pygame.transform.scale(imgTemp3, (246, 144))
        listeImg.append((imgTemp0, imgTemp1, imgTemp2, imgTemp3))
    #neige
        imgTemp0 = pygame.image.load("data/tuiles/5Neige0.png").convert_alpha()
        imgTemp0=pygame.transform.scale(imgTemp0, (246, 144))
        
        
        imgTemp1 = pygame.image.load("data/tuiles/5Neige1.png").convert_alpha()
        imgTemp1=pygame.transform.scale(imgTemp1, (246, 144))
        
        imgTemp2 = pygame.image.load("data/tuiles/5Neige2.png").convert_alpha()
        imgTemp2=pygame.transform.scale(imgTemp2, (246, 144))
        listeImg.append((imgTemp0, imgTemp1, imgTemp2))
    #Desert
        imgTemp = pygame.image.load("data/tuiles/6Desert0.png").convert_alpha()
        imgTemp=pygame.transform.scale(imgTemp, (246, 144))
        imgTemp2 = pygame.image.load("data/tuiles/6Desert1.png").convert_alpha()
        imgTemp2 =pygame.transform.scale(imgTemp2, (246, 144))
        imgTemp3 = pygame.image.load("data/tuiles/6Desert2.png").convert_alpha()
        imgTemp3 =pygame.transform.scale(imgTemp3, (246, 144))
        imgTemp4 = pygame.image.load("data/tuiles/6Desert3.png").convert_alpha()
        imgTemp4 =pygame.transform.scale(imgTemp4, (246, 144))
        imgTemp5 = pygame.image.load("data/tuiles/6Desert4.png").convert_alpha()
        imgTemp5 =pygame.transform.scale(imgTemp5, (246, 144))
        listeImg.append((imgTemp, imgTemp2, imgTemp3, imgTemp4, imgTemp5))
    #Barriere
        imgTemp0 = pygame.image.load("data/tuiles/7Barriere0.png").convert_alpha()
        imgTemp0=pygame.transform.scale(imgTemp0, (246, 144))
        
        imgTemp1 = pygame.image.load("data/tuiles/7Barriere1.png").convert_alpha()
        imgTemp1=pygame.transform.scale(imgTemp1, (246, 144))
        
        imgTemp2 = pygame.image.load("data/tuiles/7Barriere2.png").convert_alpha()
        imgTemp2=pygame.transform.scale(imgTemp2, (246, 144))
        
        imgTemp3 = pygame.image.load("data/tuiles/7Barriere3.png").convert_alpha()
        imgTemp3=pygame.transform.scale(imgTemp3, (246, 144))
        listeImg.append((imgTemp0, imgTemp1, imgTemp2, imgTemp3))
        
        return listeImg

    def loadImgItem(self):
        listeImgItem = []
        imgTemp = pygame.image.load("data/batiments/icon/icon_forge.png").convert_alpha()
        imgTemp = pygame.transform.scale(imgTemp, (60,60))
        listeImgItem.append(("forge", imgTemp))
        imgTemp = pygame.image.load("data/batiments/icon/icon_mine.png").convert_alpha()
        imgTemp = pygame.transform.scale(imgTemp, (60,60))
        listeImgItem.append(("mine", imgTemp))
        
        imgTemp = pygame.image.load("data/batiments/icon/icon_moulin.png").convert_alpha()
        imgTemp = pygame.transform.scale(imgTemp, (60,60))
        listeImgItem.append(("moulin", imgTemp))
        
        imgTemp = pygame.image.load("data/batiments/icon/icon_scierie.png").convert_alpha()
        imgTemp = pygame.transform.scale(imgTemp, (60,60))
        listeImgItem.append(("scierie", imgTemp))
        
        imgTemp = pygame.image.load("data/batiments/icon/icon_port.png").convert_alpha()
        imgTemp = pygame.transform.scale(imgTemp, (60,60))
        listeImgItem.append(("port", imgTemp))
        
        imgTemp = pygame.image.load("data/batiments/icon/icon_champs.png").convert_alpha()
        imgTemp = pygame.transform.scale(imgTemp, (60,60))
        listeImgItem.append(("champs", imgTemp))
        
        imgTemp = pygame.image.load("data/batiments/icon/icon_elevage.png").convert_alpha()
        imgTemp = pygame.transform.scale(imgTemp, (60,60))
        listeImgItem.append(("elevage", imgTemp))
        imgTemp = pygame.image.load("data/batiments/icon/icon_tour.png").convert_alpha()
        imgTemp = pygame.transform.scale(imgTemp, (60,60))
        listeImgItem.append(("tour", imgTemp))
        imgTemp = pygame.image.load("data/batiments/icon/icon_pieux.png").convert_alpha()
        imgTemp = pygame.transform.scale(imgTemp, (60,60))
        listeImgItem.append(("pieux", imgTemp))
        imgTemp = pygame.image.load("data/batiments/icon/icon_sableMouvant.png").convert_alpha()
        imgTemp = pygame.transform.scale(imgTemp, (60,60))
        listeImgItem.append(("sableMouvant", imgTemp))
        imgTemp = pygame.image.load("data/batiments/icon/icon_mortier.png").convert_alpha()
        imgTemp = pygame.transform.scale(imgTemp, (60,60))
        listeImgItem.append(("mortier", imgTemp))
        imgTemp = pygame.image.load("data/batiments/icon/icon_trou.png").convert_alpha()
        imgTemp = pygame.transform.scale(imgTemp, (60,60))
        listeImgItem.append(("trou", imgTemp))
        
        imgTemp = pygame.image.load("data/batiments/icon/icon_frigo.png").convert_alpha()
        imgTemp = pygame.transform.scale(imgTemp, (60,60))
        listeImgItem.append(("frigo", imgTemp))
        
        imgTemp = pygame.image.load("data/batiments/icon/icon_ventilo.png").convert_alpha()
        imgTemp = pygame.transform.scale(imgTemp, (60,60))
        listeImgItem.append(("ventilo", imgTemp))
        
        imgTemp = pygame.image.load("data/batiments/icon/icon_ville.png").convert_alpha()
        imgTemp = pygame.transform.scale(imgTemp, (60,60))
        listeImgItem.append(("ville", imgTemp))
        
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
        if type==0:
                print("probleme")
        if type==6 or type==3 :
            rand = random.randint(0,4)
            return self.listeImg[type][rand]
        if  type==4 or type==2 or type==7:
            rand = random.randint(0, 3)
            return self.listeImg[type][rand]
        if type==5:
            rand = random.randint(0,6)
            if rand%2==0:
                rand=2
            if rand==1 or rand == 3:
                rand = 0
            if rand == 5:
                rand=1

            return self.listeImg[type][rand]
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
            
            return self.listeImg[type][rand]
        print("probleme")
        return self.listeImg[type]

    
    def loadImgAcide(self):
        scale = (45*1, 47*1)
        tempIgmg = pygame.image.load("data/projectiles/acide.png")
        tempIgmg = pygame.transform.scale(tempIgmg, scale)
        return tempIgmg
    
    def loadImgFleche(self):
        scale = (572*0.065, 70*0.065)
        tempIgmg = pygame.image.load("data/projectiles/fleche.png")
        tempIgmg = pygame.transform.scale(tempIgmg, scale)
        return tempIgmg
    def loadImgPotion(self):
        scale = (512*0.065, 712*0.065)
        tempIgmg = pygame.image.load("data/projectiles/potion.png")
        tempIgmg = pygame.transform.scale(tempIgmg, scale)
        return tempIgmg
    def loadImgBouleDeNeige(self):
        scale = (381*0.15, 410*0.15)
        tempIgmg = pygame.image.load("data/projectiles/bouleDeNeige.png")
        tempIgmg = pygame.transform.scale(tempIgmg, scale)
        return tempIgmg
    
    def loadImgProjectile(self, nom, angle=False):
        if nom== "mortier":
            tempIgmg= self.imgAcide
            if angle:
                tempIgmg = pygame.transform.rotate(tempIgmg, angle)
            return tempIgmg
        if nom== "tour":
            tempIgmg= self.imgFleche
            if angle:
                tempIgmg = pygame.transform.rotate(tempIgmg, angle)
            return tempIgmg
        if nom =="mage":
            tempIgmg= self.imgPotion
            if angle:
                tempIgmg = pygame.transform.rotate(tempIgmg, angle)
            return tempIgmg
        if nom == "yeti":
            tempIgmg = self.imgBouleDeNeige
            if angle:
                tempIgmg = pygame.transform.rotate(tempIgmg, angle)
            return tempIgmg
        assert False, ("LoadImgProjectile n'as pas trouvé d'image correspondante a ", nom)
    
    def ImInfoBulleMob(self, nom, chemin="data/personnages/infoBulle/info_"):
        img = pygame.image.load(chemin+nom+".png")
        return img
    
    def getImCollision(self):
        im = pygame.image.load("data/personnages/degat.png")
        return pygame.transform.scale(im ,(40,40))
    def returnImItem(self, nom):
        for elem in self.listeImgItem:
            if elem[0]==nom:
                return elem[1]
        assert(False)
        #Pas d'image d'item trouvé


    def ImInfoBullItem(self, nom, chemin="data/batiments/infoBulle/info_"):
        img = pygame.image.load(chemin+nom+".png")
        return img
