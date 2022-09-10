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
          self.nom = nom
          self.rect = self.img.get_rect()
          self.rect.x = posDepartX
          self.rect.y = posDepartY
          self.degat = degat
          if self.nom =="mage" or self.nom=="yeti":
                self.angle=False
                
          else:
            self.angle = self.genererAngle()
          self.img = game.images.loadImgProjectile(nom, self.angle)
          self.rect = self.img.get_rect()
          self.rect.x = posDepartX
          self.rect.y = posDepartY
          self.lancement=self.game.tempsJeu()
          self.dureeMax = 1500
          self.dx, self.dy = self.cibleX - self.rect.x, self.cibleY - self.rect.y

     def genererAngle(self):
        dx, dy =  self.cibleX-self.rect.x , self.rect.y-self.cibleY 
        angledegre= 180/math.pi*angle([1,0],[dx,dy])
        if dy<0: ##  calcul du determinant de la matrice associé aux 2 vecteurs colonne
          angledegre = 360-angledegre
        return angledegre


     def moveProjectile(self):
        
        dist = math.hypot(self.dx, self.dy)
        if dist!=0:
            self.dx, self.dy = self.dx / dist, self.dy / dist  # normalisation du vecteur
            # bouger en direction du vecteur
            self.rect.x += self.dx * self.velocity
            self.rect.y += self.dy * self.velocity
        if self.rect.colliderect(self.cible.rect):
            self.cible.takeDamage(self.degat, self.game.moveX, self.game.moveY)
            
            self.kill()
            #detruire le projo
        elif self.game.tempsJeu()-self.lancement>self.dureeMax:
              self.kill()
        


def produit(v1, v2):
      
      return sum((a*b) for a, b in zip(v1, v2))

def longueur(v):
  
  return math.sqrt(produit(v, v))

def angle(v1, v2):
  return math.acos(produit(v1, v2) / (longueur(v1) * longueur(v2)))