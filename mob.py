from math import sqrt
import time
import pygame
import random
from loot import Loot
from projectile import Projectile
from selection import majSelectionMob
import tuto
class Mob(pygame.sprite.Sprite):

     def __init__(self, game, nom, vie, vitesse, tuile, score, pique=False, aquatique=False, aerien=False, attaque=10, annimal=False, desertique=False):
          super().__init__()
          #affichage et information
          self.name = nom
          self.skin = self.loadSkin(nom)
          self.image = self.skin
          self.mask = pygame.mask.from_surface(self.skin)
          self.game = game
          self.bateau = False
          self.annimal=annimal
          #self.skinBateau = self.loadSkin("bateau",(100, 150))
          self.health = vie
          self.max_health =vie
          self.pique = pique
          self.aquatique = aquatique
          self.aerien = aerien
          self.desertique = desertique
          self.attack = attaque
          self.velocity = vitesse
          self.maxVelocity = self.velocity
          self.slow =False
          self.armor = 0
          self.posX, self.posY = tuile.posX, tuile.posY
          
          self.the_path = [[self.posY, self.posX]]
          self.fini = True
          self.cooldown = self.majCoolDown()
          self.last=random.randint(0,self.cooldown-1)
          self.score = score
          self.rect = self.skin.get_rect()
          self.rect.x, self.rect.y = self.initRect()
          self.tuileMob = 0
          self.lastProjectile=0
          if self.name=="mage":
              self.speedProjectile=3
          else:
              self.speedProjectile=5
          self.stop=1
          self.damageDistance = 5
          self.range=300
          self.recompenseWood, self.recompenseStone, self.recompenseFood, self.recompenseWater=0,0,0,0
          self.initRecompense(self.name)
          if self.name=="oursin":
            self.listeAnnimOursin = self.game.images.oursinAnnim
            self.originSkin = self.game.images.oursinAnnim[:]
            self.angle = 0
            self.neg = False #sens de rotation
          if self.name=="golem_des_forets":
              self.listeAnnimGolem = self.game.images.golemAnnim
              self.listeAnnimGolemSpawn = self.game.images.golemAnnimSpawn[:]
          if self.name=="kraken":
              self.listeAnnimKraken = self.game.images.krakenAnnim
          if self.name=="yeti":
              self.listeAnnimYeti = self.game.images.yetiAnnim
          if self.name=="mage":
              self.listeAnnimMage = self.game.images.mageAnnim
          if self.name=="dragon":
              self.listeAnnimDragon = self.game.images.dragonAnnim
          if self.name == "oiseau":
              self.listeAnnimOiseau = self.game.images.oiseauAnnim
          if self.name == "chameau":
              self.listeAnnimChameau =self.game.images.chameauAnnim
          if self.name == "lapin":
              self.listeAnnimLapin =self.game.images.lapinAnnim
          if self.name == "oiseau2":
              self.listeAnnimOiseau2 =self.game.images.oiseau2Annim
          if self.name == "renard":
              self.listeAnnimRenard =self.game.images.renardAnnim
          self.clockAnnim=0
          self.indiceAnnim=0
          self.droite = True
          
     def rotate(self, neg = False, angle = 4):
         if not neg :
            self.angle+=angle
         else :
             self.angle-=angle
         self.skin = pygame.transform.rotozoom(self.originSkin[self.indiceAnnim], self.angle, 1)
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
        if self.name=="oiseau":
            x=self.game.map[self.posY][self.posX].rect.x+90+random.randint(-5, 5)
            y=self.game.map[self.posY][self.posX].rect.y+30+random.randint(-5, 5)
            return x,y
        if self.name=="chameau":
            x=self.game.map[self.posY][self.posX].rect.x+90+random.randint(-5, 5)
            y=self.game.map[self.posY][self.posX].rect.y+30+random.randint(-5, 5)
            return x,y
        if self.name=="lapin":
            x=self.game.map[self.posY][self.posX].rect.x+90+random.randint(-5, 5)
            y=self.game.map[self.posY][self.posX].rect.y+30+random.randint(-5, 5)
            return x,y
        if self.name=="oiseau2":
            x=self.game.map[self.posY][self.posX].rect.x+90+random.randint(-5, 5)
            y=self.game.map[self.posY][self.posX].rect.y+30+random.randint(-5, 5)
            return x,y
        if self.name=="renard":
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
                self.goUp(angle=2)
                self.goRight(angle=2)
                
                newTuile = majSelectionMob(self.game, self, -244/4, 142/4)
                if newTuile!=None:
                    self.setPos(newTuile)
        if posY==self.posY and posX-self.posX<0:

                self.goDown(angle=2)
                self.goLeft(angle=2)
                newTuile = majSelectionMob(self.game, self,244/4, -142/4)
                if newTuile!=None:
                    self.setPos(newTuile)
                
        if posX==self.posX and posY-self.posY>0:

                self.goRight(angle=2)
                self.goDown(angle=2)
                newTuile = majSelectionMob(self.game, self,-244/4, -142/4)
                if newTuile!=None:
                    self.setPos(newTuile)
        if posX==self.posX and posY-self.posY<0:

                self.goUp(angle=2)
                self.goLeft(angle=2)
                newTuile = majSelectionMob(self.game, self,244/4, 142/4)
                if newTuile!=None:
                    self.setPos(newTuile)
                
        if posX-self.posX>0 and posY-self.posY>0:

                self.goRight()
                newTuile = majSelectionMob(self.game, self,-244/2, 0)
                if newTuile!=None:
                    self.setPos(newTuile)
        if posX-self.posX>0 and posY-self.posY<0:

                self.goUp()
                newTuile = majSelectionMob(self.game, self,0, 142/2)
                if newTuile!=None:
                    self.setPos(newTuile)
        if posX-self.posX<0 and posY-self.posY<0:

                self.goLeft()
                newTuile = majSelectionMob(self.game, self,244/2, 0)
                if newTuile!=None:
                    self.setPos(newTuile)
        if posX-self.posX<0 and posY-self.posY>0:

                self.goDown()
                newTuile = majSelectionMob(self.game, self,0, -142/2)
                if newTuile!=None:
                    self.setPos(newTuile)
        
        return self.posX == posX and self.posY==posY

     def getFeet(self):
         if self.name=="golem_des_forets":
             return self.rect.x+65, self.rect.y+90
         if self.name == "mage":
             return self.rect.x+30, self.rect.y+110
         if self.name == "yeti":
             return self.rect.x+40, self.rect.y+150
         if self.name == "dragon":
             return self.rect.x+75, self.rect.y+90
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
            scale = (241*0.55, 249*0.50)
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
            skin = pygame.image.load("data/personnages/kraken/kraken (1).png").convert_alpha()
            skin = pygame.transform.scale(skin, scale)
            return skin
        elif nomSkin=="oiseau":
            scale = (240*0.3, 314*0.3)
            skin = pygame.image.load("data/personnages/oiseau/oiseau (1).png").convert_alpha()
            skin = pygame.transform.scale(skin, scale)
            return skin
        elif nomSkin=="lapin":
            skin = pygame.image.load("data/personnages/lapin/lapin (1).png").convert_alpha()
            skin = pygame.transform.scale(skin, (skin.get_width()*0.5, skin.get_height()*0.5))
            return skin
        
        elif nomSkin=="oiseau2":
            scale = (240*0.3, 314*0.3)
            skin = pygame.image.load("data/personnages/oiseau/oiseau2 (1).png").convert_alpha()
            skin = pygame.transform.scale(skin, scale)
            return skin
        elif nomSkin=="renard":
            scale = (62, 55)
            skin = pygame.image.load("data/personnages/renard/renard1.png").convert_alpha()
            skin = pygame.transform.scale(skin, scale)
            return skin
        elif nomSkin=="chameau":
            scale = (127, 110)
            skin = pygame.image.load("data/personnages/chameau/chameau (1).png").convert_alpha()
            skin = pygame.transform.scale(skin, scale)
            return skin
        
        skin = pygame.image.load("data/personnages/"+nomSkin+".png").convert_alpha()
        skin = pygame.transform.scale(skin, scale)
        return skin

     def destAnnimal(self):
         if self.name=="oiseau":
            x=self.posX
            y=self.posY
            while abs(self.posX-x)+abs(self.posY-y)<4:
                x = random.randint(1, self.game.taille_matriceX-1)
                y = random.randint(1, self.game.taille_matriceY-1)
            return x,y
        
         if self.name=="chameau":
             type=[6]
         if self.name=="lapin":
             type=[1, 4]
         if self.name=="oiseau2":
             type=[4]
         if self.name=="renard":
             type=[4]
         casePossible = []
         for i in range(-1,2):
                for j in range(-1,2):
                    if self.game.verifierCo(self.posX+j, self.posY+i):
                        if (i!=0 or j!=0) and (j!=1 or i!=-1) and (j!=-1 or i!=1) and self.game.map[self.posY+i][self.posX+j].type in type:
                            casePossible.append(self.game.map[self.posY+i][self.posX+j])
            
         if casePossible:
            if random.randint(0,4) or self.name=="lapin" or self.name=="oiseau2" or self.name=="renard":
                tuile = random.choice(casePossible)
                return tuile.posX,tuile.posY
            else:
                return self.posX,self.posY
         else:
            print(self.name, "bloque en", self.posX, self.posY, "de type", self.game.map[self.posY][self.posX].type, "suppression de", self.name)
            self.kill()
            return self.posX, self.posY
            

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
            self.game.groupProjectile.add(Projectile(self.game, "bossElec", self.speedProjectile, self.damageDistance, self.rect.x+30, self.rect.y+30, mobPlusProche, self))
            self.lastProjectile = now
            self.cooldown=1000


     def takeDamage(self, entier, moveX, moveY):
        if self.health >0 :
            self.health-=entier
            self.update_health_bar()
        if self.health<=0:
            if self.name=="mage":
                self.game.joueur.health+=15
                tuto.upadateStatutTuto(self.game,"soin")
                if self.game.joueur.health>100:
                    self.game.joueur.health=100
            self.game.groupLoot.add(Loot(self.recompenseWood, self.recompenseStone, self.recompenseWater, self.recompenseFood, self.rect.x+20-moveX, self.rect.y-30-moveY, self.game))
            self.game.joueur.setRessource(self.recompenseWood, self.recompenseStone, self.recompenseFood, self.recompenseWater)
            self.game.joueur.score=+self.score
            if self.name=="chameau" or self.name=="lapin":
                self.game.joueur.indiceEcolo+=3
                self.game.infoMortAnnimal = 440
                self.game.joueur.nbAnnimauxTue+=1
            self.kill()

     """def moveMob(self, joueur):
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
            tuile = majSelectionJoueur(self.game)
            self.setPos(tuile)
            return True
        return False        
        
     def mobHaut(self):
        self.goUp()
        tuile = majSelectionJoueur(self.game)
        self.setPos(tuile)      """
    
     def deplacementAutorise(self, direction):
         if direction=="droite":
            tuile = majSelectionMob(self.game, self, self.velocity, 0)
            
         if direction=="gauche":
            tuile = majSelectionMob(self.game, self, -self.velocity, 0)
            
         if direction=="haut":
            tuile = majSelectionMob(self.game, self,0, -self.velocity)
            
         if direction=="bas":
             tuile = majSelectionMob(self.game, self,0, self.velocity)
         if tuile:
            if self.tuileInterdit(tuile):
                
                if direction=="droite":
                    tuile = majSelectionMob(self.game, self,self.velocity+10, 0)
            
                if direction=="gauche":
                    tuile = majSelectionMob(self.game, self,-self.velocity-10, 0)
                    
                if direction=="haut":
                    tuile = majSelectionMob(self.game, self,0, -self.velocity-10)
                    
                if direction=="bas":
                    tuile = majSelectionMob(self.game, self,0, self.velocity+10)
            
            return not self.tuileInterdit(tuile)
        
         else:
             print("erreur dans fonction joueur.deplacement autorisé")
             return False
        
     def tuileInterdit(self, tuile):
          if self.name=="chameau":
            return tuile.type!=6 #uniquement les deserts
          return tuile.tuileHaute() or (tuile.estMer() and tuile.pasPort() and not self.bateau) or (not tuile.estMer() and tuile.pasPort() and self.bateau)
          
         
         
     def setPos(self, tuile):
            self.posX, self.posY = tuile.posX, tuile.posY


     
     
     def majCoolDown(self):
         if self.name=="kraken":
             cooldown=3000
         elif self.name=="golem_des_forets":
             cooldown=500
         elif self.name=="oursin":
             cooldown=1000
         elif self.name=="dragon":
             cooldown=2000
         elif self.name=="mage":
             cooldown=2000
         elif self.name=="yeti":
             cooldown=200
         elif self.name=="oiseau":
             cooldown=5000
         elif self.name=="chameau":
             cooldown=3000
         elif self.name=="lapin":
             cooldown=600
         elif self.name=="oiseau2":
             cooldown=600
         elif self.name=="renard":
             cooldown=1000
         else:
             assert(False), "Oublie du cooldown pour le mob"+self.nom   
         return cooldown

     def changeAnnimGolem(self):
        self.clockAnnim+=1
        if self.clockAnnim==5:
            self.indiceAnnim+=1
            if self.indiceAnnim>=len(self.listeAnnimGolem):
                self.indiceAnnim=0
            if self.listeAnnimGolemSpawn:
                self.skin=self.listeAnnimGolemSpawn[0]
                self.listeAnnimGolemSpawn.pop(0)
            else :
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

            else :
                self.skin=pygame.transform.flip(self.listeAnnimDragon[self.indiceAnnim], True, False)

            self.clockAnnim=0
     def changeAnnimOiseau(self, flip=False):
        self.clockAnnim+=1
        if self.clockAnnim==4:
            self.indiceAnnim+=1
            if self.indiceAnnim>=len(self.listeAnnimOiseau):
                self.indiceAnnim=0
            if not flip:
                self.skin=self.listeAnnimOiseau[self.indiceAnnim]
            else :
                self.skin=pygame.transform.flip(self.listeAnnimOiseau[self.indiceAnnim], True, False)
            self.clockAnnim=0
     def changeAnnimOiseau2(self, flip=False):
        self.clockAnnim+=1
        if self.clockAnnim==7:
            self.indiceAnnim+=1
            if self.indiceAnnim>=len(self.listeAnnimOiseau2):
                self.indiceAnnim=0
            if not flip:
                self.skin=self.listeAnnimOiseau2[self.indiceAnnim]
            else :
                self.skin=pygame.transform.flip(self.listeAnnimOiseau2[self.indiceAnnim], True, False)
            self.clockAnnim=0
     def changeAnnimRenard(self, flip=False):
        self.clockAnnim+=1
        if self.clockAnnim==7:
            self.indiceAnnim+=1
            if self.indiceAnnim>=len(self.listeAnnimRenard):
                self.indiceAnnim=0
            if not flip:
                self.skin=self.listeAnnimRenard[self.indiceAnnim]
            else :
                self.skin=pygame.transform.flip(self.listeAnnimRenard[self.indiceAnnim], True, False)
            self.clockAnnim=0
     def changeAnnimChameau(self, flip=False):
        self.clockAnnim+=1
        if self.clockAnnim==10:
            self.indiceAnnim+=1
            if self.indiceAnnim>=len(self.listeAnnimChameau):
                self.indiceAnnim=0
            if not flip:
                self.skin=self.listeAnnimChameau[self.indiceAnnim]
            else :
                self.skin=pygame.transform.flip(self.listeAnnimChameau[self.indiceAnnim], True, False)

            self.clockAnnim=0
     def changeAnnimLapin(self, flip=False):
        self.clockAnnim+=1
        if self.clockAnnim==4:
            self.indiceAnnim+=1
            if self.indiceAnnim>=len(self.listeAnnimLapin):
                self.indiceAnnim=0
            if not flip:
                self.skin=self.listeAnnimLapin[self.indiceAnnim]
            else :
                self.skin=pygame.transform.flip(self.listeAnnimLapin[self.indiceAnnim], True, False)
            self.clockAnnim=0
            
     def changeAnnimKraken(self, flip=False):
        self.clockAnnim+=1
        if self.clockAnnim==3:
            self.indiceAnnim+=1
            if self.indiceAnnim==len(self.listeAnnimKraken):
                self.indiceAnnim=0
            if not flip:
                self.skin=self.listeAnnimKraken[self.indiceAnnim]
            else:
                self.skin=pygame.transform.flip(self.listeAnnimKraken[self.indiceAnnim], True, False)
            self.clockAnnim=0
            
    
     def changeAnnimOursin(self, flip=False):

         self.clockAnnim+=1
         if self.clockAnnim==2:

            self.indiceAnnim+=1
            if self.indiceAnnim==len(self.listeAnnimOursin):
                self.indiceAnnim=0
                self.clockAnnim=-300
            else:
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
            self.changeAnnimKraken(True)
        if self.name=="oursin":
            self.changeAnnimOursin(True)
            
        if self.name=="yeti":
            self.changeAnnimYeti(True)
        if self.name=="mage":
            self.changeAnnimMage(True)
        if self.name=="dragon":
            self.changeAnnimDragon(True)
        if self.name=="oiseau":
            self.changeAnnimOiseau(True)
        if self.name=="chameau":
            self.changeAnnimChameau(True)
        if self.name=="lapin":
            self.changeAnnimLapin(True)
        if self.name=="oiseau2":
            self.changeAnnimOiseau2(True)
        if self.name=="renard":
            self.changeAnnimRenard(True)
        self.droite = True
        
     def goRight(self, angle=4):
        self.rect.x+=self.velocity
        if self.name=="oursin":
            self.rotate(True, angle)
            self.neg= True
        if self.name=="golem_des_forets":
            self.changeAnnimGolem()
        if self.name=="kraken":
            self.changeAnnimKraken()
        if self.name=="yeti":
            self.changeAnnimYeti()
        if self.name=="oursin":
            self.changeAnnimOursin()
            
        if self.name=="mage":
            self.changeAnnimMage()
        if self.name=="dragon":
            self.changeAnnimDragon()
        if self.name=="oiseau":
            self.changeAnnimOiseau()
        if self.name=="chameau":
            self.changeAnnimChameau()
        if self.name=="lapin":
            self.changeAnnimLapin()
        if self.name=="oiseau2":
            self.changeAnnimOiseau2()
        if self.name=="renard":
            self.changeAnnimRenard()
        self.droite=False
        
     def goUp(self, angle=4):
         self.rect.y-=self.velocity
         if self.name=="oursin":    
                self.rotate(self.neg, angle)
         if self.name=="golem_des_forets":
            self.changeAnnimGolem()
         if self.name=="oursin":
            self.changeAnnimOursin(True)
         if self.name=="kraken":
            self.changeAnnimKraken(self.droite)
         if self.name=="yeti":
            self.changeAnnimYeti(self.droite)
         if self.name=="mage":
            self.changeAnnimMage(self.droite)
         if self.name=="dragon":
            self.changeAnnimDragon(self.droite)
         if self.name=="oiseau":
            self.changeAnnimOiseau(self.droite)
         if self.name=="chameau":
            self.changeAnnimChameau(self.droite)
         if self.name=="lapin":
            self.changeAnnimLapin(self.droite)
         if self.name=="oiseau2":
            self.changeAnnimOiseau2(self.droite)
         if self.name=="renard":
            self.changeAnnimRenard(self.droite)
     def goDown(self, angle=4):
         if self.name=="oursin":    
                self.rotate(self.neg, angle)
         self.rect.y+=self.velocity
         if self.name=="oursin":
            self.changeAnnimOursin(True)
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
         if self.name=="oiseau":
            self.changeAnnimOiseau(self.droite)
         if self.name=="chameau":
            self.changeAnnimChameau(self.droite)
         if self.name=="lapin":
            self.changeAnnimLapin(self.droite)
         if self.name=="oiseau2":
            self.changeAnnimOiseau2(self.droite)
         if self.name=="renard":
            self.changeAnnimRenard(self.droite)
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
