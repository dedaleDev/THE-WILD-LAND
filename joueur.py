from PIL import Image
import pygame
import random
from selection import majSelectionJoueur
import generation
class Player(pygame.sprite.Sprite):

     def __init__(self, game, nom):
          super().__init__()
          #affichage et information
          self.name = nom
          self.skin = self.loadSkin(nom, (472*0.13, 978*0.13))
          self.game = game
          self.bateau = False
          self.skinBateau = self.loadSkin("bateau",(100, 150))



          #donnée du joueur
          self.health = 100
          self.velocity = 5
          self.armor = 0
          self.posX, self.posY = self.initPos()
          self.rect = self.skin.get_rect()
          self.rect.x = self.game.map[self.posY][self.posX].rect.x+50
          self.rect.y = self.game.map[self.posY][self.posX].rect.y - 20


          #ressources du joueur
          self.wood = 200
          self.stone = 100
          self.food = 50
          self.water = 30000
          self.RessourcesTEXT =""
          self.RessourcesInfoModified= ""
          self.ressourcesIMG = self.loadRessourcesIMG()
          self.ancientRessources =(0,0)#type de la dernière ressource actualisé puis sa valeur
          
          self.nbScierie = 0
          self.nbMoulin = 0
          self.nbElevage=0
          self.nbChamps=0
          self.nbMine = 0
          self.nbPort = 0
        
          self.nombreDecalageRestantX = 0

     def getFeet(self):
         return self.rect.x+35, self.rect.y+120


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



     def initPos(self):
         borneMaxX = min(generation.taille_matriceX-2, 9)
         borneMaxY = min(generation.taille_matriceY-2, 9)
         posX = random.randint(6,borneMaxX)
         posY = random.randint(6,borneMaxY)
         while self.game.map[posY][posX].caseBloquante() or self.caseBloquanteAutour(posX, posY):
             posX = random.randint(6,borneMaxX)
             posY = random.randint(6,borneMaxY)
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
        if (self.food -food>=0) :
            self.food += food
            self.compteurRessources(modif=food, type=1)
     def setStone(self, stone):
        if (self.stone -stone>=0) :
            self.stone += stone
            self.compteurRessources(modif=stone, type=2)   
     def setWater(self, water):
        if (self.water -water>=0) :
            self.water += water
            self.compteurRessources(modif=water, type=3)
     def setWood(self, wood):
        if (self.wood -wood>=0) :
            self.wood += wood
            self.compteurRessources(modif=wood, type=4)

     def loadSkin(self, nomSkin, scale):
        skin = pygame.image.load("data/personnages/"+nomSkin+".png")
        skin = pygame.transform.scale(skin, scale)
        return skin
    
    
    
     def deplacementAutorise(self, direction):
         if direction=="droite":
            tuile = majSelectionJoueur(self.game, (self.getFeet()[0]+self.velocity, self.getFeet()[1]))
            
         if direction=="gauche":
            tuile = majSelectionJoueur(self.game, (self.getFeet()[0]-self.velocity, self.getFeet()[1]))
            
         if direction=="haut":
            tuile = majSelectionJoueur(self.game, (self.getFeet()[0], self.getFeet()[1]-self.velocity))
            
         if direction=="bas":
             tuile = majSelectionJoueur(self.game, (self.getFeet()[0], self.getFeet()[1]+self.velocity))
         if tuile:
            if self.tuileInterdit(tuile):
                
                if direction=="droite":
                    tuile = majSelectionJoueur(self.game, (self.getFeet()[0]+self.velocity+10, self.getFeet()[1]))
            
                if direction=="gauche":
                    tuile = majSelectionJoueur(self.game, (self.getFeet()[0]-self.velocity-10, self.getFeet()[1]))
                    
                if direction=="haut":
                    tuile = majSelectionJoueur(self.game, (self.getFeet()[0], self.getFeet()[1]-self.velocity-10))
                    
                if direction=="bas":
                    tuile = majSelectionJoueur(self.game, (self.getFeet()[0], self.getFeet()[1]+self.velocity+10))
            return not self.tuileInterdit(tuile)
        
         else:
             print("erreur dans fonction joueur.deplacement autorisé")
             return False
         
         
     def tuileInterdit(self, tuile):
         return tuile.tuileHaute() or (tuile.estMer() and tuile.pasPort() and not self.bateau) or (not tuile.estMer() and tuile.pasPort() and self.bateau)
         


     def setPos(self, tuile):
        self.posX, self.posY = tuile.posX, tuile.posY

     def goLeft(self):
            self.rect.x-=self.velocity
     
     
        
        
     def goRight(self):
        self.rect.x+=self.velocity
        
     def goUp(self):
         self.rect.y-=self.velocity
         
     def goDown(self):
         self.rect.y+=self.velocity

     def majBateau(self):
         if self.game.map[self.posY][self.posX].type!=3:
             self.bateau=False
         
         
     def loadRessourcesIMG(self):
       
        listeRessourcesSources = ["data/ressources/r_food.png", "data/ressources/r_stone.png", "data/ressources/r_water.png", "data/ressources/r_wood.png"]
        for i in  range (len(listeRessourcesSources)) : 
            listeRessourcesSources[i]= pygame.image.load(listeRessourcesSources[i]).convert_alpha()
            listeRessourcesSources[i]= pygame.transform.scale(listeRessourcesSources[i],( 170,70))
        self.compteurRessources()
        return listeRessourcesSources

     def compteurRessources(self, modif = False,type = None):
        #1 food 
        #2 stone
        #3 water
        #4 wood
        smallfont = pygame.font.SysFont('Corbel', 50)  # definit la police utilisé
        listeRessources=[self.food, self.stone, self.water, self.wood]
        listeRessourcesTEXT=["", "","",""]
        listeRessourcesInfoModified =  [False,False,False,False]
        for i in  range (len(listeRessourcesTEXT)) : 
            listeRessourcesTEXT[i]=smallfont.render(str(listeRessources[i]), True, (0,0,0))
        if not modif and type and modif<0:
            if self.ancientRessources[0]==type and self.ancientRessources[1]<=50:
                calcul = modif + self.ancientRessources[1]
                #print("Calculating", calcul, self.ancientRessources)
            else :
                calcul = modif
            self.ancientRessources=(type,calcul)
            listeRessourcesInfoModified[type]=smallfont.render(str(calcul), True, (255,255,255))
            
        self.RessourcesInfoModified=listeRessourcesInfoModified
        self.RessourcesTEXT= listeRessourcesTEXT
        
        return
    
    
    ####        CONSTRUCTION        ####
    
     def construireBatiment(self, tuile, nom):
        if nom == "scierie":
            self.game.map[tuile.posY][tuile.posX].scierie = True
            self.nbScierie+=1
        elif nom == "moulin":
            self.game.map[tuile.posY][tuile.posX].moulin = True
            self.nbMoulin+=1
        elif nom == "puit":
            self.game.map[tuile.posY][tuile.posX].puit = True
            self.nbPuit+=1
        elif nom == "mine":
            self.game.map[tuile.posY][tuile.posX].mine = True
            self.nbMine+=1
        elif nom == "port":
            self.game.map[tuile.posY][tuile.posX].port = True
            self.nbPort+=1
        self.changerImageBatiment(tuile, nom)
    
     
     def chargerImPort(self, tuile):
         ecartX = tuile.posX-self.posX
         ecartY = tuile.posY-self.posY
         print(ecartX, ecartY)
         if ecartX==0 and ecartY == 1:
             imgTemp = Image.open("data/batiments/port/port2.png").convert('RGBA')
         if ecartX==-1 and ecartY == 0:
             imgTemp = Image.open("data/batiments/port/port3.png").convert('RGBA')
         if ecartX==0 and ecartY == -1:
             imgTemp = Image.open("data/batiments/port/port1.png").convert('RGBA')
         if ecartX == 1 and ecartY == 0:
             imgTemp = Image.open("data/batiments/port/port0.png").convert('RGBA')
         if ecartX == 1 and ecartY == -1:
             imgTemp = Image.open("data/batiments/port/port"+str(random.randint(0,1))+".png").convert('RGBA')
         if ecartX == -1 and ecartY == 1:
             imgTemp = Image.open("data/batiments/port/port"+str(random.randint(2,3))+".png").convert('RGBA')
         if ecartX == 1 and ecartY == 1:
             imgTemp = Image.open("data/batiments/port/port"+str(random.choice([0,2]))+".png").convert('RGBA')
         if ecartX == -1 and ecartY == -1:
             imgTemp = Image.open("data/batiments/port/port"+str(random.choice([1,3]))+".png").convert('RGBA')

         return imgTemp
     
     def changerImageBatiment(self, tuile, nom):
          if nom=="port":
              imgTemp = self.chargerImPort(tuile)
             
          else:
              imgTemp = Image.open("data/batiments/"+nom+".png").convert('RGBA')
          tuile.imageO = imgTemp.resize((150, 150))
          tuile.aEteModifie=True
          
     
          
     def ajouterRessources(self):

         self.setWood(1*self.nbScierie)
         self.setStone(1*self.nbMine)
         self.setWater(1*self.nbMoulin)
         self.setFood(2*self.nbElevage+ 1*self.nbChamps)

