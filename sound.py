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