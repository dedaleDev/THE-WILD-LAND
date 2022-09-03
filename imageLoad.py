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
        self.etoile = pygame.image.load("data/ressources/etoile.png").convert_alpha()
        self.etoile = pygame.transform.scale(self.etoile, (self.etoile.get_height()*0.05,self.etoile.get_width()*0.05))
        self.coffre = pygame.image.load("data/ressources/coffre.png").convert_alpha()
        self.coffre = pygame.transform.scale(self.coffre, (self.coffre.get_height()*0.15,self.coffre.get_width()*0.15))
        
        self.coffre = self.loadAnnimCoffre()

        self.moulinAnnim = self.loadAnnimMoulin()
        self.ventiloAnnim = self.loadAnnimVentilo()
        self.golemAnnim = self.loadAnnimGolem()
        self.krakenAnnim = self.loadAnnimKraken()
        self.yetiAnnim = self.loadAnnimYeti()
        self.mageAnnim = self.loadAnnimMage()
        self.dragonAnnim = self.loadAnnimDragon()
        
        self.annim1Terre3 = self.loadAnnimTuile("1Terre3_", 1, 11)
        self.annim1Terre4 = self.loadAnnimTuile("1Terre4_", 1, 17)
        self.elevage = self.loadAnnimTuile("elevage_", 2, 19)
        self.annim3eau0 = self.loadAnnimTuile("3eau0_", 1,14)
        self.annim3eau4 = self.loadAnnimTuile("3eau4_", 1,21)
        
        self.annim4foret0 = self.loadAnnimTuile("4foret0_", 1,12)
        self.annim4foret1 = self.loadAnnimTuile("4foret1_", 1,28)
        self.annim4foret2 = self.loadAnnimTuile("4foret2_", 1,12)
        
        self.lootEau = self.loadAnnimRessource("eau", 1,21)
        self.lootPierre = self.loadAnnimRessource("pierre", 1,20)
        self.lootBois = self.loadAnnimRessource("bois", 1,22)
        self.lootFood = self.loadAnnimRessource("viande", 1,20)
        
        for i in range(15):
            self.annim3eau0.append(self.annim3eau0[-1])

        for i in range(50):
            self.annim3eau4.append(self.annim3eau0[-1])
            self.annim4foret1.append(self.annim4foret1[-1])
        self.annim3eau1 = self.loadAnnimTuile("3eau1_", 1,17)
        for i in range(5):
            self.annim3eau1.append(self.annim3eau0[-1])
        self.annim3eau2 = self.loadAnnimTuile("3eau2_", 1,15)
        for i in range(5):
            self.annim3eau2.append(self.annim3eau0[-1])
        
    def loadAnnimTuile(self, nomTuile, idebut, ifin):
        liste=[]
        for i in range(idebut, ifin+1):
            im = pygame.image.load("data/animationTuiles/"+nomTuile+str(i)+".png").convert_alpha()
            liste.append(im)
            
        return liste
        
    def loadAnnimRessource(self, nomRessource, idebut, ifin):
        liste=[]
        for i in range(idebut, ifin+1):
            im=pygame.image.load("data/ressources/"+nomRessource+"/"+nomRessource+"_"+str(i)+".png").convert_alpha()
            liste.append(pygame.transform.scale(im, (im.get_width()*0.3, im.get_height()*0.3)))
        return liste
    
    def loadAnnimCoffre(self):
        liste=[]
        for i in range(1, 15):
            im = pygame.image.load("data/ressources/coffre_"+str(i)+".png").convert_alpha()
            liste.append(pygame.transform.scale(im, (100,100)))
        return liste
        
    def loadAnnimVentilo(self):
        liste = []
        for i in range(1, 26):    
            if i != 16:
                im = pygame.image.load("data/batiments/ventilo/ventilo_"+str(i)+".png").convert_alpha()
                liste.append(im)
        return liste    
    
    def loadAnnimMoulin(self):
        liste = []
        for i in range(1, 23):    
            if i != 6:
                im = pygame.image.load("data/batiments/moulin/Moulin_"+str(i)+".png").convert_alpha()
                liste.append(im)
            #im = pygame.transform.scale(im, (164, 351))  
        return liste
    def loadImgVille(self):
        im = pygame.image.load("data/batiments/ville.png").convert_alpha()
        im = pygame.transform.scale(im, (164, 351))    
        return im
    #97* 19
    def loadAnnimGolem(self):
        listeAnnim = []
        for i in range(1,9):
            im = pygame.image.load("data/personnages/golem/golem_des_forets_"+str(i)+".png").convert_alpha()
            im = pygame.transform.scale(im, (241*0.55, 249*0.50))
            listeAnnim.append(im)
        return listeAnnim
    
    def loadAnnimKraken(self):
        listeAnnim = []
        for i in range(1,10):
            im = pygame.image.load("data/personnages/kraken/kraken_"+str(i)+".png").convert_alpha()
            im = pygame.transform.scale(im, (279*0.5, 177*0.5))
            listeAnnim.append(im)
        return listeAnnim
    
    def loadAnnimMage(self):
        listeAnnim = []
        for i in range(1,11):
            im = pygame.image.load("data/personnages/mage/mage_"+str(i)+".png").convert_alpha()
            im = pygame.transform.scale(im, (111*0.62, 214*0.62))
            listeAnnim.append(im)
        return listeAnnim
    
    def loadAnnimDragon(self):
        listeAnnim = []
        for i in range(2,31):
            im = pygame.image.load("data/personnages/dragon/dragon_"+str(i)+".png").convert_alpha()
            im = pygame.transform.scale(im, (436*0.3, 473*0.3))
            listeAnnim.append(im)
        return listeAnnim
    
    def loadAnnimYeti(self):
        listeAnnim = []
        for i in range(1,13):
            im = pygame.image.load("data/personnages/yeti/yeti_"+str(i)+".png").convert_alpha()
            im = pygame.transform.scale(im, (205*0.5, 318*0.5))
            listeAnnim.append(im)
        return listeAnnim
    
    def loadAnnimGolem(self):
        listeAnnim = []
        for i in range(1,9):
            im = pygame.image.load("data/personnages/golem/golem_des_forets_"+str(i)+".png").convert_alpha()
            im = pygame.transform.scale(im, (241*0.55, 249*0.50))
            listeAnnim.append(im)
        return listeAnnim
    
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
        
        imgTemp5 = pygame.image.load("data/tuiles/1Terre5.png").convert_alpha()
        imgTemp5=pygame.transform.scale(imgTemp5, (246, 144))
        
        imgTemp6 = pygame.image.load("data/tuiles/1Terre6.png").convert_alpha()
        imgTemp6=pygame.transform.scale(imgTemp6, (246, 144))
        
        listeImg.append((imgTemp0, imgTemp1, imgTemp2, imgTemp3, imgTemp4, imgTemp5, imgTemp6))
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

    def returnImg(self, type):
        annim = []
        clockMax = None
        if type==0:
                print("probleme de type")
                assert(False)
        if type==6 or type==3 :
            
            rand = random.randint(0,4)
            if rand==0 and type==3: #grande vagues
                clockMax=7
                annim=self.annim3eau0
            elif rand==1 and type==3:
                clockMax=7
                annim=self.annim3eau1
            elif rand==2 and type==3:
                clockMax=7
                annim=self.annim3eau2
            if rand == 4 and type==3:
                
                clockMax=5
                if random.randint(0,1):
                    annim=self.annim3eau4
                else :
                    annim=[]
            if annim :
                clockAnnim=random.randint(0,len(annim)-1)
            else :
                clockAnnim=0
            return self.listeImg[type][rand], clockMax, annim, clockAnnim
        if  type==4 or type==2 or type==7:
            rand = random.randint(0, 3)
            if type==4 and rand==1:
                if random.randint(0,1):
                    annim=self.annim4foret1
                else :
                    annim=[]
                clockMax=10
            if type==4 and rand==0:
                annim=self.annim4foret0
                clockMax=10
            if type==4 and rand ==2:
                annim=self.annim4foret2
                clockMax=10
            if annim :
                clockAnnim=random.randint(0,len(annim)-1)
            else :
                clockAnnim=0
            return self.listeImg[type][rand], clockMax, annim, clockAnnim
        if type==5:
            rand = random.randint(0,6)
            if rand%2==0:
                rand=2
            elif rand == 1 or rand == 3:
                rand = 0
            elif rand == 5:
                rand=1
            if annim :
                clockAnnim=random.randint(0,len(annim)-1)
            else :
                clockAnnim=0
            return self.listeImg[type][rand], clockMax, annim, clockAnnim
        
        if type==1:
            rand = random.randint(0,12)
            if rand in [0,1, 10]:
                rand = 0
            elif rand in [3,8, 11]:
                rand = 1 #CLASSIQUE
            elif rand in [5,7,12]:
                rand = 2 #CLASSIQUE
            elif rand in [4]:
                rand = 5 #FLEURS 1
            elif rand in [2]:
                rand = 6 #FLEURS 2
            elif rand in [6]:
                rand = 3 #CLASSIQUE
                annim=self.annim1Terre3
                clockMax=10
            elif rand ==9:
                rand = 4 #ARBRE
                annim=self.annim1Terre4
                clockMax=10
            if annim :
                clockAnnim=random.randint(0,len(annim)-1)
            else :
                clockAnnim=0
            return self.listeImg[type][rand], clockMax, annim, clockAnnim
        print("probleme")
        return self.listeImg[type], clockMax, annim, random.randint(0,len(annim)-1)

    
    def loadImgAcide(self):
        scale = (45*1, 47*1)
        tempIgmg = pygame.image.load("data/projectiles/acide.png").convert_alpha()
        tempIgmg = pygame.transform.scale(tempIgmg, scale)
        return tempIgmg
    
    def loadImgFleche(self):
        scale = (572*0.065, 70*0.065)
        tempIgmg = pygame.image.load("data/projectiles/fleche.png").convert_alpha()
        tempIgmg = pygame.transform.scale(tempIgmg, scale)
        return tempIgmg
    def loadImgPotion(self):
        scale = (512*0.065, 712*0.065)
        tempIgmg = pygame.image.load("data/projectiles/potion.png").convert_alpha()
        tempIgmg = pygame.transform.scale(tempIgmg, scale)
        return tempIgmg
    def loadImgBouleDeNeige(self):
        scale = (381*0.15, 410*0.15)
        tempIgmg = pygame.image.load("data/projectiles/bouleDeNeige.png").convert_alpha()
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
        img = pygame.image.load(chemin+nom+".png").convert_alpha()
        return img
    
    def getImCollision(self):
        im = pygame.image.load("data/personnages/degat.png").convert_alpha()
        return pygame.transform.scale(im ,(40,40))
    def returnImItem(self, nom):
        for elem in self.listeImgItem:
            if elem[0]==nom:
                return elem[1]
        assert(False)
        #Pas d'image d'item trouvé


    def ImInfoBullItem(self, nom, chemin="data/batiments/infoBulle/info_"):
        img = pygame.image.load(chemin+nom+".png").convert_alpha()
        return img
