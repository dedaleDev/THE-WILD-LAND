from math import sqrt
import math
import random
import pygame
from game import Game
from projectile import Projectile
class Boss(pygame.sprite.Sprite):
    def __init__(self, game:Game, health):
        super().__init__()
        self.health = health
        self.game = game
        self.image = self.game.images.boss
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = game.mapBoss[2][3].rect.x, game.mapBoss[2][3].rect.y
        self.cooldown=0
        self.range = 10000
        self.lastProjectile=0
        self.name="Boss"
        self.recharge = None
        
        self.velocity=10
        #self.attaqueTourniquet=None
        self.rush=False
        self.directionRush=None
        
        self.dx, self.dy = 0,0
        
    def moveBoss(self):
        if self.rush:
            dist = math.hypot(self.dx, self.dy) #Norme euclidienne
            if dist!=0:
                self.dx, self.dy = self.dx / dist, self.dy / dist  # normalisation du vecteur
            
                # bouger en direction du vecteur
                self.rect.x += round(self.dx * self.velocity)
                self.rect.y += round(self.dy * self.velocity)
            if (abs(self.directionRush[0]-self.rect.x)+abs(self.directionRush[1]-self.rect.y)<10):
                self.rush=False
        else:
            if not random.randint(0,100):
                
                tuileY=random.randint(1, (len(self.game.mapBoss))-2) #trouver une tuile random sur la map
                tuileX=random.randint(1, (len(self.game.mapBoss[0]))-2)
                tuile=self.game.map[tuileY][tuileX]
                pygame.draw.rect(self.game.fenetre, (255,0,255), pygame.Rect(tuile.rect.x, tuile.rect.y, 100,100))
                
                self.directionRush=(tuile.rect.x, tuile.rect.y)
                self.game.afficherText(str(self.directionRush))
                self.dx, self.dy = self.directionRush[0] - self.rect.x, self.directionRush[1] - self.rect.y
                self.rush=True
                
    def lunchProjectile(self):
        rand = random.randint(0,1)
        rand=0
        
        if rand == 0:
            
            mob_proche = []
            xMob = self.game.joueur.rect.x
            yMob = self.game.joueur.rect.y-10
            distance = sqrt((self.rect.x - self.game.joueur.skin.get_width()/2 - xMob)**2 + (self.rect.y -self.game.joueur.skin.get_height()/2 - yMob)**2)

            if distance < self.range :
                mob_proche.append((self.game.joueur, distance))
            
            mob_proche.sort(key=lambda tup: tup[1]) #pour trier la liste selon la distance
            
            now = self.game.tempsJeu()
            
            if len(mob_proche)>0 and now-self.lastProjectile>=self.cooldown:
                mobPlusProche = mob_proche[0][0]

                self.game.groupProjectile.add(Projectile(self.game, "bossElec", 5, 10, self.rect.x+30, self.rect.y+30, mobPlusProche, self, dureeMax=3000))
                self.lastProjectile = now
                self.cooldown=1000
        if rand == 1:
            
            now = self.game.tempsJeu()
            if now-self.lastProjectile>=self.cooldown:

                self.game.groupProjectile.add(Projectile(self.game, "bossElec", 5, 10, self.rect.x+30, self.rect.y+30, self, self, (self.rect.x+1000, self.rect.y+1000), dureeMax=1500))
                self.game.groupProjectile.add(Projectile(self.game, "bossElec", 5, 10, self.rect.x+30, self.rect.y+30, self, self, (self.rect.x-1000, self.rect.y+1000), dureeMax=1500))
                self.game.groupProjectile.add(Projectile(self.game, "bossElec", 5, 10, self.rect.x+30, self.rect.y+30, self, self, (self.rect.x-1000, self.rect.y-1000), dureeMax=1500))
                self.game.groupProjectile.add(Projectile(self.game, "bossElec", 5, 10, self.rect.x+30, self.rect.y+30, self, self, (self.rect.x+1000, self.rect.y-1000), dureeMax=1500))
                self.lastProjectile = now
                self.cooldown=1000
    def takeDamage(self, entier, moveX, moveY):
        if self.health >0 :
            self.health-=entier
        if self.health<=0:
            self.kill()
            
