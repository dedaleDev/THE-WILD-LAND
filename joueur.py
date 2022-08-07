#from PIL import Image
import pygame
import random
from selection import majSelectionJoueur
import generation
from tour import Tour
class Player(pygame.sprite.Sprite):

     def __init__(self, game, nom, vitesse):
          super().__init__()
          #affichage et information
          self.name = nom
          self.skin = self.loadSkin(nom)
          self.game = game
          self.bateau = False
          self.skinBateau = self.loadSkin("bateau")
          self.skinMask = pygame.mask.from_surface(self.skin)



          #donnée du joueur
          self.health = 100
          self.max_health=100
          self.velocity = vitesse
          self.armor = 0
          self.posX, self.posY = self.initPos()
          self.rect = self.skin.get_rect()
          self.rect.x = self.game.map[self.posY][self.posX].rect.x+40
          self.rect.y = self.game.map[self.posY][self.posX].rect.y
          self.estMort=False
          self.ville=False
          #ressources du joueur
          self.wood = 3000#350
          self.stone =1000#150
          self.food = 1000#50
          self.water = 1000#100
          self.RessourcesTEXT =""
          self.RessourcesInfoModified= ""
          self.ressourcesIMG = self.loadRessourcesIMG()
          self.ancientRessources =(0,0)#type de la dernière ressource actualisé puis sa valeur
          
          self.nbScierie = 0
          self.nbMoulin = 0
          self.nbMine = 0
          self.nbPort = 0
          self.nbElevage=0
          self.nbChamps=0
          self.nbFrigo=0
          
          
          self.listeTour=[]
          
          self.cooldownDamage = 500
          self.lastDamage = 0
          
          self.indiceEcolo=0
          self.MaxEcolo=100
          #deplacement
        


     def getFeet(self):
         return self.rect.x+35, self.rect.y+120

     def takeDamage(self, entier):
        if self.health >=0 :
            self.health-=entier
            self.update_health_bar()
        else :
            self.estMort=True

            
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
    
     def setRessource(self, Wood, Stone, Food, Water):
         return self.setFood(Food) and self.setWood(Wood) and self.setStone(Stone) and self.setWater(Water)
    
     
     
     def initPos(self):
         borneMaxX = min(generation.taille_matriceX-2, 9)
         borneMaxY = min(generation.taille_matriceY-2, 9)
         posX = random.randint(6,borneMaxX)
         posY = random.randint(6,borneMaxY)
         while self.game.map[posY][posX].caseBloquante() or self.caseBloquanteAutour(posX, posY):
             posX = random.randint(6,borneMaxX)
             posY = random.randint(6,borneMaxY)
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
        if (self.food +food>=0) :
            self.food += food
            self.compteurRessources(modif=food, type=1)
            return True
        return False
    
     def setStone(self, stone):
        if (self.stone + stone>=0) :
            self.stone += stone
            self.compteurRessources(modif=stone, type=2)
            return True
        return False
            
     def setWater(self, water):
        if (self.water + water>=0) :
            self.water += water
            self.compteurRessources(modif=water, type=3)
            return True
        return False
     def setWood(self, wood):
        if (self.wood + wood>=0) :
            self.wood += wood
            self.compteurRessources(modif=wood, type=4)
            return True
        return False

     def loadSkin(self, nomSkin):
        if nomSkin=="joueur_1" or nomSkin=="joueur1-2":
            scale = (472*0.13, 978*0.13)
        elif nomSkin=="bateau":
            scale= (512*0.2, 512*0.2)
        else:
            scale = (472*0.13, 978*0.13)
        skin = pygame.image.load("data/personnages/"+nomSkin+".png")
        skin = pygame.transform.scale(skin, scale)
        return skin
    
    
    
     def deplacementAutorise(self, direction):
         if direction=="bas":
             tuile = majSelectionJoueur(self.game, (self.getFeet()[0], self.getFeet()[1]+self.velocity))
         if direction=="droite":
            tuile = majSelectionJoueur(self.game, (self.getFeet()[0]+self.velocity, self.getFeet()[1]))
            
         if direction=="gauche":
            tuile = majSelectionJoueur(self.game, (self.getFeet()[0]-self.velocity, self.getFeet()[1]))
            
         if direction=="haut":
            tuile = majSelectionJoueur(self.game, (self.getFeet()[0], self.getFeet()[1]-self.velocity))
            
         
         if tuile:
            if self.tuileInterdit(tuile): #gestion de deplacement entre 2 cases
                if direction=="bas":
                    tuile = majSelectionJoueur(self.game, (self.getFeet()[0], self.getFeet()[1]+self.velocity+30))
                    
                if direction=="droite":
                    tuile = majSelectionJoueur(self.game, (self.getFeet()[0]+self.velocity+70, self.getFeet()[1]))
            
                if direction=="gauche":
                    tuile = majSelectionJoueur(self.game, (self.getFeet()[0]-self.velocity-70, self.getFeet()[1]))
                    
                if direction=="haut":
                    tuile = majSelectionJoueur(self.game, (self.getFeet()[0], self.getFeet()[1]-self.velocity-30))
                    
            
            return not self.tuileInterdit(tuile)
        
         else:
             print("erreur dans fonction joueur.deplacement autorisé")
             return False
         
         
     def tuileInterdit(self, tuile):
         return tuile.tuileHaute() or (tuile.estMer() and tuile.pasPort() and not self.bateau) or (not tuile.estMer() and tuile.pasPort() and self.bateau)
         


     def setPos(self, tuile):
        self.posX, self.posY = tuile.posX, tuile.posY

     def goLeft(self):
            self.skin = self.loadSkin("joueur1-2")
            self.rect.x-=self.velocity
     
     
        
        
     def goRight(self):
        self.skin = self.loadSkin("joueur_1")
        self.rect.x+=self.velocity
        
     def goUp(self):
         self.rect.y-=self.velocity
         
     def goDown(self):
         self.rect.y+=self.velocity

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
        if not modif and type and modif<0:
            if self.ancientRessources[0]==type and self.ancientRessources[1]<=50:
                calcul = modif + self.ancientRessources[1]
                #print("Calculating", calcul, self.ancientRessources)
            else :
                calcul = modif
            self.ancientRessources=(type,calcul)
            listeRessourcesInfoModified[type]=smallfont.render(str(calcul), True, (255,255,255))
            
        self.RessourcesInfoModified=listeRessourcesInfoModified
        self.RessourcesTEXT= listeRessourcesTEXT
        
        return
    
    
    ####        CONSTRUCTION        ####
    
     def majCout(self, item):
        if self.wood - item.coutWood >=0 and self.food - item.coutFood >=0 and self.stone - item.coutStone >=0 and self.water - item.coutWater >=0:
            self.setFood(-item.coutFood)
            self.setWood(-item.coutWood) 
            self.setStone(-item.coutStone) 
            self.setWater(-item.coutWater)
            return True
        
        return False
        
    
    
    
     def construireBatiment(self, tuile, item):
        if not self.majCout(item):
            return False
        
        if item.nom == "scierie":
            self.game.map[tuile.posY][tuile.posX].scierie = True
            self.nbScierie+=1
            self.indiceEcolo+=1
            self.game.listeCaseBatiment.append(tuile)
            pygame.mixer.Sound.play(self.game.son.scierie)
        
              
        elif item.nom == "moulin":
            self.game.map[tuile.posY][tuile.posX].moulin = True
            self.nbMoulin+=1
            self.indiceEcolo+=1
            self.game.listeCaseBatiment.append(tuile)
            pygame.mixer.Sound.play(self.game.son.moulin)
        elif item.nom == "puit":
            self.game.map[tuile.posY][tuile.posX].puit = True
            self.nbPuit+=1
            self.game.listeCaseBatiment.append(tuile)
        elif item.nom == "champs":
            self.game.map[tuile.posY][tuile.posX].champs = True
            self.nbChamps+=1
            self.game.listeCaseBatiment.append(tuile)

        elif item.nom == "elevage":
            self.game.map[tuile.posY][tuile.posX].elevage = True
            self.nbElevage+=1
            self.indiceEcolo+=3
            self.game.listeCaseBatiment.append(tuile)
            pygame.mixer.Sound.play(self.game.son.vache)
        elif item.nom == "mine":
            self.game.map[tuile.posY][tuile.posX].mine = True
            self.nbMine+=1
            self.game.listeCaseBatiment.append(tuile)
            self.indiceEcolo+=2
            pygame.mixer.Sound.play(self.game.son.mine)
        elif item.nom == "port":
            self.game.map[tuile.posY][tuile.posX].port = True
            self.nbPort+=1
            self.indiceEcolo+=2
            self.game.listeCaseBatiment.append(tuile)
        elif item.nom == "tour":
            self.game.map[tuile.posY][tuile.posX].tour = True
            tour = Tour(self.game, tuile, 1000, "tour", 10, 300)
            self.game.groupDefense.add(tour)
            tuile.tour = tour
        elif item.nom == "pieux":
            self.game.map[tuile.posY][tuile.posX].pieux = True

        elif item.nom == "sableMouvant":
            self.game.map[tuile.posY][tuile.posX].sableMouvant = True
            self.indiceEcolo+=10
            #pygame.mixer.Sound.play(self.game.son.sableMouvant)

        elif item.nom == "mortier":
            self.game.map[tuile.posY][tuile.posX].mortier = True
            mortier = Tour(self.game, tuile, 1000, "mortier", 20, 300)
            self.game.groupDefense.add(mortier)
            tuile.mortier = mortier
            self.indiceEcolo+=10
        elif item.nom=="trou":
            self.game.map[tuile.posY][tuile.posX].trou = True
            pygame.mixer.Sound.play(self.game.son.trouCreuse, maxtime=900)
            
        elif item.nom=="frigo": 
            self.game.map[tuile.posY][tuile.posX].frigo = True
            self.nbFrigo+=1
            pygame.mixer.Sound.play(self.game.son.frigo, fade_ms=1000)
            self.indiceEcolo-=10
        elif item.nom=="ventilo":
            self.game.map[tuile.posY][tuile.posX].ventilo = True
        elif item.nom=="ville":
            self.game.map[tuile.posY][tuile.posX].ville = True
            self.ville=True        
            
            
            
            
        self.changerImageBatiment(tuile, item.nom)
        
        
            

        return True
    
     def detruireBatimentRessource(self, tuile):
         
         if tuile.champs:
            tuile.champs=False
            self.nbChamps-=1
         if tuile.elevage:
            tuile.elevage=False
            self.nbElevage-=1
         if tuile.mine:
            tuile.mine=False
            self.nbMine-=1
         if tuile.moulin:   
            tuile.moulin=False
            self.nbMoulin-=1
         if tuile.scierie:
             tuile.scierie=False
             self.nbScierie-=1
         if tuile.port:
            tuile.port=False
            self.nbPort-=1
         if tuile.pieux:
             tuile.pieux=False
         tuile.image= self.game.images.returnImg(tuile.type)
         #tuile.imageO=self.game.images.returnImgO(tuile.type)
         tuile.aEteModifie=True

         return tuile

     def chargerImPort(self, tuile, supX=0, supY=0): #sup = variable pour simuler un decalage joueur
         ecartX = tuile.posX-self.posX-supX
         ecartY = tuile.posY-self.posY-supY
         if ecartX==0 and ecartY == 1:
             imgTemp2 = pygame.image.load("data/batiments/port/port2.png").convert_alpha()
         if ecartX==-1 and ecartY == 0:
             imgTemp2 = pygame.image.load("data/batiments/port/port3.png").convert_alpha()
         if ecartX==0 and ecartY == -1:
             imgTemp2 = pygame.image.load("data/batiments/port/port1.png").convert_alpha()
         if ecartX == 1 and ecartY == 0:
             imgTemp2 = pygame.image.load("data/batiments/port/port0.png").convert_alpha()
         if ecartX == 1 and ecartY == -1:
             imgTemp2 = pygame.image.load("data/batiments/port/port"+str(random.randint(0,1))+".png").convert_alpha()
         if ecartX == -1 and ecartY == 1:
             imgTemp2 = pygame.image.load("data/batiments/port/port"+str(random.randint(2,3))+".png").convert_alpha()
         if ecartX == 1 and ecartY == 1:
             imgTemp2 = pygame.image.load("data/batiments/port/port"+str(random.choice([0,2]))+".png").convert_alpha()
         if ecartX == -1 and ecartY == -1:
             imgTemp2 = pygame.image.load("data/batiments/port/port"+str(random.choice([1,3]))+".png").convert_alpha()
         if ecartX == 0 and ecartY == 0:
             listeEcart=[]
             for i in range(-1,2):
                 for j in range(-1,2):
                     if (i!=0 or j!=0) and not self.game.map[tuile.posY+i][tuile.posX+j].caseBloquante():
                        listeEcart.append((i,j))
             for i,j in listeEcart:
                 if i==0 or j==0:

                    return self.chargerImPort(tuile, supX=j, supY=i)
             i,j = listeEcart[0]

             return self.chargerImPort(tuile, supX=j, supY=i)
         return imgTemp2

     def changerImageBatiment(self, tuile, nom):
          if nom=="port":
              imgTemp = self.chargerImPort(tuile)
              
          else:
              #imgTempO = Image.open("data/batiments/"+nom+".png").convert('RGBA')
              imgTemp = pygame.image.load("data/batiments/"+nom+".png").convert_alpha()
          #tuile.imageO = imgTempO.resize((246, 144))
          if nom != "ville" :
            tuile.image = pygame.transform.scale(imgTemp,(246, 144))
        
          tuile.aEteModifie=True

     def ajouterRessources(self):

         self.setWood(5*self.nbScierie)
         self.setStone(4*self.nbMine)
         #self.setWater(1*self.nbPuit)
         self.setWater(3*self.nbMoulin)
         self.setFood(4*self.nbElevage + 1*self.nbChamps)
         self.indiceEcolo-=self.nbFrigo*0.5
     def update_health_bar(self):
        #def la couleur
        

        if self.health >=80 : 
            bar_color = (111, 210, 46)
        elif self.health >=50 : 
            bar_color = (255, 165, 0)
        elif self.health >=25 : 
            bar_color = (255, 69, 0)
        elif self.health >=0 : 
            bar_color = (255, 0, 0)
        else : 
            bar_color = (255, 0, 0)
        back_bar_color = (60,63,60)
        bar_position = [160, 20, self.health*3, 40]
        back_bar_position = [160, 20, self.max_health*3, 40]
        #dessiner la barre de vie
        
        pygame.draw.rect(self.game.fenetre, back_bar_color, back_bar_position)
        pygame.draw.rect(self.game.fenetre, bar_color, bar_position)
        
     def update_ecolo_bar(self):
        
        if self.indiceEcolo >=80 : 
            bar_color = (255, 0, 0)
        elif self.indiceEcolo >=50 : 
            bar_color = (255, 69, 0)
        elif self.indiceEcolo >=25 : 
            bar_color = (255, 165, 0)
        else :
            bar_color = (111, 210, 46)

        back_bar_color = (60,63,60)
        bar_position = [20, 200, 30, self.MaxEcolo*2-self.indiceEcolo*2]
        back_bar_position = [20, 200, 30, self.MaxEcolo*2]
        #dessiner la barre de vie
        
        pygame.draw.rect(self.game.fenetre, back_bar_color, back_bar_position)
        pygame.draw.rect(self.game.fenetre, bar_color, bar_position)