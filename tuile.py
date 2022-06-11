import pygame
class Tuile(pygame.sprite.Sprite):
    def __init__(self, type):
        self.type = type
        self.canon = False
        self.probaSup = 0
        
        
    def getType(self):
        return self.type
    
    def getCanon(self):
        return self.canon
    

    def augmenterProba(self, entier):
        self.probaSup += entier
    
    