from math import sqrt
import pygame
import random
from projectile import Projectile
from selection import majSelectionJoueur
class Mob(pygame.sprite.Sprite):

     def __init__(self, game, nom, vie, vitesse, tuile, pique=False, aquatique=False, aerien=False, attaque=10):
          super().__init__()
          #affichage et information
          self.name = nom
          self.skin = self.loadSkin(nom)
          self.skinMask = pygame.mask.from_surface(self.skin)
          self.game = game
          self.bateau = False
          #self.skinBateau = self.loadSkin("bateau",(100, 150))
          self.health = vie
          self.max_health =vie
          self.pique = pique
          self.aquatique = aquatique
          self.aerien = aerien
          self.attack = attaque
          self.velocity = vitesse
          self.maxVelocity = self.velocity
          self.slow =False
          self.armor = 0
          self.posX, self.posY = tuile.posX, tuile.posY
          self.last=0
          self.the_path = [[self.posY, self.posX]]
          self.fini = True
          self.cooldown = 0

          self.rect = self.skin.get_rect()
          self.rect.x, self.rect.y = self.initRect()
          
          self.lastProjectile=0
          if self.name=="mage":
              self.speedProjectile=3
          else:
              self.speedProjectile=5
          self.damageDistance = 5
          self.range=300
          self.recompenseWood, self.recompenseStone, self.recompenseFood, self.recompenseWater=0,0,0,0
          self.initRecompense(self.name)
          
     def initRect(self):
        if self.name=="yeti":
            x =self.game.map[self.posY][self.posX].rect.x+70+random.randint(-5, 5)
            y= self.game.map[self.posY][self.posX].rect.y-60+random.randint(-5, 5)
            return x,y
        if self.name=="oursin":
            x =self.game.map[self.posY][self.posX].rect.x+100+random.randint(-5, 5)
            y= self.game.map[self.posY][self.posX].rect.y+30+random.randint(-5, 5)
            return x,y
        if self.name=="golem_des_forets":
            x =self.game.map[self.posY][self.posX].rect.x+90+random.randint(-5, 5)
            y= self.game.map[self.posY][self.posX].rect.y+30+random.randint(-5, 5)
            return x,y
        if self.name=="mage":
            x =self.game.map[self.posY][self.posX].rect.x+90+random.randint(-5, 5)
            y= self.game.map[self.posY][self.posX].rect.y+random.randint(-5, 5)
            return x,y
        if self.name=="kraken":
            x=self.game.map[self.posY][self.posX].rect.x+90+random.randint(-5, 5)
            y=self.game.map[self.posY][self.posX].rect.y+30+random.randint(-5, 5)
            return x,y
        if self.name=="dragon":
            x=self.game.map[self.posY][self.posX].rect.x+90+random.randint(-5, 5)
            y=self.game.map[self.posY][self.posX].rect.y+30+random.randint(-5, 5)
            return x,y
        print("oublie de calibrage du mob en rect.x et rect.y") 
        assert(False)

     def setVelocity(self, entier):
        self.velocity += entier
          

     def initRecompense(self, name):
         if name=="golem_des_forets":
             self.recompenseWood = random.randint(10,25)
             self.recompenseWater=0
             self.recompenseStone=0
             self.recompenseFood=0
         if name=="oursin":
             self.recompenseWood = 0
             self.recompenseWater=0
             self.recompenseStone=random.randint(5,15)
             self.recompenseFood=0
         if name=="dragon":
             self.recompenseWood = 0
             self.recompenseWater=0
             self.recompenseStone=random.randint(15,25)
             self.recompenseFood=0
         if name=="kraken":
             self.recompenseWood = 0
             self.recompenseWater=0
             self.recompenseStone=0
             self.recompenseFood=random.randint(10,20)
        

         
     def allerVersTuile(self, posX, posY): #renvoie True si il a atteint la tuile, False sinon
         
        if posY == self.posY and posX-self.posX>0:
            self.goUp()
            self.goRight()
            newTuile = majSelectionJoueur(self.game, (self.getFeet()[0]-244/4, self.getFeet()[1]+142/4))
            self.setPos(newTuile)
        if posY==self.posY and posX-self.posX<0:
            self.goDown()
            self.goLeft()
            newTuile = majSelectionJoueur(self.game, (self.getFeet()[0]+244/4, self.getFeet()[1]-142/4))
            self.setPos(newTuile)
        if posX==self.posX and posY-self.posY>0:
            self.goRight()
            self.goDown()
            newTuile = majSelectionJoueur(self.game, (self.getFeet()[0]-244/4, self.getFeet()[1]-142/4))
            self.setPos(newTuile)
        if posX==self.posX and posY-self.posY<0:
            self.goUp()
            self.goLeft()
            newTuile = majSelectionJoueur(self.game, (self.getFeet()[0]+244/4, self.getFeet()[1]+142/4))
            self.setPos(newTuile)
        if posX-self.posX>0 and posY-self.posY>0:
            self.goRight()
            newTuile = majSelectionJoueur(self.game, (self.getFeet()[0]-244/2, self.getFeet()[1]))
            self.setPos(newTuile)
        if posX-self.posX>0 and posY-self.posY<0:
            self.goUp()
            newTuile = majSelectionJoueur(self.game, (self.getFeet()[0], self.getFeet()[1]+142/2))
            self.setPos(newTuile)
        if posX-self.posX<0 and posY-self.posY<0:
            self.goLeft()
            newTuile = majSelectionJoueur(self.game, (self.getFeet()[0]+244/2, self.getFeet()[1]))
            self.setPos(newTuile)
        if posX-self.posX<0 and posY-self.posY>0:
            self.goDown()
            newTuile = majSelectionJoueur(self.game, (self.getFeet()[0], self.getFeet()[1]-142/2))
            self.setPos(newTuile)
        return self.posX == posX and self.posY==posY

     def getFeet(self):
         if self.name == "mage":
             return self.rect.x+30, self.rect.y+100
         if self.name == "yeti":
             return self.rect.x+40, self.rect.y+150
         if self.name == "dragon":
             return self.rect.x, self.rect.y+150
         return self.rect.x+45, self.rect.y+50
     
     def caseBloquanteAutour(self, posX, posY):
         return self.game.map[posY+1][posX].caseBloquante() and self.game.map[posY-1][posX].caseBloquante() and self.game.map[posY][posX-1].caseBloquante() and self.game.map[posY][posX+1].caseBloquante()

     def initPos(self):
         if self.aquatique:
            
            tuile = random.choice(self.game.listeCaseMer)
            
         elif self.name=="oursin":
             tuile=random.choice(self.game.listeCasePlaine)
         
         elif self.aerien:
             tuile=random.choice(self.game.listeCaseMontagne)
         
         elif self.name=="golem_des_forets" or "mage":
             tuile=random.choice(self.game.listeCaseForet)
             
         return tuile.posX, tuile.posY
     def loadSkin(self, nomSkin):
        if nomSkin== "golem_des_forets":
            scale = (704*0.13, 613*0.13)
        elif nomSkin=="oursin":
            scale = (751*0.13, 613*0.13)
        elif nomSkin=="kraken":
            scale = (756*0.13, 480*0.13)
        elif nomSkin=="dragon":
            scale = (375*0.13, 612*0.13)
        elif nomSkin=="mage":
            scale = (323*0.2, 612*0.2)
        elif nomSkin=="yeti":
            scale = (413*0.3,611*0.3)
            
        skin = pygame.image.load("data/personnages/"+nomSkin+".png")
        skin = pygame.transform.scale(skin, scale)
        return skin

     def lunchProjectile(self):
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
            
            
            self.game.groupProjectile.add(Projectile(self.game, self.name, self.speedProjectile, self.damageDistance, self.rect.x+30, self.rect.y+30, mobPlusProche))
            self.lastProjectile = now
            self.cooldown=1000


     def takeDamage(self, entier):
        if self.health >0 :
            self.health-=entier
            self.update_health_bar()
        if self.health<=0:
            if self.name=="mage":
                self.game.joueur.health+=15
            self.game.joueur.setRessource(self.recompenseWood, self.recompenseStone, self.recompenseFood, self.recompenseWater)
            self.kill()


     def moveMob(self, joueur):
        diffX = self.rect.x - joueur.rect.x
        diffY = self.rect.y - joueur.rect.y
        if diffY >= 0 and diffX>=0: #le joueur est en haut a gauche
            reussi = self.mobHaut()
            reussi = self.mobGauche() or reussi
            if not reussi:
                if random.randint(0,1):
                    self.mobBas()
                else:
                    self.mobDroite()
    
        elif diffY<=0 and diffX>=0: #le joueur est en bas a gauche
            reussi = self.mobBas()
            reussi  = self.mobGauche() or reussi
            if not reussi :
                if random.randint(0,1):
                    self.mobDroite()
                else :
                    self.mobHaut()

        elif diffY<=0 and diffX<=0: #le joueur est en bas a droite
            reussi = self.mobBas()
            reussi = self.mobDroite() or reussi
            if not reussi:
                if random.randint(0,1):
                    self.mobGauche()
                else :
                    self.mobHaut()
            
        elif diffY>=0 and diffX<=0: #le joueur est en haut a droite
            reussi = self.mobHaut()
            reussi = self.mobDroite() or reussi
            if not reussi:
                if random.randint(0,1):
                    self.mobGauche()
                else :
                    self.mobBas()
            
        
          
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
        self.goUp()
        tuile = majSelectionJoueur(self.game, self.getFeet())
        self.setPos(tuile)      
    
     def deplacementAutorise(self, direction):
         if direction=="droite":
            tuile = majSelectionJoueur(self.game, (self.getFeet()[0]+self.velocity, self.getFeet()[1]))
            
         if direction=="gauche":
            tuile = majSelectionJoueur(self.game, (self.getFeet()[0]-self.velocity, self.getFeet()[1]))
            
         if direction=="haut":
            tuile = majSelectionJoueur(self.game, (self.getFeet()[0], self.getFeet()[1]-self.velocity))
            
         if direction=="bas":
             tuile = majSelectionJoueur(self.game, (self.getFeet()[0], self.getFeet()[1]+self.velocity))
         if tuile:
            if self.tuileInterdit(tuile):
                
                if direction=="droite":
                    tuile = majSelectionJoueur(self.game, (self.getFeet()[0]+self.velocity+10, self.getFeet()[1]))
            
                if direction=="gauche":
                    tuile = majSelectionJoueur(self.game, (self.getFeet()[0]-self.velocity-10, self.getFeet()[1]))
                    
                if direction=="haut":
                    tuile = majSelectionJoueur(self.game, (self.getFeet()[0], self.getFeet()[1]-self.velocity-10))
                    
                if direction=="bas":
                    tuile = majSelectionJoueur(self.game, (self.getFeet()[0], self.getFeet()[1]+self.velocity+10))
            return not self.tuileInterdit(tuile)
        
         else:
             print("erreur dans fonction joueur.deplacement autorisé")
             return False
        
     def tuileInterdit(self, tuile):
          return tuile.tuileHaute() or (tuile.estMer() and tuile.pasPort() and not self.bateau) or (not tuile.estMer() and tuile.pasPort() and self.bateau)
         
         
     def setPos(self, tuile):
            self.posX, self.posY = tuile.posX, tuile.posY

     def goLeft(self):
            self.rect.x-=self.velocity
     
     
     def majCoolDown(self):
         if self.name=="kraken":
             self.cooldown=3000
         elif self.name=="golem_des_forets":
             self.cooldown=500
         elif self.name=="oursin":
             self.cooldown=1000
         elif self.name=="dragon":
             self.cooldown=2000
         elif self.name=="mage":
             self.cooldown=2000
         elif self.name=="yeti":
             self.cooldown=200
         else:
             assert(False), "Oublie du cooldown pour le mob"+self.nom   
        
         
        
     def goRight(self):
        self.rect.x+=self.velocity
        
     def goUp(self):
         self.rect.y-=self.velocity
         
     def goDown(self):
         self.rect.y+=self.velocity

     def update_health_bar(self):
        #def la couleur
        
        pourcentagePv = self.health/self.max_health*100
        if pourcentagePv >=80 : 
            bar_color = (111, 210, 46)
        elif pourcentagePv >=50 : 
            bar_color = (255, 165, 0)
        elif pourcentagePv >=25 : 
            bar_color = (255, 69, 0)
        elif pourcentagePv >=0 : 
            bar_color = (255, 0, 0)
        else :
            bar_color = (255, 0, 0)
        back_bar_color = (60,63,60)
        bar_position = [self.rect.x, self.rect.y-10, pourcentagePv, 5]
        back_bar_position = [self.rect.x, self.rect.y-10, 100, 5]
        #dessiner la barre de vie
        pygame.draw.rect(self.game.fenetre, back_bar_color, back_bar_position)
        pygame.draw.rect(self.game.fenetre, bar_color, bar_position)
