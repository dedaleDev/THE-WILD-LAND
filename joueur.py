import pygame
from PIL import Image
class Player(pygame.sprite.Sprite):

     def __init__(self, game):
          super().__init__()
          #affichage et information
          self.name ="Joueur"
          self.skin = self.loadSkin("joueur_1")
          self.game = game



          #donnée du joueur
          self.health = 100
          self.velocity = 5
          self.armor = 0
          self.posX=5
          self.posY=5

          #ressources du joueur
          self.wood = 200
          self.stone = 100
          self.food = 50
          self.water = 50
          self.RessourcesTEXT =""
          self.ressourcesIMG = self.loadRessourcesIMG()


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

     def setHealth(self, health):
               self.health += health     
     def setVelocity(self, velocity):
               self.velocity += velocity
     def setArmor(self, armor):
               self.armor += armor
               
     def setWood(self, wood):
               self.wood += wood
               self.compteurRessources()
     def setStone(self, stone):
               self.stone += stone
               self.compteurRessources()
     def setFood(self, food):
               self.food += food
               self.compteurRessources()
     def setWater(self, water):
               self.water += water
               self.compteurRessources()
     def loadSkin(self, skin):
        self.skin = pygame.image.load("data/personnages/"+skin+".png")
        self.skin = pygame.transform.scale(self.skin, (100, 150))
        return(self.skin)
    
    
    
     def deplacementAutorise(self, direction):
         if direction=="droite":
            return not (self.game.map[self.posY][self.posX+1].estMontagne() or self.game.map[self.posY][self.posX+1].estMer()) #on ne doit pas avoir mer ou montagne
         if direction=="gauche":
            return not (self.game.map[self.posY][self.posX-1].estMontagne() or self.game.map[self.posY][self.posX-1].estMer())
         if direction=="haut":
             return not (self.game.map[self.posY-1][self.posX].estMontagne() or self.game.map[self.posY-1][self.posX].estMer())
         if direction=="bas":
             return not (self.game.map[self.posY+1][self.posX].estMontagne() or self.game.map[self.posY+1][self.posX].estMer())
         if direction=="diagHautDroit":
            return not (self.game.map[self.posY-1][self.posX+1].estMontagne() or self.game.map[self.posY-1][self.posX+1].estMer())
         if direction=="diagHautGauche":
            return not (self.game.map[self.posY-1][self.posX-1].estMontagne() or self.game.map[self.posY-1][self.posX-1].estMer())
         if direction=="diagBasGauche":
            return not (self.game.map[self.posY+1][self.posX-1].estMontagne() or self.game.map[self.posY+1][self.posX-1].estMer())
         if direction=="diagBasDroit":
            return not (self.game.map[self.posY+1][self.posX+1].estMontagne() or self.game.map[self.posY+1][self.posX+1].estMer())
        
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

     def compteurRessources(self):
        smallfont = pygame.font.SysFont('Corbel', 50)  # definit la police utilisé
        listeRessources=[self.stone, self.food, self.water, self.wood]
        listeRessourcesTEXT=["", "","",""]
        for i in  range (len(listeRessourcesTEXT)) : 
            listeRessourcesTEXT[i]=smallfont.render(str(listeRessources[i]), True, (0,0,0))
        self.RessourcesTEXT= listeRessourcesTEXT
        return
