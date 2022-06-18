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
          self.posX=1
          self.posY=1

          #ressources du joueur
          self.bois = 0
          self.pierre = 0
          self.nourriture = 0
          self.eau = 0


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

     def getBois(self):
           return self.bois
     def getPierre(self):
               return self.pierre
     def getNourriture(self):
               return self.nourriture
     def getEau(self):
               return self.eau

     def setHealth(self, health):
               self.health += health     
     def setVelocity(self, velocity):
               self.velocity += velocity
     def setArmor(self, armor):
               self.armor += armor
               
     def setBois(self, bois):
               self.bois += bois
     def setPierre(self, pierre):
               self.pierre += pierre
     def setNourriture(self, nourriture):
               self.nourriture += nourriture
     def setEau(self, eau):
               self.eau += eau
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