###Classe avec TOUT les effets sonnores et musique
import random
import pygame
class Sound():
    def __init__(self):
    #Musiques
    
    
    
    
    #Bruitage
        

        self.trou = pygame.mixer.Sound("data/son/effets/trou.wav")
        self.trou.set_volume(0.05)
        self.mine = pygame.mixer.Sound("data/son/effets/mine.wav")
        self.mine.set_volume(0.05)
        self.scierie = pygame.mixer.Sound("data/son/effets/scierie.wav")
        self.scierie.set_volume(0.05)
        self.moulin = pygame.mixer.Sound("data/son/effets/moulin.wav")
        self.moulin.set_volume(0.05)
        self.trouCreuse = pygame.mixer.Sound("data/son/effets/trouCreuse.wav")
        self.trouCreuse.set_volume(0.05)
        self.fleche = pygame.mixer.Sound("data/son/effets/fleche.wav")
        self.fleche.set_volume(0.05)
        self.vache = pygame.mixer.Sound("data/son/effets/vache.wav")
        self.vache.set_volume(0.05)
        #self.sableMouvant = pygame.mixer.Sound("data/son/effets/sableMouvant.wav")
        self.sableMouvantPassage = pygame.mixer.Sound("data/son/effets/sableMouvantPassage.wav")
        self.sableMouvantPassage.set_volume(0.05)
        self.frigo =  pygame.mixer.Sound("data/son/effets/frigo.wav")
        self.frigo.set_volume(0.05)
        self.ventilo = pygame.mixer.Sound("data/son/effets/ventilo.wav")
        self.ventilo.set_volume(0.05)
        self.incendie = pygame.mixer.Sound("data/son/effets/incendie.wav")
        self.incendie.set_volume(0.05)
        self.tremblement = pygame.mixer.Sound("data/son/effets/tremblement.wav")
        self.tremblement.set_volume(0.05)
        
        self.krakenSpawn = pygame.mixer.Sound("data/son/effets/krakenSpawn.wav")
        self.krakenSpawn.set_volume(0.05)
        self.mageSpawn = pygame.mixer.Sound("data/son/effets/mageSpawn.wav")
        self.mageSpawn.set_volume(0.05)
        self.golem_des_foretsSpawn = pygame.mixer.Sound("data/son/effets/golem_des_foretsSpawn.wav")
        self.golem_des_foretsSpawn.set_volume(0.05)
        self.dragonSpawn = pygame.mixer.Sound("data/son/effets/dragonSpawn.wav")
        self.dragonSpawn.set_volume(0.05)
        self.oursinSpawn = pygame.mixer.Sound("data/son/effets/oursinSpawn.wav")
        self.oursinSpawn.set_volume(0.05)
        self.yetiSpawn = pygame.mixer.Sound("data/son/effets/yetiSpawn.wav")
        self.yetiSpawn.set_volume(0.05)
        
        ###MUSIQUE
        
        self.musiqueCalme1 = pygame.mixer.Sound("data/son/musiques/musique1.mp3")
        self.musiqueCalme1.set_volume(0.1)
        self.musiqueConstruction1 = pygame.mixer.Sound("data/son/musiques/musique2.mp3")
        self.musiqueConstruction1.set_volume(0.1)
        self.musiqueCombat3 = pygame.mixer.Sound("data/son/musiques/musique3.mp3")
        self.musiqueCombat3.set_volume(0.1)
        self.musiqueCombat4 = pygame.mixer.Sound("data/son/musiques/musique4.mp3")
        self.musiqueCombat4.set_volume(0.1)
        self.musiqueCombat2 = pygame.mixer.Sound("data/son/musiques/musique5.mp3")
        self.musiqueCombat2.set_volume(0.1)
        
        self.listeMusiqueCalme = [self.musiqueCalme1]
        self.listeMusiqueConstruction = [self.musiqueConstruction1]
        self.listeMusiqueCombat = [self.musiqueCombat2, self.musiqueCombat3, self.musiqueCombat3, self.musiqueCombat4]
        
        
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