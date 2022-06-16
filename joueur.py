import pygame
from PIL import Image
class Player(pygame.sprite.Sprite):
     def __init__(self):
          super().__init__()
          #affichage et information
          self .name ="Joueur"
          self.skin = pygame.image.load("data/personnage/joueur_1.png")
          self.skin = pygame.transform.scale(self.skin, (100, 150))

          #donnée du joueur
          self.health = 100
          self.velocity = 5
          self.armor = 0

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


    
     
