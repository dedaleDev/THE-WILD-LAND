###Classe avec TOUT les effets sonnores et musique
import pygame
class Sound():
    def __init__(self):
    #Musiques
    
    
    
    
    #Bruitage
    

        self.trou = pygame.mixer.Sound("data/son/effets/trou.wav")
        self.mine = pygame.mixer.Sound("data/son/effets/mine.wav")
        self.scierie = pygame.mixer.Sound("data/son/effets/scierie.wav")
        self.moulin = pygame.mixer.Sound("data/son/effets/moulin.wav")
        self.trouCreuse = pygame.mixer.Sound("data/son/effets/trouCreuse.wav")
        self.fleche = pygame.mixer.Sound("data/son/effets/fleche.wav")
        self.vache = pygame.mixer.Sound("data/son/effets/vache.wav")
        #self.sableMouvant = pygame.mixer.Sound("data/son/effets/sableMouvant.wav")
        self.sableMouvantPassage = pygame.mixer.Sound("data/son/effets/sableMouvantPassage.wav")
        self.frigo =  pygame.mixer.Sound("data/son/effets/frigo.wav")
        self.ventilo = pygame.mixer.Sound("data/son/effets/ventilo.wav")
        self.incendie = pygame.mixer.Sound("data/son/effets/incendie.wav")
        self.tremblement = pygame.mixer.Sound("data/son/effets/tremblement.wav")
        
        self.krakenSpawn = pygame.mixer.Sound("data/son/effets/krakenSpawn.wav")
        self.mageSpawn = pygame.mixer.Sound("data/son/effets/mageSpawn.wav")
        self.golem_des_foretsSpawn = pygame.mixer.Sound("data/son/effets/golem_des_foretsSpawn.wav")
        self.dragonSpawn = pygame.mixer.Sound("data/son/effets/dragonSpawn.wav")
        self.oursinSpawn = pygame.mixer.Sound("data/son/effets/oursinSpawn.wav")
        self.yetiSpawn = pygame.mixer.Sound("data/son/effets/yetiSpawn.wav")
    #Delay entre son
        self.dernierVentilo = 0
        self.dernierSable = 0
