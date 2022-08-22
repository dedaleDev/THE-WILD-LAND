###Classe avec TOUT les effets sonnores et musique
import csv
import random
import pygame
import csv
import aideCSV
class Sound():
    def __init__(self):
    
    #Bruitage
        volumeBruitage = float(aideCSV.valCorrespondante("volumeBruitage"))
        volumeMusique = float(aideCSV.valCorrespondante("volumeMusique"))
        
        self.trou = pygame.mixer.Sound("data/son/effets/trou.wav")
        self.trou.set_volume(volumeBruitage)
        self.mine = pygame.mixer.Sound("data/son/effets/mine.wav")
        self.mine.set_volume(volumeBruitage)
        self.scierie = pygame.mixer.Sound("data/son/effets/scierie.wav")
        self.scierie.set_volume(volumeBruitage)
        self.moulin = pygame.mixer.Sound("data/son/effets/moulin.wav")
        self.moulin.set_volume(volumeBruitage)
        self.trouCreuse = pygame.mixer.Sound("data/son/effets/trouCreuse.wav")
        self.trouCreuse.set_volume(volumeBruitage)
        self.fleche = pygame.mixer.Sound("data/son/effets/fleche.wav")
        self.fleche.set_volume(volumeBruitage)
        self.vache = pygame.mixer.Sound("data/son/effets/vache.wav")
        self.vache.set_volume(volumeBruitage)
        #self.sableMouvant = pygame.mixer.Sound("data/son/effets/sableMouvant.wav")
        self.sableMouvantPassage = pygame.mixer.Sound("data/son/effets/sableMouvantPassage.wav")
        self.sableMouvantPassage.set_volume(volumeBruitage)
        self.frigo =  pygame.mixer.Sound("data/son/effets/frigo.wav")
        self.frigo.set_volume(volumeBruitage)
        self.ventilo = pygame.mixer.Sound("data/son/effets/ventilo.wav")
        self.ventilo.set_volume(volumeBruitage)
        self.incendie = pygame.mixer.Sound("data/son/effets/incendie.wav")
        self.incendie.set_volume(volumeBruitage)
        self.tremblement = pygame.mixer.Sound("data/son/effets/tremblement.wav")
        self.tremblement.set_volume(volumeBruitage)
        
        self.krakenSpawn = pygame.mixer.Sound("data/son/effets/krakenSpawn.wav")
        self.krakenSpawn.set_volume(volumeBruitage)
        self.mageSpawn = pygame.mixer.Sound("data/son/effets/mageSpawn.wav")
        self.mageSpawn.set_volume(volumeBruitage)
        self.golem_des_foretsSpawn = pygame.mixer.Sound("data/son/effets/golem_des_foretsSpawn.wav")
        self.golem_des_foretsSpawn.set_volume(volumeBruitage)
        self.dragonSpawn = pygame.mixer.Sound("data/son/effets/dragonSpawn.wav")
        self.dragonSpawn.set_volume(volumeBruitage)
        self.oursinSpawn = pygame.mixer.Sound("data/son/effets/oursinSpawn.wav")
        self.oursinSpawn.set_volume(volumeBruitage)
        self.yetiSpawn = pygame.mixer.Sound("data/son/effets/yetiSpawn.wav")
        self.yetiSpawn.set_volume(volumeBruitage)
        
        ###MUSIQUE
        
        self.m1_0 = pygame.mixer.Sound("data/son/1_0.mp3")
        self.m1_0.set_volume(volumeMusique)
        self.m1_1 = pygame.mixer.Sound("data/son/1_1.mp3")
        self.m1_1.set_volume(volumeMusique)
        self.m1_2 = pygame.mixer.Sound("data/son/1_2.mp3")
        self.m1_2.set_volume(volumeMusique)
        self.m1_3 = pygame.mixer.Sound("data/son/1_3.mp3")
        self.m1_3.set_volume(volumeMusique)
        self.m2_0 = pygame.mixer.Sound("data/son/2_0.mp3")
        self.m2_0.set_volume(volumeMusique)
        self.m2_1 = pygame.mixer.Sound("data/son/2_1.mp3")
        self.m2_1.set_volume(volumeMusique)
        self.m2_2 = pygame.mixer.Sound("data/son/2_2.mp3")
        self.m2_2.set_volume(volumeMusique)
        self.m2_3 = pygame.mixer.Sound("data/son/2_3.mp3")
        self.m2_3.set_volume(volumeMusique)
        self.m3_0 = pygame.mixer.Sound("data/son/3_0.mp3")
        self.m3_0.set_volume(volumeMusique)
        self.m3_1 = pygame.mixer.Sound("data/son/3_1.mp3")
        self.m3_1.set_volume(volumeMusique)
        self.m3_2 = pygame.mixer.Sound("data/son/3_2.mp3")
        self.m3_2.set_volume(volumeMusique)
        self.m3_3 = pygame.mixer.Sound("data/son/3_3.mp3")
        self.m3_3.set_volume(volumeMusique)


        
        self.listeMusiqueCalme = [self.m1_0, self.m1_1, self.m1_2, self.m1_3]
        self.listeMusiqueConstruction = [self.m2_0, self.m2_1, self.m2_2, self.m2_3]
        self.listeMusiqueCombat = [self.m3_0, self.m3_1, self.m3_2, self.m3_3]
        
        
        #taille de base des listes
        self.tailleListeMusiqueCalme = len(self.listeMusiqueCalme)
        self.tailleListeMusiqueConstruction = len(self.listeMusiqueConstruction)
        self.tailleListeMusiqueCombat = len(self.listeMusiqueCombat)
    #Delay entre son
        self.dernierVentilo = 0
        self.dernierSable = 0

    def jouerMusique(self):
        if not pygame.mixer.get_busy():
            print("je lance musique")
            if len(self.listeMusiqueCalme)==self.tailleListeMusiqueCalme and len(self.listeMusiqueCalme)>0:
                i=random.randint(0, len(self.listeMusiqueCalme)-1)
                
                pygame.mixer.Sound.play(self.listeMusiqueCalme[i])
                self.listeMusiqueCalme.pop(i)
                
            elif len(self.listeMusiqueConstruction)>=self.tailleListeMusiqueConstruction-1 and len(self.listeMusiqueConstruction)>0:
                
                i=random.randint(0, len(self.listeMusiqueConstruction)-1)
                pygame.mixer.Sound.play(self.listeMusiqueConstruction[i])
                self.listeMusiqueConstruction.pop(i)
                
            elif len(self.listeMusiqueCombat)>=self.tailleListeMusiqueCombat-2 and len(self.listeMusiqueCombat)>0:
                i=random.randint(0, len(self.listeMusiqueCombat)-1)
                pygame.mixer.Sound.play(self.listeMusiqueCombat[i])
                self.listeMusiqueCombat.pop(i)
