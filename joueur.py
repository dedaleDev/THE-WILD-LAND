from PIL import Image
import pygame
import random
import generation
class Player(pygame.sprite.Sprite):

     def __init__(self, game, nom):
          super().__init__()
          #affichage et information
          self.name = nom
          self.skin = self.loadSkin("joueur_1")
          self.game = game



          #donnée du joueur
          self.health = 100
          self.velocity = 5
          self.armor = 0
          self.posX, self.posY = self.initPos()
         

          #ressources du joueur
          self.wood = 200
          self.stone = 100
          self.food = 50
          self.water = 30000
          self.RessourcesTEXT =""
          self.RessourcesInfoModified= ""
          self.ressourcesIMG = self.loadRessourcesIMG()
          self.ancientRessources =(0,0)#type de la dernière ressource actualisé puis sa valeur

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
         posX = random.randint(1,generation.taille_matriceX-2)
         posY = random.randint(1,generation.taille_matriceY-2)
         print("posX=",posX,"posY=",posY)
         print("largeur=", len(self.game.map[0]),"hauteur =", len(self.game.map))
         while self.game.map[posY][posX].caseBloquante() or self.caseBloquanteAutour(posX, posY):
             posX = random.randint(1,generation.taille_matriceX-2)
             posY = random.randint(1,generation.taille_matriceY-2)
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

     def loadSkin(self, skin):
        self.skin = pygame.image.load("data/personnages/"+skin+".png")
        self.skin = pygame.transform.scale(self.skin, (100, 150))
        return(self.skin)
    
    
    
     def deplacementAutorise(self, direction):
         if direction=="droite":
            return not (self.game.map[self.posY][self.posX+1].tuileHaute() or self.game.map[self.posY][self.posX+1].estMer()) #on ne doit pas avoir mer ou montagne
         if direction=="gauche":
            return not (self.game.map[self.posY][self.posX-1].tuileHaute() or self.game.map[self.posY][self.posX-1].estMer())
         if direction=="haut":
             return not (self.game.map[self.posY-1][self.posX].tuileHaute() or self.game.map[self.posY-1][self.posX].estMer())
         if direction=="bas":
             return not (self.game.map[self.posY+1][self.posX].tuileHaute() or self.game.map[self.posY+1][self.posX].estMer())
         if direction=="diagHautDroit":
            return not (self.game.map[self.posY-1][self.posX+1].tuileHaute() or self.game.map[self.posY-1][self.posX+1].estMer())
         if direction=="diagHautGauche":
            return not (self.game.map[self.posY-1][self.posX-1].tuileHaute() or self.game.map[self.posY-1][self.posX-1].estMer())
         if direction=="diagBasGauche":
            return not (self.game.map[self.posY+1][self.posX-1].tuileHaute() or self.game.map[self.posY+1][self.posX-1].estMer())
         if direction=="diagBasDroit":
            return not (self.game.map[self.posY+1][self.posX+1].tuileHaute() or self.game.map[self.posY+1][self.posX+1].estMer())
        
     def goLeft(self):
        self.posX-=1
        if self.posX<1:
            self.posX=1
        
        
     def goRight(self):
        self.posX+=1
        if self.posX>len(self.game.map[0])-2:
            self.posX=len(self.game.map[0])-2
        
     def goUp(self):
         self.posY-=1
         if self.posY<1:
                self.posY=1
         
     def goDown(self):
         self.posY+=1
         if self.posY>len(self.game.map)-2:
            self.posY=len(self.game.map)-2

     def goDownLeft(self):
         self.goDown()
         self.goLeft()


     def goDownRight(self):
         self.goDown()
         self.goRight()
         
     def goUpRight(self):
        self.goRight()
        self.goUp()

     def goUpLeft(self):
         self.goUp()
         self.goLeft()
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
        if modif != False and type != None and modif<0:
            if self.ancientRessources[0]==type and self.ancientRessources[1]<=50:
                calcul = modif + self.ancientRessources[1]
                #print("Calculating", calcul, self.ancientRessources)
            else :
                calcul =modif
            self.ancientRessources=(type,calcul)
            listeRessourcesInfoModified[type]=smallfont.render(str(calcul), True, (255,255,255))
            
        self.RessourcesInfoModified=listeRessourcesInfoModified
        self.RessourcesTEXT= listeRessourcesTEXT
        
        return
    
    
    ####        CONSTRUCTION        ####
    
     def construireScierie(self, tuile):
        self.game.map[tuile.posY][tuile.posX].scierie = True
     
     def changerImageScierie(self, tuile):
          imgTemp = Image.open("data/batiments/scierie.png").convert('RGBA')

          self.game.map[tuile.posY][tuile.posX].imageO = imgTemp.resize((150, 150))