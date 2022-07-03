import pygame
import random
class Projectile(pygame.sprite.Sprite):

     def __init__(self, game, nom, vitesse, mob, tuileBatimentCompatible):
          super().__init__()
          #affichage et information
          self.name = nom
          self.img = self.loadImg(nom)
          self.game = game
          self.velocity = vitesse
          

          self.rect = self.img.get_rect()
          self.rect.x = self.game.map[tuileBatimentCompatible[0]][tuileBatimentCompatible[1]].rect.x
          self.rect.y = self.game.map[tuileBatimentCompatible[0]][tuileBatimentCompatible[1]].rect.y
          
     def loadImg(self, nom):
        if nom== "fleche":
            scale = (704*0.13, 613*0.13)
        tempIgmg = pygame.image.load("data/projectile"+nom+".png")
        tempIgmg = pygame.transform.scale(tempIgmg, scale)
        return tempIgmg


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
        if self.deplacementAutorise("haut"):
            self.goUp()
            tuile = majSelectionJoueur(self.game, self.getFeet())
            self.setPos(tuile)
            return True
        return False        
         
     def setPos(self, tuile):
            self.posX, self.posY = tuile.posX, tuile.posY

     def goLeft(self):
            self.rect.x-=self.velocity
     
     
        
        
     def goRight(self):
        self.rect.x+=self.velocity
        
     def goUp(self):
         self.rect.y-=self.velocity
         
     def goDown(self):
         self.rect.y+=self.velocity
