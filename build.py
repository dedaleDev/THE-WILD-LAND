from ctypes.wintypes import RECT
import random
import pygame

from tour import Tour

class Build(pygame.sprite.Sprite):
    def __init__(self, game, nomBatiment, tuile, nbClickMax):
          super().__init__()
          self.game = game
          self.nomBatiment=nomBatiment
          self.tuile = tuile
          self.image=None
          
          self.imageClick=None
          self.actuelClick=None #Endroit ou on doit cliquer
          
          #self.annimClick=game.images.clickBuild
          self.indiceAnnimClick = 0
          
          
          self.nbClick = 0
          self.nbClickMax=nbClickMax
          
          
          self.clockMax=3
          self.clock=0
          self.construireLeBatiment(tuile)
    
    def spawnButton(self):
        posX=random.randint(self.tuile.rect.x, self.tuile.rect.x+200)
        posY=random.randint(self.tuile.rect.y, self.tuile.rect.y+100)
        self.actuelClick=pygame.Rect(posX, posY, 50,50)
        self.indiceAnnimClick=0
    
    
    def checkClick(self):
        mouse= pygame.mouse.get_pos()
        if pygame.Rect.collidepoint(self.actuelClick,mouse[0], mouse[1]):
            self.nbClick+=1
    
    def update(self):
        if self.nbClick==self.nbClickMax:
            self.construireLeBatiment(self.tuile)
            
            
        if self.indiceAnnimClick>=len(self.annimClick):
            self.indiceAnnimClick=-1
        elif self.clock>=self.clockMax:
            self.indiceAnnimClick+=1
            self.self.clock=0
        self.imageClick=self.annimClick[self.indiceAnnimClick]
    
    def construireLeBatiment(self, tuile):
        changerImg = True
        if self.nomBatiment == "scierie":
            self.game.map[tuile.posY][tuile.posX].scierie = True
            self.game.joueur.nbScierie+=1
            self.game.joueur.indiceEcolo+=1
            self.game.listeCaseBatiment.append(tuile)
            tuile.annimation=[]
            pygame.mixer.Sound.play(self.game.son.scierie)
            if tuile.indiceSurbrillance>=0:
                self.game.groupTuileBoost.add(tuile)
            
              
        elif self.nomBatiment == "moulin":
            self.game.map[tuile.posY][tuile.posX].moulin = True
            self.game.joueur.nbMoulin+=1
            self.game.joueur.indiceEcolo+=1
            self.game.listeCaseBatiment.append(tuile)
            tuile.annimation = self.game.images.moulinAnnim
            tuile.clockAnnimMax = 6
            if tuile.indiceSurbrillance>=0:
                self.game.groupTuileBoost.add(tuile)
            pygame.mixer.Sound.play(self.game.son.moulin)
        elif self.nomBatiment == "puit":
            tuile.annimation=[]
            self.game.map[tuile.posY][tuile.posX].puit = True
            self.game.joueur.nbPuit+=1
            self.game.listeCaseBatiment.append(tuile)
        elif self.nomBatiment == "champs":
            tuile.annimation=[]
            self.game.map[tuile.posY][tuile.posX].champs = True
            self.game.joueur.nbChamps+=1
            self.game.listeCaseBatiment.append(tuile)

        elif self.nomBatiment == "elevage":
            tuile.annimation=[]
            self.game.map[tuile.posY][tuile.posX].elevage = True
            self.game.joueur.nbElevage+=1
            self.game.joueur.indiceEcolo+=3
            self.game.listeCaseBatiment.append(tuile)
            tuile.annimation = self.game.images.elevage
            tuile.clockAnnimMax = 10
            pygame.mixer.Sound.play(self.game.son.vache)
        elif self.nomBatiment == "mine":
            tuile.annimation=self.game.images.mineAnnim
            tuile.clockAnnimMax = 6
            self.game.map[tuile.posY][tuile.posX].mine = True
            self.game.joueur.nbMine+=1
            self.game.listeCaseBatiment.append(tuile)
            self.game.joueur.indiceEcolo+=2
            changerImg=False
            pygame.mixer.Sound.play(self.game.son.mine)
            if tuile.indiceSurbrillance>=0:
                self.game.groupTuileBoost.add(tuile)
        elif self.nomBatiment == "port":
            tuile.annimation=[]
            self.game.map[tuile.posY][tuile.posX].port = True
            self.game.joueur.nbPort+=1
            self.game.joueur.indiceEcolo+=2
            self.game.listeCaseBatiment.append(tuile)
        elif self.nomBatiment == "tour":
            tuile.annimation=[]
            self.game.map[tuile.posY][tuile.posX].tour = True
            tour = Tour(self.game, tuile, 1000, "tour", 10, 300)
            self.game.groupDefense.add(tour)
            tuile.tour = tour
        elif self.nomBatiment == "pieux":
            tuile.annimation=[]
            self.game.map[tuile.posY][tuile.posX].pieux = True

        elif self.nomBatiment == "sableMouvant":
            tuile.annimation=[]
            self.game.map[tuile.posY][tuile.posX].sableMouvant = True
            self.game.joueur.indiceEcolo+=10
            #pygame.mixer.Sound.play(self.game.son.sableMouvant)

        elif self.nomBatiment == "mortier":
            tuile.annimation=self.game.images.mortierAnnim
            tuile.clockAnnimMax = 5
            self.game.map[tuile.posY][tuile.posX].mortier = True
            mortier = Tour(self.game, tuile, 1000, "mortier", 20, 300)
            self.game.groupDefense.add(mortier)
            tuile.game.joueur.mortier = mortier
            self.game.joueur.indiceEcolo+=10
            
        elif self.nomBatiment=="trou":
            tuile.annimation=[]
            self.game.map[tuile.posY][tuile.posX].trou = True
            pygame.mixer.Sound.play(self.game.son.trouCreuse, maxtime=900)
            
        elif self.nomBatiment=="frigo": 
            tuile.annimation=[]
            self.game.map[tuile.posY][tuile.posX].frigo = True
            self.game.joueur.nbFrigo+=1
            pygame.mixer.Sound.play(self.game.son.frigo, fade_ms=1000)
            tuile.annimation = self.game.images.frigoAnnim
            tuile.clockAnnimMax = 7
            self.game.joueur.indiceEcolo-=10
        elif self.nomBatiment=="ventilo":
            self.game.map[tuile.posY][tuile.posX].ventilo = True
            tuile.annimation = self.game.images.ventiloAnnim
            tuile.clockAnnimMax = 1
        elif self.nomBatiment=="ville":
            
            self.game.map[tuile.posY][tuile.posX].ville = True
            self.game.joueur.ville=True   
        
        elif self.nomBatiment=="statueEau" or self.nomBatiment=="statueBois" or self.nomBatiment=="statueFood" or self.nomBatiment=="statuePierre":
            if self.nomBatiment=="statueFood":
                self.game.joueur.statueFood=True
            if self.nomBatiment=="statueBois":
                self.game.joueur.statueBois=True
            if self.nomBatiment=="statueEau":
                self.game.joueur.statueEau=True
            if self.nomBatiment=="statuePierre":
                self.game.joueur.statuePierre=True
            self.game.map[tuile.posY][tuile.posX].statue=True
            for y in range(-1,2):
                for x in range(-1,2):
                    
                    if self.game.map[tuile.posY+y][tuile.posX+x].type==self.game.map[tuile.posY][tuile.posX].type and (y!=0 or x!=0):
                        self.game.map[tuile.posY+y][tuile.posX+x].indiceSurbrillance=random.randint(0,200)
                        if self.game.map[tuile.posY+y][tuile.posX+x].scierie or self.game.map[tuile.posY+y][tuile.posX+x].mine or self.game.map[tuile.posY+y][tuile.posX+x].moulin:
                            self.game.groupTuileBoost.add(self.game.map[tuile.posY+y][tuile.posX+x])
            changerImg=False
        elif self.nomBatiment=="forge":
            tuile.annimation=self.game.images.forgeAnnim
            tuile.clockAnnimMax = 6
            self.game.map[tuile.posY][tuile.posX].forge = True
            changerImg=False
        elif self.nomBatiment=="armure1":
            self.game.joueur.nomArmure="armure1"
            self.game.joueur.imageArmure = self.game.images.armure[0]
            self.game.joueur.armure=5
            changerImg=False
        elif self.nomBatiment=="armure2":
            self.game.joueur.nomArmure="armure2"
            self.game.joueur.imageArmure = self.game.images.armure[1]
            self.game.joueur.armure=15
        elif self.nomBatiment=="armure3":
            self.game.joueur.nomArmure="armure3"
            self.game.joueur.imageArmure = self.game.images.armure[2]
            self.game.joueur.armure=25
        elif self.nomBatiment=="armure4":
            self.game.joueur.nomArmure="armure4"
            self.game.joueur.imageArmure = self.game.images.armure[3]
            self.game.joueur.armure=35
        if changerImg:
            self.game.joueur.changerImageBatiment(tuile, self.nomBatiment)
        