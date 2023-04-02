from math import sqrt
import pygame
from projectile import Projectile 
class Tour(pygame.sprite.Sprite):

     def __init__(self, game, tuile, cooldown, nom, damage, range):
         super().__init__() 
         self.cooldown =cooldown
         self.nom = nom
         self.addMob = True
         self.game =game
         self.tuile = tuile
         self.lastProjectile =0
         self.image = pygame.image.load("data/batiments/"+self.nom+".png").convert_alpha()
         self.rect = self.image.get_rect()
         self.rect.x = tuile.rect.x+45
         self.rect.y = tuile.rect.y+20
         self.range = range
         self.damage = damage
         self.speedProjectile = 10
         self.cooldown = 0
         
     


     def attack(self):
         mob_proche = []
         for mob in self.game.groupMob:
            if not mob.annimal:
                xMob = mob.rect.x
                yMob = mob.rect.y-10
                distance = sqrt((self.rect.x - mob.skin.get_width()/2 - xMob)**2 + (self.rect.y -mob.skin.get_height()/2 - yMob)**2)

                if distance < self.range :
                    if self.nom=="mortier":
                        if mob.aerien:
                            mob_proche.append((mob, distance))
                    else :
                        mob_proche.append((mob, distance))
                   
         mob_proche.sort(key=lambda tup: tup[1]) #pour trier la liste selon la distance
         
         now = self.game.tempsJeu()
         
         if len(mob_proche)>0 and now-self.lastProjectile>=self.cooldown:
            mobPlusProche = mob_proche[0][0]
            
            
            self.game.groupProjectile.add(Projectile(self.game, self.nom, self.speedProjectile, self.damage, self.rect.x+30, self.rect.y, mobPlusProche))
            pygame.mixer.Sound.play(self.game.son.fleche)
            self.lastProjectile = now
            self.cooldown=1000
            

