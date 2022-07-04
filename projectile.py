import math
import pygame
class Projectile(pygame.sprite.Sprite):

     def __init__(self, game, nom, vitesse, degat, posDepartX, posDepartY, cible):
          super().__init__()
          #affichage et information
          
          self.game = game
          self.velocity = vitesse
          self.cibleRect = cible.rect
          self.cibleX = cible.rect.x
          self.cibleY = cible.rect.y
          self.cible=cible
          self.img=game.images.loadImgProjectile(nom)
          
          self.rect = self.img.get_rect()
          self.degat = degat
          self.angle = self.genererAngle()
          self.img = game.images.loadImgProjectile(nom, self.angle)
          
          self.rect = self.img.get_rect()
          self.rect.x = posDepartX
          self.rect.y = posDepartY

     def genererAngle(self):
        dx, dy = self.cibleX - self.rect.x, self.cibleY - self.rect.y
        dist = math.hypot(dx, dy)
        print(dx,dy)
        return angle([dx,dy], [1,0])
        
        

     def moveProjectile(self):
        dx, dy = self.cibleX - self.rect.x, self.cibleY - self.rect.y
        dist = math.hypot(dx, dy)
        if dist!=0:
            dx, dy = dx / dist, dy / dist  # normalisation du vecteur
            # bouger en direction du vecteur
            self.rect.x += dx * self.velocity
            self.rect.y += dy * self.velocity
        if self.rect.colliderect(self.cible.rect):
            self.cible.takeDamage(self.degat)
            self.kill()
            #detruire le projo
        


def produit(v1, v2):
      return sum((a*b) for a, b in zip(v1, v2))

def longueur(v):
  return math.sqrt(produit(v, v))

def angle(v1, v2):
  return math.acos(produit(v1, v2) / (longueur(v1) * longueur(v2)))