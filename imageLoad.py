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
        self.imgJoueur =self.loadImgJoueur()
        self.imgBossElec =self.loadImgbossElec()
        self.ville = self.loadImgVille()
        self.mort = pygame.image.load("data/menu/defaite.png").convert_alpha()
        self.mort = pygame.transform.scale(self.mort,(infoObject.current_w,infoObject.current_h))
        self.victoire = pygame.image.load("data/menu/victoire.png").convert_alpha()
        self.victoire = pygame.transform.scale(self.victoire,(infoObject.current_w,infoObject.current_h))
        self.etoile = pygame.image.load("data/ressources/etoile.png").convert_alpha()
        self.etoile = pygame.transform.scale(self.etoile, (self.etoile.get_height()*0.05,self.etoile.get_width()*0.05))
        self.coffre = pygame.image.load("data/ressources/coffre.png").convert_alpha()
        self.coffre = pygame.transform.scale(self.coffre, (self.coffre.get_height()*0.15,self.coffre.get_width()*0.15))
        
        
        self.fondForet = pygame.image.load("data/tuiles/fondForet.png").convert_alpha()
        self.fondJungle = pygame.image.load("data/tuiles/fondJungle.png").convert_alpha()
        self.armure = self.loadImArmure()
        self.coffre = self.loadAnnimCoffre()

        self.backgroundArene = self.loadImgBackArene()

        self.moulinAnnim = self.loadAnnimMoulin()
        self.mortierAnnim = self.loadAnnimMortier()
        self.ventiloAnnim = self.loadAnnimVentilo()
        self.frigoAnnim = self.loadAnnimFrigo()
        self.golemAnnim, self.golemAnnimSpawn = self.loadAnnimGolem()
        self.oursinAnnim = self.loadAnnimOursin()
        self.krakenAnnim = self.loadAnnimKraken()
        self.yetiAnnim = self.loadAnnimYeti()
        self.mageAnnim = self.loadAnnimMage()
        self.dragonAnnim = self.loadAnnimDragon()
        self.oiseauAnnim = self.loadAnnimOiseau(random.randint(0,1))
        
        self.oiseau2Annim = self.loadAnnimOiseau2()
        self.renardAnnim = self.loadAnnimRenard()
        
        self.chameauAnnim = self.loadAnnimChameau()
        self.lapinAnnim = self.loadAnnimLapin()
        
        
        self.backVolcan=pygame.image.load("data/tuiles/backVolcan.png").convert_alpha()
        self.statueBois=pygame.image.load("data/batiments/statueBois.png").convert_alpha()
        self.statuePierre=pygame.image.load("data/batiments/statuePierre.png").convert_alpha()
        self.statueEau=pygame.image.load("data/batiments/statueEau.png").convert_alpha()
        self.statueFood=pygame.image.load("data/batiments/statueFood.png").convert_alpha()
        self.annim1Terre3 = self.loadAnnimTuile("1Terre3_", 1, 11)
        self.annim1Terre4 = self.loadAnnimTuile("1Terre4_", 1, 17)
        self.elevage = self.loadAnnimTuile("elevage_", 2, 19)
        self.annim3eau0 = self.loadAnnimTuile("3eau0_", 1,9)
        self.annim3eau4 = self.loadAnnimTuile("3eau4_", 1,21)
        
        self.annim2Roche1 = self.loadAnnimTuile("2Roche1_", 1,1)
        self.annim2Roche2 = self.loadAnnimTuile("2Roche2_", 1,1)
        self.annim2Roche3 = self.loadAnnimTuile("2Roche3_", 1,1)
        self.annim2Roche4 = self.loadAnnimTuile("2Roche4_", 1,6)
        
        self.mineAnnim = self.loadAnnimTuile("mine_", 1,1)
        self.forgeAnnim = self.loadAnnimTuile("forge_", 1,18)
        
        self.annim7Barriere0 = self.loadAnnimTuile("7Barriere0_", 1,1)
        self.annim7Barriere1 = self.loadAnnimTuile("7Barriere1_", 1,24)
        self.annim7Barriere2 = self.loadAnnimTuile("7Barriere2_", 0,220)
        self.annim7Barriere3 = self.loadAnnimTuile("7Barriere3_", 1,12)
        
        self.annim4foret0 = self.loadAnnimTuile("4foret0_", 1,12)
        self.annim4foret1 = self.loadAnnimTuile("4foret1_", 1,28)
        self.annim4foret2 = self.loadAnnimTuile("4foret2_", 1,12)
        
        self.annim8violet0 = self.loadAnnimTuileViolet(0)
        self.annim8violet1 = self.loadAnnimTuileViolet(2)
        self.annim8violet3 = self.loadAnnimTuileViolet(3)
        
        
        self.annim6desert4 = self.loadAnnimTuile("6desert4_", 1,16)
        self.surbrillance = self.loadAnnimSurbrillance()
        self.lootEau = self.loadAnnimRessource("eau", 1,21)
        self.lootPierre = self.loadAnnimRessource("pierre", 1,20)
        self.lootBois = self.loadAnnimRessource("bois", 1,22)
        self.lootFood = self.loadAnnimRessource("viande", 1,20)
        
        self.boss = pygame.image.load("data/personnages/boss/boss1.png")
        
        self.clickBuild = self.loadAnnimClickBuild()
        self.moveBox = self.loadAnnimBoxMove()
        self.boomBox = self.loadAnnimBoxBoom()
        self.inventaire = self.loadInventaire()
        
        self.arene=self.loadAnnimArene()
        
        for i in range(15):
            self.annim3eau0.append(self.annim3eau0[-1])
            self.annim7Barriere3.append(self.annim7Barriere3[-1])
        
        for i in range(5):
            self.annim2Roche1.append(self.annim2Roche1[0])
            self.annim2Roche2.append(self.annim2Roche2[0])
            self.annim2Roche3.append(self.annim2Roche3[0])
            self.annim3eau0.append(self.annim3eau0[-1])
        for i in range(30):
            self.frigoAnnim.append(self.frigoAnnim[0])
        
        for i in range(50):
            self.annim3eau4.append(self.annim3eau0[-1])
            self.annim4foret1.append(self.annim4foret1[-1])
            self.annim6desert4.append(self.annim6desert4[-1])
            
        self.annim3eau1 = self.loadAnnimTuile("3eau1_", 1,17)
        for i in range(5):
            self.annim3eau1.append(self.annim3eau0[-1])
        
        self.annim3eau3 = self.loadAnnimTuileEau()
        self.annim3eau2 = self.loadAnnimTuileEau(True)
        
    def loadImgBackArene(self):
        liste=[]
        for i in range(1,134):
            im = pygame.image.load("data/animationTuiles/background_arene/background ("+str(i)+").jpg").convert_alpha()
            liste.append(im)
        return liste
    
    def loadImgBackMonde(self):
        liste=[]
        for i in range(1,84):
            im = pygame.image.load("data/animationTuiles/background_monde/background_"+str(i)+".jpeg").convert_alpha()
            liste.append(im)
        return liste
    
    def loadInventaire(self):
        im = pygame.image.load("data/menu/menu_tuile.png").convert()
        im = pygame.transform.scale(im, (758/2,178/2))
        return im
    def loadAnnimClickBuild(self):
        liste=[]
        for i in range(2, 28):
            im = pygame.image.load("data/animationTuiles/click/click ("+str(i)+").png").convert_alpha()
            im=pygame.transform.scale(im, (40,40))
            liste.append(im)
        return liste
    
    def loadAnnimBoxMove(self):
        liste=[]
        for i in range(1, 17):
            im = pygame.image.load("data/animationTuiles/boxMove/Box ("+str(i)+").png").convert_alpha()
            im = pygame.transform.scale(im, (340,400))
            liste.append(im)
        return liste
    def loadAnnimBoxBoom(self):
        liste=[]
        for i in range(2, 34):
            im = pygame.image.load("data/animationTuiles/boxMove/boomBox ("+str(i)+").png").convert_alpha()
            im = pygame.transform.scale(im, (340,400))
            liste.append(im)
        return liste
    def loadAnnimTuileEau(self, bool=False):
        liste=[]
        if not bool:
            for i in range(1, 193):
                im = pygame.image.load("data/animationTuiles/eau/3eau3 ("+str(i)+").png").convert_alpha()
                liste.append(im)
        else:
            for i in range(1, 197):
                im = pygame.image.load("data/animationTuiles/eau/dauphin/3eau2_"+str(i)+".png").convert_alpha()
                liste.append(im)
            
        return liste
    
    def loadAnnimTuileViolet(self, j):
        liste=[]
        if j == 0:
            iMax = 52
        if j==2:
            iMax=53
        if j ==3:
            iMax=53
        for i in range(1, iMax):
            im = pygame.image.load("data/animationTuiles/violet/8violet"+str(j)+"/8violet"+str(j)+"_"+str(i)+".png").convert_alpha()
            liste.append(im)
        return liste
    
    def loadAnnimArene(self):
        liste=[]
        for i in range(1, 96):
            im = pygame.image.load("data/animationTuiles/areneBoss/areneBoss ("+str(i)+").png").convert_alpha()
            liste.append(im)
        return liste
    def loadAnnimSurbrillance(self):
        liste = []
        for i in range(1,202):
              im = pygame.image.load("data/animationTuiles/surbrillance2/surbrillance ("+str(i)+").png").convert_alpha()
              liste.append(im)
        return liste
    
    def loadAnnimTuile(self, nomTuile, idebut, ifin):
        liste=[]
        for i in range(idebut, ifin+1):
            im = pygame.image.load("data/animationTuiles/"+nomTuile+str(i)+".png").convert_alpha()
            liste.append(im)
            
        return liste
    def statue(self, type):
        if type==4:
            return self.statueBois
        if type==2:
            return self.statuePierre
        if type==1:
            return self.statueFood
        if type==3:
            return self.statueEau
    def loadImArmure(self):
        liste=[]
        for i in range(1,5):
            liste.append(pygame.transform.scale(pygame.image.load("data/personnages/armure"+str(i)+".png").convert_alpha(), (75,75)))
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
    
    def loadAnnimFrigo(self):
        liste = []
        for i in range(1, 15):    
            if i != 16:
                im = pygame.image.load("data/batiments/frigo/frigo_"+str(i)+".png").convert_alpha()
                liste.append(im)
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
        for i in range(1, 198):    
            if i != 6:
                im = pygame.image.load("data/batiments/moulin/moulin_"+str(i)+".png").convert_alpha()
                liste.append(im)
                
            #im = pygame.transform.scale(im, (164, 351))  
        return liste
    
    def loadAnnimMortier(self):
        liste = []
        for i in range(1, 12):    
            if i != 6:
                im = pygame.image.load("data/batiments/mortier/mortier"+str(i)+".png").convert_alpha()
                liste.append(im)
            #im = pygame.transform.scale(im, (164, 351))  
        for i in range(12):
            liste.append(liste[0])
        return liste
    
    def loadImgVille(self):
        im = pygame.image.load("data/batiments/ville.png").convert_alpha()
        #im = pygame.transform.scale(im, (164, 351))    
        return im
    #97* 19

    def loadAnnimGolem(self):
        listeAnnim = []
        for i in range(1,9):
            im = pygame.image.load("data/personnages/golem/golem_des_forets_"+str(i)+".png").convert_alpha()
            im = pygame.transform.scale(im, (241*0.55, 249*0.50))
            listeAnnim.append(im)
        ###SPAWN
        listeAnnimSpawn=[]
        for i in range(56):
            im = pygame.image.load("data/personnages/golem/golem_des_forets_spawn"+str(i)+".png").convert_alpha()
            im = pygame.transform.scale(im, (241*0.55, 249*0.50))
            listeAnnimSpawn.append(im)
        return listeAnnim, listeAnnimSpawn
    
    def loadAnnimKraken(self):
        listeAnnim = []
        for i in range(1,69):
            im = pygame.image.load("data/personnages/kraken/kraken ("+str(i)+").png").convert_alpha()
            im = pygame.transform.scale(im, (279*0.5, 177*0.5))
            im=pygame.transform.flip(im, True, False)
            listeAnnim.append(im)
        return listeAnnim
    
    
    def loadAnnimOursin(self):
        listeAnnim = []
        for i in range(0,46):
            im = pygame.image.load("data/personnages/oursin/oursinSpawn"+str(i)+".png").convert_alpha()
            im = pygame.transform.scale(im, (175*0.56, 142*0.56))
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
    
    def loadAnnimOiseau(self, int2):
        listeAnnim = []
        if int2:
            for i in range(1,21):
                im = pygame.image.load("data/personnages/oiseau/oiseau ("+str(i)+").png").convert_alpha()
                im = pygame.transform.scale(im, (240*0.3, 314*0.3))
                im=pygame.transform.flip(im, True, False)
                listeAnnim.append(im)
            return listeAnnim
        else:
            for i in range(21,33):
                im = pygame.image.load("data/personnages/oiseau/oiseau ("+str(i)+").png").convert_alpha()
                #im = pygame.transform.scale(im, (240*0.3, 314*0.3))
                #im=pygame.transform.flip(im, True, False)
                listeAnnim.append(im)
            return listeAnnim
    
    def loadAnnimLapin(self):
        listeAnnim = []
        for i in range(1,25):
            im = pygame.image.load("data/personnages/lapin/lapin ("+str(i)+").png").convert_alpha()
            im = pygame.transform.scale(im, (im.get_width()*0.5, im.get_height()*0.5))
            #im=pygame.transform.flip(im, True, False)
            listeAnnim.append(im)
        return listeAnnim
    
    def loadAnnimOiseau2(self):
        listeAnnim = []
        for i in range(1,10):
            im = pygame.image.load("data/personnages/oiseau/oiseau2 ("+str(i)+").png").convert_alpha()
            im = pygame.transform.scale(im, (240*0.3, 314*0.3))
            listeAnnim.append(im)
        return listeAnnim
    
    def loadAnnimRenard(self):
        listeAnnim = []
        """for i in range(1,10):
            im = pygame.image.load("data/personnages/renard/renard"+str(i)+".png").convert_alpha()
            im = pygame.transform.scale(im, (62*0.8, 55*0.8))
            im = pygame.transform.flip(im, 1,0)
            listeAnnim.append(im)"""
        for i in range(10,19):
            im = pygame.image.load("data/personnages/renard/renard"+str(i)+".png").convert_alpha()
            im = pygame.transform.scale(im, (62, 55))
            im = pygame.transform.flip(im, 1,0)
            listeAnnim.append(im)
        return listeAnnim
    def loadAnnimChameau(self):
        listeAnnim = []
        for i in range(1,18):
            im = pygame.image.load("data/personnages/chameau/chameau ("+str(i)+").png").convert_alpha()
            im = pygame.transform.scale(im, (127, 110))
            listeAnnim.append(im)
        return listeAnnim
    
    def loadAnnimYeti(self):
        listeAnnim = []
        for i in range(1,13):
            im = pygame.image.load("data/personnages/yeti/yeti_"+str(i)+".png").convert_alpha()
            im = pygame.transform.scale(im, (205*0.5, 318*0.5))
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
        
        
        imgTemp1 = pygame.image.load("data/tuiles/4Foret1.png").convert_alpha()
        
        
        imgTemp2 = pygame.image.load("data/tuiles/4Foret2.png").convert_alpha()
        
        imgTemp3 = pygame.image.load("data/tuiles/4Foret3.png").convert_alpha()
        
        imgTemp4 = pygame.image.load("data/tuiles/4Foret4.png").convert_alpha()
        
        
        imgTemp5 = pygame.image.load("data/tuiles/4Foret5.png").convert_alpha()
        
        
        imgTemp6 = pygame.image.load("data/tuiles/4Foret6.png").convert_alpha()
        
        imgTemp7 = pygame.image.load("data/tuiles/4Foret7.png").convert_alpha()
        
        imgTemp8 = pygame.image.load("data/tuiles/4Foret8.png").convert_alpha()
        listeImg.append((imgTemp0, imgTemp1, imgTemp2, imgTemp3, imgTemp4, imgTemp5, imgTemp6, imgTemp7, imgTemp8))
    #neige
        imgTemp0 = pygame.image.load("data/tuiles/5Neige0.png").convert_alpha()
        imgTemp0=pygame.transform.scale(imgTemp0, (246, 144))
        
        
        imgTemp1 = pygame.image.load("data/tuiles/5Neige1.png").convert_alpha()
        imgTemp1=pygame.transform.scale(imgTemp1, (246, 144))
        
        imgTemp2 = pygame.image.load("data/tuiles/5Neige2.png").convert_alpha()
        imgTemp2=pygame.transform.scale(imgTemp2, (246, 144))

        imgTemp3 = pygame.image.load("data/tuiles/5Neige3.png").convert_alpha()
        imgTemp3=pygame.transform.scale(imgTemp3, (246, 144))
        listeImg.append((imgTemp0, imgTemp1, imgTemp2, imgTemp3))
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
    #Electrique
        imgTemp0 = pygame.image.load("data/tuiles/debug.png").convert_alpha()
        imgTemp0=pygame.transform.scale(imgTemp0, (246, 144))
        imgTemp1 = pygame.image.load("data/tuiles/debug.png").convert_alpha()
        imgTemp1=pygame.transform.scale(imgTemp1, (246, 144))
        listeImg.append((imgTemp0, imgTemp1))
    #Violet
        imgTemp0 = pygame.image.load("data/tuiles/8violet1.png").convert_alpha()
        imgTemp0=pygame.transform.scale(imgTemp0, (246, 144))
        
        imgTemp1 = pygame.image.load("data/tuiles/8violet4.png").convert_alpha()
        imgTemp1=pygame.transform.scale(imgTemp1, (246, 144))
        listeImg.append((imgTemp0, imgTemp1))
        
    #jungle
        imgTemp0 = pygame.image.load("data/tuiles/9jungle0.png").convert_alpha()
        
        imgTemp1 = pygame.image.load("data/tuiles/9jungle1.png").convert_alpha()
        
        imgTemp2 = pygame.image.load("data/tuiles/9jungle2.png").convert_alpha()
    
        imgTemp3 = pygame.image.load("data/tuiles/9jungle3.png").convert_alpha()
        
        imgTemp3 = pygame.image.load("data/tuiles/9jungle3.png").convert_alpha()
        
        imgTemp4 = pygame.image.load("data/tuiles/9jungle4.png").convert_alpha()
        
        imgTemp5 = pygame.image.load("data/tuiles/9jungle5.png").convert_alpha()
        imgTemp6 = pygame.image.load("data/tuiles/9jungle6.png").convert_alpha()
        imgTemp7 = pygame.image.load("data/tuiles/9jungle7.png").convert_alpha()

        
        
        listeImg.append((imgTemp0, imgTemp1, imgTemp2, imgTemp3, imgTemp4, imgTemp5, imgTemp6, imgTemp7))

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
        
        imgTemp = pygame.image.load("data/batiments/icon/armure1.png").convert_alpha()
        imgTemp = pygame.transform.scale(imgTemp, (60,60))
        listeImgItem.append(("armure1", imgTemp))
        
        imgTemp = pygame.image.load("data/batiments/icon/armure2.png").convert_alpha()
        imgTemp = pygame.transform.scale(imgTemp, (60,60))
        listeImgItem.append(("armure2", imgTemp))
        
        imgTemp = pygame.image.load("data/batiments/icon/armure3.png").convert_alpha()
        imgTemp = pygame.transform.scale(imgTemp, (60,60))
        listeImgItem.append(("armure3", imgTemp))
        
        imgTemp = pygame.image.load("data/batiments/icon/armure4.png").convert_alpha()
        imgTemp = pygame.transform.scale(imgTemp, (60,60))
        listeImgItem.append(("armure4", imgTemp))
        
        imgTemp = pygame.image.load("data/batiments/icon/icon_statueEau.png").convert_alpha()
        imgTemp = pygame.transform.scale(imgTemp, (60,60))
        listeImgItem.append(("statueEau", imgTemp))
        
        imgTemp = pygame.image.load("data/batiments/icon/icon_statuePierre.png").convert_alpha()
        imgTemp = pygame.transform.scale(imgTemp, (60,60))
        listeImgItem.append(("statuePierre", imgTemp))
        
        imgTemp = pygame.image.load("data/batiments/icon/icon_statueFood.png").convert_alpha()
        imgTemp = pygame.transform.scale(imgTemp, (60,60))
        listeImgItem.append(("statueFood", imgTemp))
        
        imgTemp = pygame.image.load("data/batiments/icon/icon_statueBois.png").convert_alpha()
        imgTemp = pygame.transform.scale(imgTemp, (60,60))
        listeImgItem.append(("statueBois", imgTemp))
        return listeImgItem

    def returnImg(self, type):
        annim = []
        clockMax = None
        if type==0:
                print("probleme de type")
                assert(False)
        if type==6 or type==3 :
            
            rand = random.randint(0,4)
            if type==3:
                if random.randint(0,5):
                    rand = 3
                else:
                    rand=2
            if rand == 4 and type==6: #arbre desert
                clockMax=7
                annim=self.annim6desert4
            if rand==0 and type==3: #grande vagues
                clockMax=7
                annim=self.annim3eau0
            if rand==1 and type==3:
                clockMax=7
                annim=self.annim3eau1
            if rand==2 and type==3:
                clockMax=2
                annim=self.annim3eau2
                
            elif rand==3 and type==3: #mer classique
                clockMax=2
                annim=self.annim3eau3
            if rand == 4 and type==3:
                
                clockMax=5
                if random.randint(0,1):
                    annim=self.annim3eau4
                    clockMax=7
                else :
                    annim=[pygame.image.load("data/animationTuiles/3Eau0_9.png")]
            
            if annim :
                clockAnnim=random.randint(0,len(annim)-1)
            else :
                clockAnnim=0
            return self.listeImg[type][rand], clockMax, annim, clockAnnim
        if  type==2 or type==7:
            rand = random.randint(0, 3)
            if type==7 and rand==1: 
                annim=self.annim7Barriere1
                clockMax=5
            if type==7 and rand==2: 
                annim=self.annim7Barriere2
                clockMax=5
            if type==7 and rand==3: 
                annim=self.annim7Barriere3
                clockMax=7
            if type==7 and rand==0: 
                annim=self.annim7Barriere0
                clockMax=5
            if type==2 and rand==1: #roche haut basique
                annim=self.annim2Roche1
                clockMax=5
            if type==2 and rand==2: #roche haut +1 pique
                annim=self.annim2Roche2
                clockMax=5
            if type==2 and rand==3: #roche haut basique
                annim=self.annim2Roche3
                clockMax=5
            if type==2 and rand==0: #roche eau
                annim=self.annim2Roche4
                clockMax=10
            
            if annim :
                clockAnnim=random.randint(0,len(annim)-1)
            else :
                clockAnnim=0
            
            return self.listeImg[type][rand], clockMax, annim, clockAnnim
        if type==4:
            rand = random.randint(0,8)
            if random.randint(0,1):
                return self.fondForet, 2, [self.listeImg[type][rand]], 1 
            return self.fondForet, 2, [pygame.transform.flip(self.listeImg[type][rand], 1,0)], 1 
        if type==10:
            rand = random.randint(0,7)
            if random.randint(0,1):
                return self.fondJungle, 2, [self.listeImg[type][rand]], 1 
            return self.fondJungle, 2, [pygame.transform.flip(self.listeImg[type][rand], 1,0)], 1 
        if type==5:
            rand = random.randint(0,6)
            
            if rand%2==0:
                rand=2
            elif rand == 1:
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
        if type==8:
            clockMax=None
            annim=[]
            clockAnnim = 0
            return self.listeImg[type][0], clockMax, annim, clockAnnim
        if type==9:
            clockMax=None
            annim=[]
            clockAnnim = 0
            rand = random.randint(0,5)
            if rand ==0 or rand==1:
                return self.listeImg[type][rand], clockMax, annim, clockAnnim
            if rand == 2 :
                annim=self.annim8violet0
                clockMax=10
                clockAnnim=random.randint(0,len(annim)-1)
            if rand ==3 :
                annim=self.annim8violet1
                clockMax=10
                clockAnnim=random.randint(0,len(annim)-1)
            if rand ==4 :
                annim=self.annim8violet3
                clockMax=10
                clockAnnim=random.randint(0,len(annim)-1)
            return self.listeImg[type][0], clockMax, annim, clockAnnim
        
        
        
        print("probleme")
        if type>=100:
            return self.listeImgUtilisateur[type], clockMax, annim, random.randint(0,len(annim)-1)
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
    def loadImgJoueur(self):
        tempIgmg = pygame.image.load("data/projectiles/joueur.png").convert_alpha()
        
        return tempIgmg
    def loadImgbossElec(self):
        tempIgmg = pygame.image.load("data/projectiles/bossElec.png").convert_alpha()
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
        if nom == "joueur":
            tempIgmg = self.imgJoueur
            if angle:
                tempIgmg = pygame.transform.rotate(tempIgmg, angle)
            return tempIgmg
        if nom == "bossElec":
            tempIgmg = self.imgBossElec
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
        print(nom)
        assert(False)
        #Pas d'image d'item trouvé


    def ImInfoBullItem(self, nom, chemin="data/batiments/infoBulle/info_"):
        img = pygame.image.load(chemin+nom+".png").convert_alpha()
        img = pygame.transform.scale(img, (411,257))
        return img
