import pygame
from projectile import Projectile 
class Tours(pygame.sprite.Sprite):

     def __init__(self, game, tuile, cooldown, groupMob ):
         super().__init__() 
         self.cooldown =cooldown
         self.groupMob = groupMob
         self.addMob = True
         self.listProjectile=[]
         self.game =game
         self.tuileX  = self.game.map[tuile.posX]
         self.tuileY  = self.game.map[tuile.posY]

         def tirerFleche():
            if self.addMob == True :
               self.listProjectile.append(Projectile(self.game, vitesse=20, posDepartX=self.tuile, posDepartY=self.tuileY,cible=groupMob[-1]))
               self.addMob =False
            for i in range (len(groupMob)):
               game.fenetre.blit(self.listProjectile[i],(self.groupMob[i].rect.x,self.groupMob[i].rect.Y ))



