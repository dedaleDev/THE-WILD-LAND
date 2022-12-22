
import random
import time
import pygame
import tuto

from tour import Tour

class Build(pygame.sprite.Sprite):
    def __init__(self, game, nomBatiment, tuile, nbClickMax):
          nbClickMax=nbClickMax
          super().__init__()
          tuile.build=True
          self.game = game
          self.nomBatiment=nomBatiment
          self.tuile = tuile
          self.image=None
          #self.image=pygame.transform.scale(self.image, (self.image.get_width()*1.5, self.image.get_height()*1.5))
          self.imageClickPassif=None
          self.actuelClick=None #Endroit ou on doit cliquer
          
          self.moveBox = game.images.moveBox
          self.indiceBox = -1
          
          self.annimClick=game.images.clickBuild
          self.indiceAnnimClick = 0
          self.rect=tuile.rect
          
          self.boomBox = game.images.boomBox
          self.indiceBoomBox = -1
          
          self.nbClick = 0
          self.nbClickMax=nbClickMax
          
          self.posXclick = 0
          self.posYclick=0
          
          
          self.clockMax=3
          self.clock=0
          self.clockBox = 0
          self.clockBoxMax = 1
          
          if self.nomBatiment=="statueFood":
                self.game.joueur.statueFood=True
          if self.nomBatiment=="statueBois":
                    self.game.joueur.statueBois=True
          if self.nomBatiment=="statueEau":
                    self.game.joueur.statueEau=True
          if self.nomBatiment=="statuePierre":
                    self.game.joueur.statuePierre=True

          if self.nomBatiment=="sableMouvant":
                    tuto.upadateStatutTuto(game,"sable")
    
    def spawnButton(self):
        #pygame.draw.rect(self.game.fenetre, (255,255,255), (self.tuile.rect.x, self.tuile.rect.y, 256,144), 1)
        i=0
        
        #while i<400:
        y=random.randint(-100, 146)
        x=random.randint(10, 234)
        hauteurCaisse=300
        basCaisse = -55
        while not (y<0.6*x+81+basCaisse and y<-0.6*x+231+basCaisse and y>0.6*x-70-hauteurCaisse and y >-0.6*x+80-hauteurCaisse):
            y=random.randint(-100, 146)
            x=random.randint(10, 234)
            #pygame.draw.circle(self.game.fenetre, (255,255,255), (self.tuile.rect.x+x,self.tuile.rect.y+y), 1)
            #pygame.draw.rect(self.game.fenetre, (255,255,255), (self.tuile.rect.x+x-20,self.tuile.rect.y+y-20, 40,40), width=1)
            #pygame.display.flip()
            #i+=1
        #time.sleep(3)
        self.posYclick=y
        self.posXclick=x
        self.actuelClick=pygame.Rect(self.posXclick-20, self.posYclick-20, 40,40)
        
        self.indiceAnnimClick=0
    
    
    def checkClick(self):
        mouse= pygame.mouse.get_pos()
        if self.actuelClick:
            
            if pygame.Rect.collidepoint(self.actuelClick,mouse[0], mouse[1]):
                self.nbClick+=1
                self.actuelClick=None
                self.indiceBox=0
                return True
        return False
    
    
    def update(self):
        if self.actuelClick==None and self.nbClick<self.nbClickMax :
            self.spawnButton()
        if self.actuelClick:
            self.actuelClick.x=self.tuile.rect.x+self.posXclick
            self.actuelClick.y = self.tuile.rect.y+self.posYclick
        
        
        if self.nbClick>=self.nbClickMax:
            self.indiceBoomBox+=1
            if self.indiceBoomBox>=len(self.boomBox):
                
                self.kill() # pauvre build :(
                return
            if self.indiceBoomBox==12:
                
                self.construireLeBatiment(self.tuile)
            self.image=self.boomBox[self.indiceBoomBox]
            
        elif self.clock>=self.clockMax:
            self.indiceAnnimClick+=1
            self.clock=0
            
        if self.clockBox>=self.clockBoxMax:
            if self.indiceBox>=0:    
                self.indiceBox+=1
            self.clockBox=0
        if self.indiceAnnimClick>=len(self.annimClick):
            self.indiceAnnimClick=0
        if self.indiceBox>=len(self.moveBox):
            self.indiceBox=-1
        self.imageClickPassif=self.annimClick[self.indiceAnnimClick]
        if self.indiceBoomBox==-1:
            self.image = self.moveBox[self.indiceBox]
        self.clock+=1
        self.clockBox+=1
        
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
            tuile.clockAnnimMax = 2
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
            mortier = Tour(self.game, tuile, 1000, "mortier", 40, 300)
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
            
            self.game.map[tuile.posY][tuile.posX].statue=True
            for y in range(-1,2):
                for x in range(-1,2):
                    
                    if self.game.map[tuile.posY+y][tuile.posX+x].type==self.game.map[tuile.posY][tuile.posX].type and (y!=0 or x!=0):

                        self.game.map[tuile.posY+y][tuile.posX+x].indiceSurbrillance=random.randint(0,200)
                        print("ini indice surbri=", self.game.map[tuile.posY+y][tuile.posX+x].indiceSurbrillance)
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
        elif self.nomBatiment=="marteau1":
            self.game.joueur.nomProj = "marteau1"
            self.game.joueur.damageDistance=8
            changerImg=False
        elif self.nomBatiment=="marteau2":
            self.game.joueur.nomProj = "marteau2"
            self.game.joueur.damageDistance=16
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
            self.game.joueur.health*=1.2
        if changerImg:
            self.game.joueur.changerImageBatiment(tuile, self.nomBatiment)
        self.tuile.build=False
        
        