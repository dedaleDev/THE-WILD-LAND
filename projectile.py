import math
import pygame
import random

from selection import majSelectionJoueur
class Projectile(pygame.sprite.Sprite):

     def __init__(self, game, nom, vitesse, posDepartX, posDepartY, cible):
          super().__init__()
          #affichage et information
          self.name = nom
          self.img = game.images.loadImgFleche()
          self.game = game
          self.velocity = vitesse
          self.cibleX = cible.rect.x
          self.cibleY = cible.rect.y

          self.rect = self.img.get_rect()
          self.rect.x = posDepartX
          self.rect.y = posDepartY
          
          self.estDetruit= False
        
     def moveProjectile(self):
        dx, dy = self.cibleX - self.rect.x, self.cibleY - self.rect.y
        dist = math.hypot(dx, dy)
        if dist!=0:
            dx, dy = dx / dist, dy / dist  # normalisation du vecteur
            # bouger en direction du vecteur
            self.rect.x += dx * self.velocity
            self.rect.y += dy * self.velocity
        else :
            self.estDetruit=True
            #detruire le projo

     """def moveProjectile(self):
        diffX = self.rect.x - self.cible.rect.x
        diffY = self.rect.y - self.cible.rect.y
        if diffY >= 0 and diffX>=0: #la cible est en haut a gauche
            reussi = self.projHaut()
            reussi = self.projGauche() or reussi
    
        elif diffY<=0 and diffX>=0: #la cible est en bas a gauche
            reussi = self.projBas()
            reussi  = self.projGauche() or reussi

        elif diffY<=0 and diffX<=0: #la cible est en bas a droite
            reussi = self.projBas()
            reussi = self.projDroite() or reussi

            
        elif diffY>=0 and diffX<=0: #la cible est en haut a droite
            reussi = self.projHaut()
            reussi = self.projDroite() or reussi"""
            
            
        
          
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
         
