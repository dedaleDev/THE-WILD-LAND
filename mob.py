import pygame
import random
from selection import majSelectionJoueur
import generation
class Mob(pygame.sprite.Sprite):

     def __init__(self, game, nom, vie, vitesse):
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
          self.attack = 10
          self.velocity = vitesse
          self.armor = 0
          self.posX, self.posY = self.initPos()

          self.rect = self.skin.get_rect()
          self.rect.x = self.game.map[self.posY][self.posX].rect.x+28
          self.rect.y = self.game.map[self.posY][self.posX].rect.y+97-75
          

     def setVelocity(self, entier):
        self.velocity += entier
          

     def allerVersTuile(self, posX, posY): #renvoie True si il a atteint la tuile, False sinon
        if posY == self.posY and posX-self.posX>0:
            self.goUp()
            self.goRight()
            newTuile = majSelectionJoueur(self.game, (self.getFeet()[0]-75/2, self.getFeet()[1]+75/2))
            self.setPos(newTuile)
        if posY==self.posY and posX-self.posX<0:
            self.goDown()
            self.goLeft()
            newTuile = majSelectionJoueur(self.game, (self.getFeet()[0]+75/2, self.getFeet()[1]-75/2))
            self.setPos(newTuile)
        if posX==self.posX and posY-self.posY>0:
            self.goRight()
            self.goDown()
            newTuile = majSelectionJoueur(self.game, (self.getFeet()[0]-75/2, self.getFeet()[1]-75/2))
            self.setPos(newTuile)
        if posX==self.posX and posY-self.posY<0:
            self.goUp()
            self.goLeft()
            newTuile = majSelectionJoueur(self.game, (self.getFeet()[0]+75/2, self.getFeet()[1]+75/2))
            self.setPos(newTuile)
        if posX-self.posX>0 and posY-self.posY>0:
            self.goRight()
            newTuile = majSelectionJoueur(self.game, (self.getFeet()[0]-75, self.getFeet()[1]))
            self.setPos(newTuile)
        if posX-self.posX>0 and posY-self.posY<0:
            self.goUp()
            newTuile = majSelectionJoueur(self.game, (self.getFeet()[0], self.getFeet()[1]+75))
            self.setPos(newTuile)
        if posX-self.posX<0 and posY-self.posY<0:
            self.goLeft()
            newTuile = majSelectionJoueur(self.game, (self.getFeet()[0]+75, self.getFeet()[1]))
            self.setPos(newTuile)
        if posX-self.posX<0 and posY-self.posY>0:
            self.goDown()
            newTuile = majSelectionJoueur(self.game, (self.getFeet()[0], self.getFeet()[1]-75))
            self.setPos(newTuile)
        return self.posX == posX and self.posY==posY

     def getFeet(self):
         return self.rect.x+45, self.rect.y+50
     
     def caseBloquanteAutour(self, posX, posY):
         return self.game.map[posY+1][posX].caseBloquante() and self.game.map[posY-1][posX].caseBloquante() and self.game.map[posY][posX-1].caseBloquante() and self.game.map[posY][posX+1].caseBloquante()

     def initPos(self):
         borneMaxX = min(generation.taille_matriceX-2, 20)
         borneMaxY = min(generation.taille_matriceY-2, 20)
         posX = random.randint(1,borneMaxX)
         posY = random.randint(1,borneMaxY)
         while self.game.map[posY][posX].caseBloquante() or self.caseBloquanteAutour(posX, posY):
             posX = random.randint(1,borneMaxX)
             posY = random.randint(1,borneMaxY)
         return posX, posY
          
     def loadSkin(self, nomSkin):
        if nomSkin== "golem_des_forets":
            scale = (704*0.13, 613*0.13)
        skin = pygame.image.load("data/personnages/"+nomSkin+".png")
        skin = pygame.transform.scale(skin, scale)
        return skin

     def takeDamage(self, entier):
        if self.health >0 :
            self.health-=entier
            self.update_health_bar(self.game.fenetre)
        if self.health<=0:
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
     
     
        
        
     def goRight(self):
        self.rect.x+=self.velocity
        
     def goUp(self):
         self.rect.y-=self.velocity
         
     def goDown(self):
         self.rect.y+=self.velocity

     def update_health_bar(self, surface):
        #def la couleur
        infoObject = pygame.display.Info()  #récupère la taille de l'écran

        if self.health >=80 : 
            bar_color = (111, 210, 46)
        elif self.health >=50 : 
            bar_color = (255, 165, 0)
        elif self.health >=25 : 
            bar_color = (255, 69, 0)
        elif self.health >=0 : 
            bar_color = (255, 0, 0)
        else : 
            print("Le "+ self.name+" est MORT !!!")
            bar_color = (255, 0, 0)
        back_bar_color = (60,63,60)
        bar_position = [self.rect.x, self.rect.y-10, self.health, 5]
        back_bar_position = [self.rect.x, self.rect.y-10, self.max_health, 5]
        #dessiner la barre de vie

        pygame.draw.rect(surface, back_bar_color, back_bar_position)
        pygame.draw.rect(surface, bar_color, bar_position)
