from dis import dis
from math import sqrt
import pygame
from projectile import Projectile 
class Tour(pygame.sprite.Sprite):

     def __init__(self, game, tuile, cooldown):
         super().__init__() 
         self.cooldown =cooldown
         self.addMob = True
         self.game =game
         self.tuile = tuile
         self.lastProjectile =0
         self.image = pygame.image.load("data/batiments/tour.png").convert_alpha()
         self.rect = self.image.get_rect()
         self.rect.x = tuile.rect.x
         self.rect.y = tuile.rect.y
         self.range = 300
         self.damage = 10
         self.attackSpeed = 10
         self.cooldown = 0
         
     def tirerFleche(self, cible):
         self.game.groupProjectile.add(Projectile(self.game, vitesse=20, posDepartX=self.tuile.posX, posDepartY=self.tuile.posY,cible=cible))



     def attack(self):
         
         mob_proche = []
         for mob in self.game.groupMob:
            xMob = mob.rect.x
            yMob = mob.rect.y
            distance = sqrt((self.rect.x - mob.skin.get_width()/2 - xMob)**2 + (self.rect.y -mob.skin.get_height()/2 - yMob)**2)
            print(distance)
            if distance < self.range:
                   mob_proche.append((mob, distance))
                   
                   
                   
         mob_proche.sort(key=lambda tup: tup[1]) #pour trier la liste selon la distance
         
         now = pygame.time.get_ticks()
         
         if len(mob_proche)>0 and now-self.lastProjectile>=self.cooldown:
            mobPlusProche = mob_proche[0][0]
            mobPlusProche.takeDamage(self.damage) #Il faudra ajouter un delai de tir
            self.game.groupProjectile.add(Projectile(self.game, "fleche", self.attackSpeed, self.rect.x, self.rect.y, mobPlusProche))
            self.lastProjectile = now
            self.cooldown=1000