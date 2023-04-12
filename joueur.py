#from PIL import Image
from ctypes import pointer
from math import sqrt
import math
import pygame
from build import Build
from coffre import Coffre
import random
from projectile import Projectile
from selection import majSelectionJoueur
from tuile import Tuile

class Player(pygame.sprite.Sprite):

     def __init__(self, game, nom, vitesse, pointSpawn):
          super().__init__()
          #affichage et information
          self.name = nom
          self.skin = self.loadSkin(nom)
          self.image = self.skin
          self.game = game
          self.bateau = False
          self.skinBateau = self.loadSkin("bateau")
          self.mask = pygame.mask.from_surface(self.skin)
          
          
          self.annimationDroite = self.annimLoadDroite()
          self.annimationGauche = self.annimLoadGauche()
          self.annimationBas = self.annimLoadBas()
          self.annimationHaut = self.annimLoadHaut()
          self.indiceDroite = 0
          self.indiceBas = 0
          self.indiceHaut = 0
          self.clockAnnim = 0

          #donnée du joueur
          self.health = 100
          self.max_health=100
          self.velocity = vitesse
          self.armure = 0
          self.posX, self.posY = self.initPos(pointSpawn)
          self.rect = self.skin.get_rect()
          self.rect.x = self.game.map[self.posY][self.posX].rect.x+40
          self.rect.y = self.game.map[self.posY][self.posX].rect.y
          self.estMort=False
          self.ville=False
          self.tuile = 0 #tuile actuelle du joueur
          #ressources du joueur
          self.wood = 3500
          self.stone = 1000
          self.food = 5000
          self.water = 1000
          self.RessourcesTEXT =""
          self.RessourcesInfoModified= ""
          self.ressourcesIMG = self.loadRessourcesIMG()
          self.ancientRessources =(0,0)#type de la dernière ressource actualisé puis sa valeur
          self.score = 0
          self.nbScierie = 0
          self.nbMoulin = 0
          self.nbMine = 0
          self.nbPort = 0
          self.nbElevage=0
          self.nbChamps=0
          self.nbFrigo=0
          self.blit = False
          self.statuePierre = False
          self.statueBois = False
          self.statueEau = False
          self.statueFood = False
          self.imageArmure = None
          self.nomArmure = None
          
          self.listeTour=[]
          self.nomProj="joueur"
          self.cooldownDamage = 500
          self.lastDamage = 0
          self.cooldownShot = 1000
          self.indiceEcolo=0
          self.MaxEcolo=100
          
          self.nbAnnimauxTue = 0
          self.dictioDegatMob = {"golem_des_forets":0, "mage":0, "dragon":0, "yeti":0, "kraken":0, "oursin":0}
          #deplacement
          
          self.marteau="marteau0"
          self.lastProjectile = 0
          self.speedProjectile = 10
          self.damageDistance = 4
          self.range = 600
          self.attendre = 0
          
          self.tempsBateau=0
          self.maxTempBateau=90
          
          self.imgBateau=pygame.image.load("data/personnages/joueur/iconBateau.png").convert_alpha()
          
    
    
     def updateBateau(self):
         if self.getTuile().port:
             self.tempsBateau+=1
             if self.tempsBateau>=self.maxTempBateau:
                 self.bateau = not self.bateau
                 self.tempsBateau=-100
         else:
             self.tempsBateau=-10
             
         if self.tempsBateau>=0:
             bar_position = [self.rect.x, self.rect.y-10, self.tempsBateau, 5]
             back_bar_position = [self.rect.x, self.rect.y-10, 100, 5]

             pygame.draw.rect(self.game.fenetre, (128,128,128), back_bar_position)
             pygame.draw.rect(self.game.fenetre, (0,0,204), bar_position)
             self.game.fenetre.blit(self.imgBateau, (self.rect.x-60, self.rect.y-30))
             
                 
     def getTuile(self):
         return self.game.map[self.posY][self.posX]
    
     def changeAnnimDroite(self):

         self.clockAnnim+=1
         if self.clockAnnim==5:
             
            self.indiceDroite+=1
            if self.indiceDroite >= len(self.annimationDroite):
                self.indiceDroite=0
            self.clockAnnim=0
            self.skin = self.annimationDroite[self.indiceDroite]
            
            
     def changeAnnimHaut(self):

         self.clockAnnim+=1
         if self.clockAnnim==5:
             
            self.indiceHaut+=1
            if self.indiceHaut >= len(self.annimationHaut):
                self.indiceHaut=0
            self.clockAnnim=0
            self.skin = self.annimationHaut[self.indiceHaut] 
            
     def changeAnnimGauche(self):
         self.clockAnnim+=1
         if self.clockAnnim==5:
            self.indiceDroite+=1
            if self.indiceDroite >= len(self.annimationDroite):
                self.indiceDroite=0
            self.clockAnnim=0
            self.skin = self.annimationGauche[self.indiceDroite] 

     def changeAnnimBas(self):
         self.clockAnnim+=1
         if self.clockAnnim==5:
            self.indiceBas+=1
            if self.indiceBas >= len(self.annimationBas):
                self.indiceBas=0
            self.clockAnnim=0
            self.skin = self.annimationBas[self.indiceBas]


     def annimLoadDroite(self):
         listeAnnimDroite = []
         for i in range(11):
             im = pygame.image.load("data/personnages/joueur/Joueur"+str(i)+".png").convert_alpha()
             listeAnnimDroite.append(pygame.transform.scale(im, (48,97))) 
         return listeAnnimDroite
    
     def annimLoadBas(self):
         listeAnnimBas = []
         for i in range(1, 12):
             im = pygame.image.load("data/personnages/joueur/JoueurAvant_"+str(i)+".png").convert_alpha()
             listeAnnimBas.append(pygame.transform.scale(im, (48,97)))
         return listeAnnimBas
    
     def annimLoadHaut(self):
         listeAnnimHaut = []
         for i in range(1, 11):
             im = pygame.image.load("data/personnages/joueur/JoueurHaut_"+str(i)+".png").convert_alpha()
             listeAnnimHaut.append(pygame.transform.scale(im, (48,97)))
         return listeAnnimHaut
    
     def annimLoadGauche(self):
         listeAnnimGauche = []
         for i in range(11):
             im = pygame.image.load("data/personnages/joueur/Joueur"+str(i)+".png").convert_alpha()
             listeAnnimGauche.append(pygame.transform.flip(pygame.transform.scale(im, (48,97)),True, False))

         return listeAnnimGauche
    
     def getFeet(self):
         return self.rect.x+25, self.rect.y+80

     def takeDamage(self, entier, moveX=0, moveY=0):
        resistance = 100-self.armure
        #print("de base",entier)
        entier=int(resistance/100*entier)
        #print("prit", entier)
        if self.health >=0 :
            self.health-=entier
            self.update_health_bar()
            self.game.annimDegat=0
        else :
            self.estMort=True


     def genererCoffre(self):
         borneMin = 1#5 #Distance minimal entre le joueur et le spawn du coffre
         borneMax = 5#10 #distance max ""   ""
         
         tuilesDispo = []
         
         for ligne in self.game.map:
             for tuile in ligne :
                 if tuile.type!=7 and tuile.type!=2:
                     if abs(self.posX-tuile.posX) >= borneMin and abs(self.posX-tuile.posX)<=borneMax :
                         tuilesDispo.append(tuile)
                         
         tuileCoffre = random.choice(tuilesDispo)
         self.game.groupCoffre.add(Coffre(self.game, tuileCoffre, random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100)))
         pygame.mixer.Sound.play(self.game.son.coffre)
                     

     def getSkin(self):
         return self.skin
     def getName(self):
         return self.name
     def getHealth(self):
         return self.health   
     def getVelocity(self):
           return self.velocity
     def getArmor(self): 
               return self.armor

     def getWood(self):
           return self.wood
     def getStone(self):
               return self.stone
     def getFood(self):
               return self.food
     def getWater(self):
               return self.water
    
     def setRessource(self, Wood, Stone, Food, Water):
         return self.setFood(Food) and self.setWood(Wood) and self.setStone(Stone) and self.setWater(Water)
    
     
     
     def initPos(self, pointSpawn):
         if pointSpawn : 
             a =random.choice(pointSpawn)
             return a
         borneMaxX = min(self.game.taille_matriceX-2, 9)
         borneMaxY = min(self.game.taille_matriceY-2, 9)
         posX = random.randint(0,borneMaxX)
         posY = random.randint(0,borneMaxY)
         while self.game.map[posY][posX].caseBloquante() or self.caseBloquanteAutour(posX, posY):
             posX = random.randint(0,borneMaxX)
             posY = random.randint(0,borneMaxY)
         return posX, posY

     def caseBloquanteAutour(self, posX, posY):
         return self.game.map[posY+1][posX].caseBloquante() and self.game.map[posY-1][posX].caseBloquante() and self.game.map[posY][posX-1].caseBloquante() and self.game.map[posY][posX+1].caseBloquante()


     def resetRessourcesModified(self):
        self.RessourcesInfoModified=[False,False,False,False]

     def setHealth(self, health):
               self.health += health     
     def setVelocity(self, velocity):
               self.velocity += velocity
     def setArmor(self, armor):
               self.armor += armor
               
     def setFood(self, food):
        if (self.food + food>=0) :
            self.food += food
            self.compteurRessources(modif=food, type=1)
            return True
        return False
    
     def setStone(self, stone):
        if (self.stone + stone>=0) :
            self.stone += stone
            self.compteurRessources(modif=stone, type=2)
            return True
        return False
            
     def setWater(self, water):
        if (self.water + water>=0) :
            self.water += water
            self.compteurRessources(modif=water, type=3)
            return True
        return False
     def setWood(self, wood):
        if (self.wood + wood>=0) :
            self.wood += wood
            self.compteurRessources(modif=wood, type=4)
            return True
        return False

     def loadSkin(self, nomSkin):
        if nomSkin=="joueur1" or nomSkin=="joueur1-2":
            scale = (48, 97) #48, 97
        elif nomSkin=="bateau":
            scale= (512*0.2, 512*0.2)
        else:
            scale = (48, 97)
        skin = pygame.image.load("data/personnages/joueur/"+nomSkin+".png").convert_alpha()
        skin = pygame.transform.scale(skin, scale)
        return skin
    
    
    
     def deplacementAutorise(self, direction):
         if direction=="bas":
             tuile = majSelectionJoueur(self.game, 0, self.velocity)
         if direction=="droite":
            tuile = majSelectionJoueur(self.game, self.velocity, 0)
            
         if direction=="gauche":
            tuile = majSelectionJoueur(self.game, -self.velocity, 0)
            
         if direction=="haut":
            tuile = majSelectionJoueur(self.game, 0, -self.velocity)
            
         
         if tuile:
            if self.tuileInterdit(tuile): #gestion de deplacement entre 2 cases
                if direction=="bas":
                    tuile = majSelectionJoueur(self.game, 0, self.velocity+30)
                    
                if direction=="droite":
                    tuile = majSelectionJoueur(self.game, self.velocity+70, 0)
            
                if direction=="gauche":
                    tuile = majSelectionJoueur(self.game, -self.velocity-70, 0)
                    
                if direction=="haut":
                    tuile = majSelectionJoueur(self.game, 0, -self.velocity-30)
                    
            if tuile:
                return not self.tuileInterdit(tuile)
            else:
                print("erreur dans fonction joueur.deplacement autorisé")
                return True
         else:
             print("erreur dans fonction joueur.deplacement autorisé")
             return True
         
         
     def tuileInterdit(self, tuile):
         return tuile.tuileHaute() or (tuile.estMer() and tuile.pasPort() and not self.bateau) or (not tuile.estMer() and tuile.pasPort() and self.bateau)
         


     def setPos(self, tuile):
        self.posX, self.posY = tuile.posX, tuile.posY

     def goLeft(self):
            self.changeAnnimGauche()
            self.rect.x-=self.velocity
     
     
        
        
     def goRight(self):
        self.changeAnnimDroite()
        self.rect.x+=self.velocity
        
     def goUp(self, annim=True):
         if annim:
            self.changeAnnimHaut()
         self.rect.y-=self.velocity

     def goDown(self, annim=True):
         if annim:
            self.changeAnnimBas()
         self.rect.y+=self.velocity

     def majBateau(self):
         if self.game.map[self.posY][self.posX].type!=3:
             self.bateau=False
         
         
     def loadRessourcesIMG(self):
       
        listeRessourcesSources = ["data/ressources/r_food.png", "data/ressources/r_stone.png", "data/ressources/r_water.png", "data/ressources/r_wood.png"]
        for i in  range (len(listeRessourcesSources)) : 
            listeRessourcesSources[i]= pygame.image.load(listeRessourcesSources[i]).convert_alpha()
            listeRessourcesSources[i]= pygame.transform.scale(listeRessourcesSources[i],(self.game.infoObject[0]*0.08,self.game.infoObject[1]*0.06))
        self.compteurRessources()
        return listeRessourcesSources

     def compteurRessources(self, modif = False,type = None):
        #1 food 
        #2 stone
        #3 water
        #4 wood
        smallfont =pygame.font.SysFont("Corbel", round(math.sqrt(self.game.infoObject[0]**2 + self.game.infoObject[1]**2)*0.02))  # definit la police utilisé
        listeRessources=[self.food, self.stone, self.water, self.wood]
        listeRessourcesTEXT=["", "","",""]
        listeRessourcesInfoModified =  [False,False,False,False]
        for i in  range (len(listeRessourcesTEXT)) : 
            listeRessourcesTEXT[i]=smallfont.render(str(listeRessources[i]), True, (0,0,0))
        if not modif and type and modif<0:
            if self.ancientRessources[0]==type and self.ancientRessources[1]<=50:
                calcul = modif + self.ancientRessources[1]
            else :
                calcul = modif
            self.ancientRessources=(type,calcul)
            listeRessourcesInfoModified[type]=smallfont.render(str(calcul), True, (255,255,255))
            
        self.RessourcesInfoModified=listeRessourcesInfoModified
        self.RessourcesTEXT= listeRessourcesTEXT
        
        return
    
    
    ####        CONSTRUCTION        ####
    
     def cout(self, item):
        return self.wood - item.coutWood >=0 and self.food - item.coutFood >=0 and self.stone - item.coutStone >=0 and self.water - item.coutWater >=0
    
    
     def majCout(self, item):
        if self.wood - item.coutWood >=0 and self.food - item.coutFood >=0 and self.stone - item.coutStone >=0 and self.water - item.coutWater >=0:
            self.setFood(-item.coutFood)
            self.setWood(-item.coutWood) 
            self.setStone(-item.coutStone) 
            self.setWater(-item.coutWater)
            return True
        
        return False
              
     def lunchProjectile(self):
         if self.attendre>60:
            mob_proche = []
            
            for mob in self.game.groupMob:
                if not mob.annimal:
                    xMob = mob.rect.x
                    yMob = mob.rect.y-10
                    distance = sqrt((self.rect.x - mob.skin.get_width()/2 - xMob)**2 + (self.rect.y -mob.skin.get_height()/2 - yMob)**2)
                    if distance < self.range :
                        mob_proche.append((mob, distance))
            if self.game.theBoss:
                mob = self.game.theBoss
                mob_proche.append((mob, 1))
            mob_proche.sort(key=lambda tup: tup[1]) #pour trier la liste selon la distance
            
            now = self.game.tempsJeu()
            
            if len(mob_proche)>0 and now-self.lastProjectile>=self.cooldownShot:
                mobPlusProche = mob_proche[0][0]
                self.game.groupProjectile.add(Projectile(self.game, self.nomProj, self.speedProjectile, self.damageDistance, self.rect.x+30, self.rect.y+30, mobPlusProche, self))
                self.lastProjectile = now
            self.attendre=0
    
     
     def construireBatiment(self, tuile, item):
        dictio = {"elevage":1, "champs":0, "moulin":1, "scierie":1, "port":1, "mine":2, "pieux":0, "trou":1,"forge":3,
                  "statueEau":3, "sableMouvant":3, "tour":4, "mortier":4, "ventilo":5, "frigo":4,"statueBois":3,
                  "statueFood":3, "statuePierre":3, "ville":6,"armure1":0,"armure2":0,"armure3":0,"armure4":0, "marteau1":0, "marteau2":0}
        if not self.majCout(item):
            return False
        
        self.game.groupBuild.add(Build(self.game, item.nom, tuile, dictio[item.nom]))
        return True
    
     def detruireBatimentRessource(self, tuile):
         if tuile.champs:
            tuile.champs=False
            self.nbChamps-=1
         if tuile.elevage:
            tuile.elevage=False
            self.nbElevage-=1
         if tuile.mine:
            tuile.mine=False
            self.nbMine-=1
         if tuile.moulin:   
            tuile.moulin=False
            self.nbMoulin-=1
         if tuile.scierie:
             tuile.scierie=False
             self.nbScierie-=1
         if tuile.port:
            tuile.port=False
            self.nbPort-=1
         if tuile.pieux:
             tuile.pieux=False
         tuile.image, tuile.clockAnnimMax, tuile.annimation, tuile.indiceAnnim = self.game.images.returnImg(tuile.type)
         tuile.aEteModifie=True

         return tuile

     def chargerImPort(self, tuile, posJoueurX, posJoueurY,supX=0, supY=0): #sup = variable pour simuler un decalage joueur
         ecartX = tuile.posX-posJoueurX-supX
         ecartY = tuile.posY-posJoueurY-supY
         if ecartX==0 and ecartY == 1:
             imgTemp2 = pygame.image.load("data/batiments/port/port2.png").convert_alpha()
         if ecartX==-1 and ecartY == 0:
             imgTemp2 = pygame.image.load("data/batiments/port/port3.png").convert_alpha()
         if ecartX==0 and ecartY == -1:
             imgTemp2 = pygame.image.load("data/batiments/port/port1.png").convert_alpha()
         if ecartX == 1 and ecartY == 0:
             imgTemp2 = pygame.image.load("data/batiments/port/port0.png").convert_alpha()
         if ecartX == 1 and ecartY == -1:
             imgTemp2 = pygame.image.load("data/batiments/port/port"+str(random.randint(0,1))+".png").convert_alpha()
         if ecartX == -1 and ecartY == 1:
             imgTemp2 = pygame.image.load("data/batiments/port/port"+str(random.randint(2,3))+".png").convert_alpha()
         if ecartX == 1 and ecartY == 1:
             imgTemp2 = pygame.image.load("data/batiments/port/port"+str(random.choice([0,2]))+".png").convert_alpha()
         if ecartX == -1 and ecartY == -1:
             imgTemp2 = pygame.image.load("data/batiments/port/port"+str(random.choice([1,3]))+".png").convert_alpha()
         if ecartX == 0 and ecartY == 0:
             listeEcart=[]
             for i in range(-1,2):
                 for j in range(-1,2):
                     if (i!=0 or j!=0) and not self.game.map[tuile.posY+i][tuile.posX+j].caseBloquante():
                        listeEcart.append((i,j))
             for i,j in listeEcart:
                 if i==0 or j==0:
                    return self.chargerImPort(tuile, posJoueurX, posJoueurY, supX=j, supY=i)
             i,j = listeEcart[0]
             return self.chargerImPort(tuile, posJoueurX, posJoueurY, supX=j, supY=i)
         return imgTemp2

     def changerImageBatiment(self, tuile:Tuile, nom, posJoueurX=-1, posJoueurY=-1):
          if nom=="port":
              imgTemp = self.chargerImPort(tuile, posJoueurX, posJoueurY)
              imgTemp = pygame.transform.scale(imgTemp,(246, 144))
              tuile.surAnnimListe=[imgTemp]
              
              return
              
          else:
              if nom!="moulin" and nom!="elevage" and nom!="mortier" and nom[0:-1]!="armure" and nom[0:-1]!="marteau":
                imgTemp = pygame.image.load("data/batiments/"+nom+".png").convert_alpha()
          if nom != "ville" and nom!="moulin"and nom!="elevage" and nom!="mortier" and nom[0:-1]!="armure" and nom[0:-1]!="marteau" and nom!="forge" and nom!="scierie":
            tuile.image = pygame.transform.scale(imgTemp,(246, 144))
          if nom=="scierie":
              if tuile.type==10:
                  tuile.annimation=[pygame.image.load("data/batiments/"+nom+"2.png").convert_alpha()]
              else:
                tuile.annimation=[pygame.image.load("data/batiments/"+nom+".png").convert_alpha()]
          tuile.aEteModifie=True

     def ajouterRessources(self):
         self.setWood(5*self.nbScierie)
         self.setStone(4*self.nbMine)
         #self.setWater(1*self.nbPuit)
         self.setWater(3*self.nbMoulin)
         self.setFood(5*self.nbElevage + 1*self.nbChamps)
         self.indiceEcolo-=self.nbFrigo*0.5
         if self.indiceEcolo<0:
             self.indiceEcolo=0
             
     def update_health_bar(self):
        #def la couleur
        

        if self.health >=80 : 
            bar_color = (3, 166, 160)
        elif self.health >=50 : 
            bar_color = (255, 165, 0)
        elif self.health >=25 : 
            bar_color = (255, 69, 0)
        elif self.health >=0 : 
            bar_color = (255, 0, 0)
        else : 
            bar_color = (255, 0, 0)
        back_bar_color = (60,63,60)
        bar_position = [60, 20, self.health*3, 40]
        back_bar_position = [60, 20, self.max_health*3, 40]
        #dessiner la barre de vie
        
        pygame.draw.rect(self.game.fenetre, back_bar_color, back_bar_position)
        pygame.draw.rect(self.game.fenetre, bar_color, bar_position)
        
     def update_ecolo_bar(self):
        
        if self.indiceEcolo >=80 : 
            bar_color = (255, 0, 0)
        elif self.indiceEcolo >=50 : 
            bar_color = (255, 69, 0)
        elif self.indiceEcolo >=25 : 
            bar_color = (255, 165, 0)
        else :
            bar_color = (111, 210, 46)

        back_bar_color = (60,63,60)
        bar_position = [20, 170+self.indiceEcolo*2, 30, self.MaxEcolo*2-self.indiceEcolo*2]
        back_bar_position = [20, 170, 30, self.MaxEcolo*2]
        #dessiner la barre de vie
        
        pygame.draw.rect(self.game.fenetre, back_bar_color, back_bar_position)
        pygame.draw.rect(self.game.fenetre, bar_color, bar_position)