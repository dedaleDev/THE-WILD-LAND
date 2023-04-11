import copy
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
        self.max_health = health
        police = pygame.font.Font("data/menu/font.ttf", 50)
        color = (255, 0, 0)
        self.texte_surface = police.render("Relouatord", True, color)
        self.texte_rect = self.texte_surface.get_rect()

        # Centrer le texte sur l'écran
        x = (game.infoObject[0] - self.texte_rect.width) // 2 +100
        y = 200
        self.texte_rect.center = (x, y)
        self.game = game
        self.annim=self.game.images.loadAnnimBoss()
        self.annimBoule=self.game.images.loadAnnimBossBoule()
        self.imageBoule=self.annimBoule[0]
        self.image = self.annim[0]
        self.tick=0
        self.tickMax=3
        self.indiceAnnim=0
        self.indiceAnnimBoule=0
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = game.mapBoss[2][3].rect.x, game.mapBoss[2][3].rect.y
        self.cooldown=0
        self.range = 10000
        self.lastProjectile=0
        self.name="Boss"
        self.recharge = None
        self.velocity=10
        self.vitesseProjectile=5
        self.rush=False
        self.directionRush=None
        self.dx, self.dy = 0,0
        self.listeCaseDispo = [(2, 0), (3, 0), (4, 0), (5, 0), (6, 1), (5, 1), (4, 1), (3, 1), (2, 1), 
                               (2, 2), (3, 2), (4, 2), (5, 2), (6, 2), (6, 3), (5, 3), (4, 3), (3, 3), (2, 3), (1, 3), 
                               (1, 4), (2, 4), (3, 4), (4, 4), (5, 4), (6, 4)]
    
    def getVitesseProjectile(self):
        self.vitesseProjectile=random.randint(4,7)
        return self.vitesseProjectile
    def getFeet(self):
        return self.rect.x+108, self.rect.y+200
    def moveBoss(self):
        if self.rush:
            
            dist = math.hypot(self.dx, self.dy) #Norme euclidienne
            if dist!=0:
                self.dx, self.dy = self.dx / dist, self.dy / dist  # normalisation du vecteur
            
                # bouger en direction du vecteur
                self.rect.x += round(self.dx * self.velocity)
                self.rect.y += round(self.dy * self.velocity)
            if (abs(self.directionRush.x-self.rect.x)+abs(self.directionRush.y-self.rect.y)<70) or not self.estDansArene(self.getFeet()[0],self.getFeet()[1], self.game.map[0][0]) :
                self.rush=False
        else:
            if not random.randint(0,100):
                co=random.choice(self.listeCaseDispo)
                tuileY=co[1] #trouver une tuile random sur la map
                tuileX=co[0]
                tuile=self.game.map[tuileY][tuileX] 
                self.directionRush=copy.deepcopy(tuile.rect)
                self.directionRush.x+=50
                self.directionRush.y-=100
                #self.game.afficherText(str((self.rect.x,self.rect.y)))
                self.dx, self.dy = self.directionRush.x - self.getFeet()[0], self.directionRush.y - self.getFeet()[1]
                self.rush=True
                if self.game.modeDifficile:
                    self.velocity=random.randint(5,15)
                if self.game.modeExtreme:
                    self.velocity=random.randint(8,20)
                if self.game.modeFacile:
                    self.velocity=random.randint(2,8)
                if self.game.modeNormal:
                    self.velocity=random.randint(4,10)
          
    def estDansArene(self, x,y,tuile00):
        A = tuile00.rect.center
        decalageVertical = A[1]
        decalageHorizontal = -tuile00.rect.x
        if y<0.57*(x+decalageHorizontal) +decalageVertical and y>-0.58*(x+decalageHorizontal) +decalageVertical and y<-0.58*(x+decalageHorizontal)+1000 +decalageVertical and y >0.59*(x+decalageHorizontal)-1020 +decalageVertical: 
            return True
        return False
    
    def update_health_bar(self):
        #def la couleur
        pourcentagePv = self.health/self.max_health*100
        bar_color = (111, 210, 46)
        back_bar_color = (60,63,60)
        
        
        maxHealth = 100*self.game.infoObject[0]*0.0045
        moitieBar = (maxHealth*self.game.infoObject[0]*0.0045)/2
        yBar = self.game.infoObject[1]*0.05

        xBar=(self.game.infoObject[0]/2)-(maxHealth*self.game.infoObject[0]*0.0045)/2
        bar_position = [xBar, yBar, pourcentagePv*self.game.infoObject[0]*0.0045, self.game.infoObject[1]*0.008]
        back_bar_position = [xBar, yBar, maxHealth, self.game.infoObject[1]*0.008]
        #dessiner la barre de vie
        pygame.draw.rect(self.game.fenetre, back_bar_color, back_bar_position)
        pygame.draw.rect(self.game.fenetre, bar_color, bar_position)
   

    def lunchProjectile(self):
        posXprojectile = 56
        posYprojectile = 124
        rand = random.randint(0,5)
        
        
        if rand < 5:
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
                self.game.groupProjectile.add(Projectile(self.game, "bossElec", self.getVitesseProjectile(), 10, self.rect.x+posXprojectile, self.rect.y+posYprojectile, mobPlusProche, self, dureeMax=3000))
                self.lastProjectile = now
                if self.game.modeDifficile:
                    self.cooldown=random.randint(800,1500)
                if self.game.modeExtreme:
                    self.cooldown=random.randint(500,1500)
                if self.game.modeFacile:
                    self.cooldown=random.randint(1800,2000)
                if self.game.modeNormal:
                    self.cooldown=random.randint(1300,2000)

        if rand == 5:

            now = self.game.tempsJeu()
            if now-self.lastProjectile>=self.cooldown:
                self.game.groupProjectile.add(Projectile(self.game, "bossElec", self.getVitesseProjectile(), 10, self.rect.x+posXprojectile, self.rect.y+posYprojectile, self, self, (self.rect.x+1000, self.rect.y+1000), dureeMax=1500))
                self.game.groupProjectile.add(Projectile(self.game, "bossElec", self.getVitesseProjectile(), 10, self.rect.x+posXprojectile, self.rect.y+posYprojectile, self, self, (self.rect.x-1000, self.rect.y+1000), dureeMax=1500))
                self.game.groupProjectile.add(Projectile(self.game, "bossElec", self.getVitesseProjectile(), 10, self.rect.x+posXprojectile, self.rect.y+posYprojectile, self, self, (self.rect.x-1000, self.rect.y-1000), dureeMax=1500))
                self.game.groupProjectile.add(Projectile(self.game, "bossElec", self.getVitesseProjectile(), 10, self.rect.x+posXprojectile, self.rect.y+posYprojectile, self, self, (self.rect.x+1000, self.rect.y-1000), dureeMax=1500))
                self.lastProjectile = now
                self.cooldown=random.randint(500,1500)

    def takeDamage(self, entier, moveX, moveY):
        if self.health >0 :
            self.health-=entier
        if self.health<=0:
            self.kill()

    def update(self):
        if self.tick==self.tickMax:
            self.tick=0
            self.indiceAnnim+=1
            self.indiceAnnimBoule+=1
            if self.indiceAnnim==len(self.annim):
                self.indiceAnnim=0
            self.image=self.annim[self.indiceAnnim]
            
            if self.indiceAnnimBoule==len(self.annimBoule):
                self.indiceAnnimBoule=0
            self.imageBoule=self.annimBoule[self.indiceAnnimBoule]
        else:
            self.tick+=1
        
    
    def drawHealthBar(self, screen):
        largeur = self.game.infoObject[0]
        hauteur = self.game.infoObject[1]
        yBar = hauteur*0.05
        moitieBar = (self.max_health*largeur*0.0045)/2
        xBar=(largeur/2)-(self.max_health*largeur*0.0045)/2
        barFond = (xBar, yBar, self.max_health*largeur*0.0045, hauteur*0.008)
        barDevant = (xBar, yBar, self.health*largeur*0.0045, hauteur*0.008)
        if self.health<=0:
            self.game.win = True
            self.kill()
        
        pygame.draw.rect(screen, (200, 200, 200), barFond)
        pygame.draw.rect(screen, (255, 0, 0), barDevant)
        
        screen.blit(self.texte_surface,(xBar+150,yBar+30))
        