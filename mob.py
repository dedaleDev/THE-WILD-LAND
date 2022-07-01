from tkinter import Scale
from PIL import Image
from numpy import true_divide
import pygame
import random
from selection import majSelectionJoueur
import generation
class Mob(pygame.sprite.Sprite):

     def __init__(self, game, nom, vie, vitesse):
          super().__init__()
          #affichage et information
          self.name = nom
          self.skin = self.loadSkin(nom)
          self.game = game
          self.bateau = False
          #self.skinBateau = self.loadSkin("bateau",(100, 150))

          self.health = vie
          self.velocity = vitesse
          self.armor = 0
          self.posX, self.posY = self.initPos()
          #self.posX, self.posY=3,3
          print(self.posY, self.posX)
          self.rect = self.skin.get_rect()
          self.rect.x = self.game.map[self.posY][self.posX].rect.x+40
          self.rect.y = self.game.map[self.posY][self.posX].rect.y+40



     def getFeet(self):
         return self.rect.x+30, self.rect.y+60
     
     def caseBloquanteAutour(self, posX, posY):
         return self.game.map[posY+1][posX].caseBloquante() and self.game.map[posY-1][posX].caseBloquante() and self.game.map[posY][posX-1].caseBloquante() and self.game.map[posY][posX+1].caseBloquante()

     def initPos(self):
         borneMaxX = min(generation.taille_matriceX-2, 9)
         borneMaxY = min(generation.taille_matriceY-2, 9)
         posX = random.randint(6,borneMaxX)
         posY = random.randint(6,borneMaxY)
         while self.game.map[posY][posX].caseBloquante() or self.caseBloquanteAutour(posX, posY):
             posX = random.randint(6,borneMaxX)
             posY = random.randint(6,borneMaxY)
         return posX, posY
          
     def loadSkin(self, nomSkin):
        if nomSkin== "monstre":
            scale = (704*0.13, 613*0.13)
        skin = pygame.image.load("data/personnages/"+nomSkin+".png")
        skin = pygame.transform.scale(skin, scale)
        return skin

     def moveMob(self, joueur):
        diffX = self.rect.x - joueur.rect.x
        diffY = self.rect.y - joueur.rect.y
        if diffY >= 0 and diffX>=0: #le joueur est en haut a gauche
            reussi = self.mobHaut()
            reussi = self.mobGauche() or reussi
            if not reussi:
                if random.randint(0,1):
                    self.mobBas()
                else:
                    self.mobDroite()
    
        elif diffY<=0 and diffX>=0: #le joueur est en bas a gauche
            reussi = self.mobBas()
            reussi  = self.mobGauche() or reussi
            if not reussi :
                if random.randint(0,1):
                    self.mobDroite()
                else :
                    self.mobHaut()

        elif diffY<=0 and diffX<=0: #le joueur est en bas a droite
            reussi = self.mobBas()
            reussi = self.mobDroite() or reussi
            if not reussi:
                if random.randint(0,1):
                    self.mobGauche()
                else :
                    self.mobHaut()
            
        elif diffY>=0 and diffX<=0: #le joueur est en haut a droite
            reussi = self.mobHaut()
            reussi = self.mobDroite() or reussi
            if not reussi:
                if random.randint(0,1):
                    self.mobGauche()
                else :
                    self.mobBas()
            
        
          
     def mobDroite(self):
        if self.deplacementAutorise("droite"):
            self.goRight()
            tuile = majSelectionJoueur(self.game, self.getFeet())
            self.setPos(tuile)
            return True
        return False
    
     def mobGauche(self):
        if self.deplacementAutorise("gauche"):
            self.goLeft()
            tuile = majSelectionJoueur(self.game, self.getFeet())
            self.setPos(tuile)
            return True
        return False
    
     def mobBas(self):
        if self.deplacementAutorise("bas"):
            self.goDown()
            tuile = majSelectionJoueur(self.game, self.getFeet())
            self.setPos(tuile)
            return True
        return False        
        
     def mobHaut(self):
        if self.deplacementAutorise("haut"):
            self.goUp()
            tuile = majSelectionJoueur(self.game, self.getFeet())
            self.setPos(tuile)
            return True
        return False        
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