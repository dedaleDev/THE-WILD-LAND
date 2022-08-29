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
        
        self.trou = pygame.mixer.Sound("data/son/effets/trou.mp3")
        self.trou.set_volume(volumeBruitage)
        self.mine = pygame.mixer.Sound("data/son/effets/mine.mp3")
        self.mine.set_volume(volumeBruitage)
        self.scierie = pygame.mixer.Sound("data/son/effets/scierie.mp3")
        self.scierie.set_volume(volumeBruitage)
        self.moulin = pygame.mixer.Sound("data/son/effets/moulin.mp3")
        self.moulin.set_volume(volumeBruitage)
        self.trouCreuse = pygame.mixer.Sound("data/son/effets/trouCreuse.mp3")
        self.trouCreuse.set_volume(volumeBruitage)
        self.fleche = pygame.mixer.Sound("data/son/effets/fleche.mp3")
        self.fleche.set_volume(volumeBruitage)
        self.vache = pygame.mixer.Sound("data/son/effets/vache.mp3")
        self.vache.set_volume(volumeBruitage)
        self.coffre = pygame.mixer.Sound("data/son/effets/coffre.mp3")
        self.coffre.set_volume(volumeBruitage)
        self.coffreOuverture = pygame.mixer.Sound("data/son/effets/coffreOuverture.mp3")
        self.coffreOuverture.set_volume(volumeBruitage)
        self.sableMouvantPassage = pygame.mixer.Sound("data/son/effets/sableMouvantPassage.mp3")
        self.sableMouvantPassage.set_volume(volumeBruitage)
        self.frigo =  pygame.mixer.Sound("data/son/effets/frigo.mp3")
        self.frigo.set_volume(volumeBruitage)
        self.ventilo = pygame.mixer.Sound("data/son/effets/ventilo.mp3")
        self.ventilo.set_volume(volumeBruitage)
        self.incendie = pygame.mixer.Sound("data/son/effets/incendie.mp3")
        self.incendie.set_volume(volumeBruitage)
        self.tremblement = pygame.mixer.Sound("data/son/effets/tremblement.mp3")
        self.tremblement.set_volume(volumeBruitage)
        
        self.krakenSpawn = pygame.mixer.Sound("data/son/effets/krakenSpawn.mp3")
        self.krakenSpawn.set_volume(volumeBruitage)
        self.mageSpawn = pygame.mixer.Sound("data/son/effets/mageSpawn.mp3")
        self.mageSpawn.set_volume(volumeBruitage)
        self.golem_des_foretsSpawn = pygame.mixer.Sound("data/son/effets/golem_des_foretsSpawn.mp3")
        self.golem_des_foretsSpawn.set_volume(volumeBruitage)
        self.dragonSpawn = pygame.mixer.Sound("data/son/effets/dragonSpawn.mp3")
        self.dragonSpawn.set_volume(volumeBruitage)
        self.oursinSpawn = pygame.mixer.Sound("data/son/effets/oursinSpawn.mp3")
        self.oursinSpawn.set_volume(volumeBruitage)
        self.yetiSpawn = pygame.mixer.Sound("data/son/effets/yetiSpawn.mp3")
        self.yetiSpawn.set_volume(volumeBruitage)
        
        ###MUSIQUE
        
        self.musiqueCalme1 = pygame.mixer.Sound("data/son/musiques/musique1.mp3")
        self.musiqueCalme1.set_volume(volumeMusique)
        self.musiqueConstruction1 = pygame.mixer.Sound("data/son/musiques/musique2.mp3")
        self.musiqueConstruction1.set_volume(volumeMusique)
        self.musiqueCombat3 = pygame.mixer.Sound("data/son/musiques/musique3.mp3")
        self.musiqueCombat3.set_volume(volumeMusique)
        self.musiqueCombat4 = pygame.mixer.Sound("data/son/musiques/musique4.mp3")
        self.musiqueCombat4.set_volume(volumeMusique)
        self.musiqueCombat2 = pygame.mixer.Sound("data/son/musiques/musique5.mp3")
        self.musiqueCombat2.set_volume(volumeMusique)

        self.listeMusiqueCalme = [self.musiqueCalme1]
        self.listeMusiqueConstruction = [self.musiqueConstruction1]
        self.listeMusiqueCombat = [self.musiqueCombat2, self.musiqueCombat3, self.musiqueCombat3, self.musiqueCombat4]

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
        
        self.listeMusiqueCalme2 = [self.m1_0, self.m1_1, self.m1_2, self.m1_3]
        self.listeMusiqueConstruction2 = [self.m2_0, self.m2_1, self.m2_2, self.m2_3]
        self.listeMusiqueCombat2 = [self.m3_0, self.m3_1, self.m3_2, self.m3_3]
        
        #taille de base des listes
        self.tailleListeMusiqueCalme = len(self.listeMusiqueCalme)
        self.tailleListeMusiqueConstruction = len(self.listeMusiqueConstruction)
        self.tailleListeMusiqueCombat = len(self.listeMusiqueCombat)
        
        self.tailleListeMusiqueCalme2 = len(self.listeMusiqueCalme2)
        self.tailleListeMusiqueConstruction2 = len(self.listeMusiqueConstruction2)
        self.tailleListeMusiqueCombat2 = len(self.listeMusiqueCombat2)
    #Delay entre son
        self.dernierVentilo = 0
        self.dernierSable = 0
        
        
        
        
    def stop(self):
        pygame.mixer.pause()
        
    def jouerMusique(self):
        if not pygame.mixer.get_busy():
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
                
                
            elif self.listeMusiqueCombat==0:
                self.listeMusiqueCombat = [self.musiqueCombat2, self.musiqueCombat3, self.musiqueCombat3, self.musiqueCombat4]
                
    def jouerMusique2(self):
        if not pygame.mixer.get_busy():
            if len(self.listeMusiqueCalme2)==self.tailleListeMusiqueCalme2 and len(self.listeMusiqueCalme2)>0:
                i=random.randint(0, len(self.listeMusiqueCalme2)-1)
                
                pygame.mixer.Sound.play(self.listeMusiqueCalme2[i])

                self.listeMusiqueCalme2.pop(i)
                
            elif len(self.listeMusiqueConstruction2)>=self.tailleListeMusiqueConstruction2-1 and len(self.listeMusiqueConstruction2)>0:
                
                i=random.randint(0, len(self.listeMusiqueConstruction2)-1)
                pygame.mixer.Sound.play(self.listeMusiqueConstruction2[i])
                self.listeMusiqueConstruction2.pop(i)
                
            elif len(self.listeMusiqueCombat2)>=self.tailleListeMusiqueCombat2-2 and len(self.listeMusiqueCombat2)>0:
                i=random.randint(0, len(self.listeMusiqueCombat2)-1)
                pygame.mixer.Sound.play(self.listeMusiqueCombat2[i])
                self.listeMusiqueCombat2.pop(i)
                
                
            elif self.listeMusiqueCombat==0:
                self.listeMusiqueCombat = [self.musiqueCombat2, self.musiqueCombat3, self.musiqueCombat3, self.musiqueCombat4]