import math
import pygame
import random

from selection import majSelectionJoueur
class Projectile(pygame.sprite.Sprite):

     def __init__(self, game, nom, vitesse, posDepartX, posDepartY, cible):
          super().__init__()
          #affichage et information
          self.img = game.images.loadImgProjectile(nom)
          self.game = game
          self.velocity = vitesse
          self.cibleX = cible.rect.x
          self.cibleY = cible.rect.y

          self.rect = self.img.get_rect()
          self.rect.x = posDepartX
          self.rect.y = posDepartY

        
     def moveProjectile(self):
        dx, dy = self.cibleX - self.rect.x, self.cibleY - self.rect.y
        dist = math.hypot(dx, dy)
        if dist!=0:
            dx, dy = dx / dist, dy / dist  # normalisation du vecteur
            # bouger en direction du vecteur
            self.rect.x += dx * self.velocity
            self.rect.y += dy * self.velocity
        else :
            self.kill()
            #detruire le projo
        
