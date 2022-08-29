from math import sqrt
import pygame
import random
from projectile import Projectile
from selection import majSelectionJoueur
class Mob(pygame.sprite.Sprite):

     def __init__(self, game, nom, vie, vitesse, tuile, score, pique=False, aquatique=False, aerien=False, attaque=10):
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
          self.score = score
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
          if self.name=="oursin":
            self.originSkin = self.skin
            self.angle = 0
            self.neg = False #sens de rotation
          if self.name=="golem_des_forets":
              self.listeAnnimGolem = self.game.images.golemAnnim
          if self.name=="kraken":
              self.listeAnnimKraken = self.game.images.krakenAnnim
          if self.name=="yeti":
              self.listeAnnimYeti = self.game.images.yetiAnnim
          if self.name=="mage":
              self.listeAnnimMage = self.game.images.mageAnnim
          if self.name=="dragon":
              self.listeAnnimDragon = self.game.images.dragonAnnim
              
          self.clockAnnim=0
          self.indiceAnnim=0
          self.droite = True
          
     def rotate(self, neg = False, angle = 4):
         if not neg :
            self.angle+=angle
         else :
             self.angle-=angle
         self.skin = pygame.transform.rotozoom(self.originSkin, self.angle, 1)
         self.rect = self.skin.get_rect(center=self.rect.center)
     
     
          
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
     """
     def changeAnnimOursin(self):
         self.clockAnnim+=1
         if self.clockAnnim==5:
            self.indiceAnnim+=1
            if self.indiceAnnim >= len(self.listeAnnimOursin):
                self.indiceAnnim=0
            self.clockAnnim=0
            self.skin = self.listeAnnimOursin[self.indiceAnnim]
            
     def changeAnnimOursin2(self):
         self.clockAnnim+=1
         if self.clockAnnim==5:
            self.indiceAnnim+=1
            if self.indiceAnnim >= len(self.listeAnnimOursin):
                self.indiceAnnim=0
            self.clockAnnim=0
            self.skin = self.listeAnnimOursin2[self.indiceAnnim] """
     def allerVersTuile(self, posX, posY): #renvoie True si il a atteint la tuile, False sinon
         
        if posY == self.posY and posX-self.posX>0:
            self.goUp(angle=2)
            self.goRight(angle=2)
            newTuile = majSelectionJoueur(self.game, (self.getFeet()[0]-244/4, self.getFeet()[1]+142/4))
            self.setPos(newTuile)
        if posY==self.posY and posX-self.posX<0:
            self.goDown(angle=2)
            self.goLeft(angle=2)
            newTuile = majSelectionJoueur(self.game, (self.getFeet()[0]+244/4, self.getFeet()[1]-142/4))
            self.setPos(newTuile)
        if posX==self.posX and posY-self.posY>0:
            self.goRight(angle=2)
            self.goDown(angle=2)
            newTuile = majSelectionJoueur(self.game, (self.getFeet()[0]-244/4, self.getFeet()[1]-142/4))
            self.setPos(newTuile)
        if posX==self.posX and posY-self.posY<0:
            self.goUp(angle=2)
            self.goLeft(angle=2)
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
            scale = (241*0.32, 249*0.32)
            skin = pygame.image.load("data/personnages/golem/golem_des_forets_1.png").convert_alpha()
            skin = pygame.transform.scale(skin, scale)
            return skin
        elif nomSkin=="oursin":
            scale = (175*0.56, 142*0.56)
        elif nomSkin=="yeti":
            scale = (205*0.5, 318*0.5)
            skin = pygame.image.load("data/personnages/yeti/yeti_1.png").convert_alpha()
            skin = pygame.transform.scale(skin, scale)
            return skin
        elif nomSkin=="dragon":
            scale =(436*0.3, 473*0.3)
            skin = pygame.image.load("data/personnages/dragon/dragon_2.png").convert_alpha()
            skin = pygame.transform.scale(skin, scale)
            return skin
        elif nomSkin=="mage":
            scale =(111*0.62, 214*0.62)
            skin = pygame.image.load("data/personnages/mage/mage_1.png").convert_alpha()
            skin = pygame.transform.scale(skin, scale)
            return skin
        elif nomSkin=="kraken":
            scale = (279*0.5, 177*0.5)
            skin = pygame.image.load("data/personnages/kraken/kraken_1.png").convert_alpha()
            skin = pygame.transform.scale(skin, scale)
            return skin
        skin = pygame.image.load("data/personnages/"+nomSkin+".png").convert_alpha()
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
            self.game.joueur.score=+self.score
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
             
             
     def changeAnnimGolem(self):
        self.clockAnnim+=1
        if self.clockAnnim==5:
            self.indiceAnnim+=1
            if self.indiceAnnim>=len(self.listeAnnimGolem):
                self.indiceAnnim=0
            self.skin=self.listeAnnimGolem[self.indiceAnnim]
            self.clockAnnim=0
    
    
     def changeAnnimDragon(self, flip=False):
        self.clockAnnim+=1
        if self.clockAnnim==7:
            self.indiceAnnim+=1
            if self.indiceAnnim>=len(self.listeAnnimDragon):
                self.indiceAnnim=0
            if not flip:
                self.skin=self.listeAnnimDragon[self.indiceAnnim]
                print("droite")
            else :
                self.skin=pygame.transform.flip(self.listeAnnimDragon[self.indiceAnnim], True, False)
                print("gauche")
            self.clockAnnim=0
     
     def changeAnnimKraken(self, flip=False):
        self.clockAnnim+=1
        if self.clockAnnim==10:
            self.indiceAnnim+=1
            if self.indiceAnnim==len(self.listeAnnimKraken):
                self.indiceAnnim=0
            if not flip:
                self.skin=self.listeAnnimKraken[self.indiceAnnim]
            else:
                self.skin=pygame.transform.flip(self.listeAnnimKraken[self.indiceAnnim], True, False)
            self.clockAnnim=0
            
     def changeAnnimYeti(self, flip=False):
        self.clockAnnim+=1
        if self.clockAnnim==10:
            self.indiceAnnim+=1
            if self.indiceAnnim==len(self.listeAnnimYeti):
                self.indiceAnnim=0
            if not flip:
                self.skin=self.listeAnnimYeti[self.indiceAnnim]
            else:
                self.skin=pygame.transform.flip(self.listeAnnimYeti[self.indiceAnnim], True, False)
            self.clockAnnim=0
     def changeAnnimMage(self, flip=False):
        self.clockAnnim+=1
        if self.clockAnnim==10:
            self.indiceAnnim+=1
            if self.indiceAnnim==len(self.listeAnnimMage):
                self.indiceAnnim=0
            if not flip:
                self.skin=self.listeAnnimMage[self.indiceAnnim]
            else :
                self.skin = pygame.transform.flip(self.listeAnnimMage[self.indiceAnnim], True, False)
            self.clockAnnim=0
            
     def goLeft(self, angle=4):
        if self.name=="oursin":    
            self.rotate(angle=angle)
            self.neg = False
        self.rect.x-=self.velocity 
        if self.name=="golem_des_forets":
            self.changeAnnimGolem()
        if self.name=="kraken":
            self.changeAnnimKraken()
        if self.name=="yeti":
            self.changeAnnimYeti(True)
        if self.name=="mage":
            self.changeAnnimMage(True)
        if self.name=="dragon":
            self.changeAnnimDragon(True)
            print("gaucheG")
        self.droite = True
        
     def goRight(self, angle=4):
        self.rect.x+=self.velocity
        if self.name=="oursin":
            self.rotate(True, angle)
            self.neg= True
        if self.name=="golem_des_forets":
            self.changeAnnimGolem()
        if self.name=="kraken":
            self.changeAnnimKraken(True)
        if self.name=="yeti":
            self.changeAnnimYeti()
        if self.name=="mage":
            self.changeAnnimMage()
        if self.name=="dragon":
            self.changeAnnimDragon()
            print("droiteD")
        self.droite=False
        
     def goUp(self, angle=4):
         self.rect.y-=self.velocity
         if self.name=="oursin":    
                self.rotate(self.neg, angle)
         if self.name=="golem_des_forets":
            self.changeAnnimGolem()
         if self.name=="kraken":
            self.changeAnnimKraken(self.droite)
         if self.name=="yeti":
            self.changeAnnimYeti(self.droite)
         if self.name=="mage":
            self.changeAnnimMage(self.droite)
         if self.name=="dragon":
            self.changeAnnimDragon(self.droite)
            
            
     def goDown(self, angle=4):
         if self.name=="oursin":    
                self.rotate(self.neg, angle)
         self.rect.y+=self.velocity
         
         if self.name=="golem_des_forets":
             self.changeAnnimGolem()
         if self.name=="kraken":
            self.changeAnnimKraken(self.droite)
         if self.name=="yeti":
            self.changeAnnimYeti(self.droite)
         if self.name=="mage":
            self.changeAnnimMage(self.droite)
         if self.name=="dragon":
            self.changeAnnimDragon(self.droite)
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
