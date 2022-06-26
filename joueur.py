from PIL import Image
import pygame
import random
import generation
class Player(pygame.sprite.Sprite):

     def __init__(self, game, nom):
          super().__init__()
          #affichage et information
          self.name = nom
          self.skin = self.loadSkin(nom, (100, 150))
          self.game = game
          self.bateau = False
          self.skinBateau = self.loadSkin("bateau",(100, 150))



          #donnée du joueur
          self.health = 100
          self.velocity = 5
          self.armor = 0
          self.posX, self.posY = self.initPos()
          self.rect = self.skin.get_rect()
          self.rect.x = self.game.map[self.posY][self.posX].rect.x
          self.rect.y = self.game.map[self.posY][self.posX].rect.y - 10

          #ressources du joueur
          self.wood = 200
          self.stone = 100
          self.food = 50
          self.water = 30000
          self.RessourcesTEXT =""
          self.RessourcesInfoModified= ""
          self.ressourcesIMG = self.loadRessourcesIMG()
          self.ancientRessources =(0,0)#type de la dernière ressource actualisé puis sa valeur
          
          #deplacement
        
          self.nombreDecalageRestantX = 0

     def getSkin(self):
         return self.skin
     def getName(self):
         return self.name
     def getHealth(self):
         return self.health   
     def getVelocity(self):
           return self.velocity
     def getArmor(self): 
               return self.armor

     def getWood(self):
           return self.wood
     def getStone(self):
               return self.stone
     def getFood(self):
               return self.food
     def getWater(self):
               return self.water




     def majPos(self):
        tuileSelect = False
        souris = self.rect.x+75, self.rect.y+135
        for i in range(generation.taille_matriceY):
            for j in range(generation.taille_matriceX):
                pos_in_mask = souris[0] - self.game.map[i][j].rect.x, souris[1] - self.game.map[i][j].rect.y
                touching = self.game.map[i][j].rect.collidepoint(souris) and self.game.map[i][j].mask.get_at(pos_in_mask)
                if touching :
                    self.game.map[i][j].setSelect(True)
                    tuileSelect = self.game.map[i][j]
                  
                else :
                    self.game.map[i][j].setSelect(False)
        self.posX=tuileSelect.posX
        self.posY = tuileSelect.posY
        return tuileSelect






     def initPos(self):
         borneMaxX = min(generation.taille_matriceX-2, 15)
         borneMaxY = min(generation.taille_matriceY-2, 5)
         posX = random.randint(1,borneMaxX)
         posY = random.randint(1,borneMaxY)
         while self.game.map[posY][posX].caseBloquante() or self.caseBloquanteAutour(posX, posY):
             posX = random.randint(1,borneMaxX)
             posY = random.randint(1,borneMaxY)
         return posX, posY

     def caseBloquanteAutour(self, posX, posY):
         return self.game.map[posY+1][posX].caseBloquante() and self.game.map[posY-1][posX].caseBloquante() and self.game.map[posY][posX-1].caseBloquante() and self.game.map[posY][posX+1].caseBloquante()


     def resetRessourcesModified(self):
        self.RessourcesInfoModified=[False,False,False,False]

     def setHealth(self, health):
               self.health += health     
     def setVelocity(self, velocity):
               self.velocity += velocity
     def setArmor(self, armor):
               self.armor += armor
     def setFood(self, food):
        if (self.food -food>=0) :
            self.food += food
            self.compteurRessources(modif=food, type=1)
     def setStone(self, stone):
        if (self.stone -stone>=0) :
            self.stone += stone
            self.compteurRessources(modif=stone, type=2)   
     def setWater(self, water):
        if (self.water -water>=0) :
            self.water += water
            self.compteurRessources(modif=water, type=3)   
     def setWood(self, wood):
        if (self.wood -wood>=0) :
            self.wood += wood
            self.compteurRessources(modif=wood, type=4)

     def loadSkin(self, nomSkin, scale):
        skin = pygame.image.load("data/personnages/"+nomSkin+".png")
        skin = pygame.transform.scale(skin, scale)
        return skin
    
    
    
     def deplacementAutorise(self, direction):
         if direction=="droite":
                return not (self.game.map[self.posY][self.posX+1].tuileHaute() or (self.game.map[self.posY][self.posX+1].estMer() and not self.bateau)) #on ne doit pas avoir mer ou montagne
         if direction=="gauche":
            return not (self.game.map[self.posY][self.posX-1].tuileHaute() or (self.game.map[self.posY][self.posX-1].estMer() and not self.bateau))
         if direction=="haut":
             return not (self.game.map[self.posY-1][self.posX].tuileHaute() or (self.game.map[self.posY-1][self.posX].estMer() and not self.bateau))
         if direction=="bas":
             return not (self.game.map[self.posY+1][self.posX].tuileHaute() or (self.game.map[self.posY+1][self.posX].estMer() and not self.bateau))
         if direction=="diagHautDroit":
                return not (self.game.map[self.posY-1][self.posX+1].tuileHaute() or (self.game.map[self.posY-1][self.posX+1].estMer() and not self.bateau))
         if direction=="diagHautGauche":
            return not (self.game.map[self.posY-1][self.posX-1].tuileHaute() or (self.game.map[self.posY-1][self.posX-1].estMer() and not self.bateau))
         if direction=="diagBasGauche":
            return not (self.game.map[self.posY+1][self.posX-1].tuileHaute() or (self.game.map[self.posY+1][self.posX-1].estMer() and not self.bateau))
         if direction=="diagBasDroit":
            return not (self.game.map[self.posY+1][self.posX+1].tuileHaute() or (self.game.map[self.posY+1][self.posX+1].estMer() and not self.bateau))
        
     def goLeft(self):
        self.posX-=1
        if self.posX<1:
            self.posX=1
     
     
        
        
     def goRight(self):
        self.posX+=1
        if self.posX>len(self.game.map[0])-2:
            self.posX=len(self.game.map[0])-2
        
     def goUp(self):
         self.posY-=1
         if self.posY<1:
                self.posY=1
         
     def goDown(self):
         self.posY+=1
         if self.posY>len(self.game.map)-2:
            self.posY=len(self.game.map)-2

     def goDownLeft(self):
         self.goDown()
         self.goLeft()


     def goDownRight(self):
         self.goDown()
         self.goRight()
         
     def goUpRight(self):
        self.goRight()
        self.goUp()

     def goUpLeft(self):
         self.goUp()
         self.goLeft()
         
     def majBateau(self):
         if self.game.map[self.posY][self.posX].type!=3:
             self.bateau=False
         
         
     def loadRessourcesIMG(self):
       
        listeRessourcesSources = ["data/ressources/r_food.png", "data/ressources/r_stone.png", "data/ressources/r_water.png", "data/ressources/r_wood.png"]
        for i in  range (len(listeRessourcesSources)) : 
            listeRessourcesSources[i]= pygame.image.load(listeRessourcesSources[i]).convert_alpha()
            listeRessourcesSources[i]= pygame.transform.scale(listeRessourcesSources[i],( 170,70))
        self.compteurRessources()
        return listeRessourcesSources

     def compteurRessources(self, modif = False,type = None):
        #1 food 
        #2 stone
        #3 water
        #4 wood
        smallfont = pygame.font.SysFont('Corbel', 50)  # definit la police utilisé
        listeRessources=[self.food, self.stone, self.water, self.wood]
        listeRessourcesTEXT=["", "","",""]
        listeRessourcesInfoModified =  [False,False,False,False]
        for i in  range (len(listeRessourcesTEXT)) : 
            listeRessourcesTEXT[i]=smallfont.render(str(listeRessources[i]), True, (0,0,0))
        if modif != False and type != None and modif<0:
            if self.ancientRessources[0]==type and self.ancientRessources[1]<=50:
                calcul = modif + self.ancientRessources[1]
                #print("Calculating", calcul, self.ancientRessources)
            else :
                calcul =modif
            self.ancientRessources=(type,calcul)
            listeRessourcesInfoModified[type]=smallfont.render(str(calcul), True, (255,255,255))
            
        self.RessourcesInfoModified=listeRessourcesInfoModified
        self.RessourcesTEXT= listeRessourcesTEXT
        
        return
    
    
    ####        CONSTRUCTION        ####
    
     def construireScierie(self, tuile):
        self.game.map[tuile.posY][tuile.posX].scierie = True
     
     def changerImageScierie(self, tuile):
          imgTemp = Image.open("data/batiments/scierie.png").convert('RGBA')

          self.game.map[tuile.posY][tuile.posX].imageO = imgTemp.resize((150, 150))