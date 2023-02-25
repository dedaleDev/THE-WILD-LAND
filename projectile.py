import math
import pygame
class Projectile(pygame.sprite.Sprite):

     def __init__(self, game, nom, vitesse, degat, posDepartX, posDepartY, cible, origine=None, cibleCoordonnee=None, dureeMax=1500):
          super().__init__()
          #affichage et information
          
          self.game = game
          self.velocity = vitesse
          self.cibleCoordonnee=cibleCoordonnee
          if not self.cibleCoordonnee:
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
          self.dureeMax = dureeMax
          if not self.cibleCoordonnee:
            self.dx, self.dy = self.cibleX - self.rect.x, self.cibleY - self.rect.y
          else :
            self.dx, self.dy = self.cibleCoordonnee[0] - self.rect.x, self.cibleCoordonnee[1] - self.rect.y
          self.origine=origine
          
          
     def genererAngle(self):
        if not self.cibleCoordonnee:
          dx, dy =  self.cibleX-self.rect.x , self.rect.y-self.cibleY
          
          
        else:
          dx, dy = self.cibleCoordonnee[0]-self.rect.x , self.rect.y-self.cibleCoordonnee[1]
        angledegre= 180/math.pi*angle([1,0],[dx,dy])
        if dy<0: ##  calcul du determinant de la matrice associé aux 2 vecteurs colonne
          angledegre = 360-angledegre
        return angledegre


     def moveProjectile(self):
        
        dist = math.hypot(self.dx, self.dy) #Norme euclidienne
        if dist!=0:
            self.dx, self.dy = self.dx / dist, self.dy / dist  # normalisation du vecteur
            
            # bouger en direction du vecteur
            self.rect.x += round(self.dx * self.velocity)
            self.rect.y += round(self.dy * self.velocity)

        if not self.cibleCoordonnee:
          if self.rect.colliderect(self.cible.rect):
              self.cible.takeDamage(self.degat, self.game.moveX, self.game.moveY)
              if type(self.cible) == type(self.game.joueur) and not self.origine.name=="Boss":
                self.cible.dictioDegatMob[self.origine.name]+=self.origine.damageDistance
                
              self.kill()
              #detruire le projo
          elif self.game.tempsJeu()-self.lancement>self.dureeMax:
                self.kill()
        else:
          if self.rect.colliderect(self.game.joueur.rect):
              self.game.joueur.takeDamage(self.degat, self.game.moveX, self.game.moveY)
              self.kill()
          elif self.game.tempsJeu()-self.lancement>self.dureeMax:
            self.kill()
          


def produit(v1, v2):
      
      return sum((a*b) for a, b in zip(v1, v2))

def longueur(v):
  
  return math.sqrt(produit(v, v))

def angle(v1, v2):
  return math.acos(produit(v1, v2) / (longueur(v1) * longueur(v2)))