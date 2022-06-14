import pygame


class Tuile(pygame.sprite.Sprite):
    def __init__(self, type):
        self.type = type
        self.canon = False
        self.probaSup_mer = 0
        self.probaSup_roche = 0
        self.probaSup_foret = 0
        self.probaSup_desert = 0
        self.probaSup_neige = 0
        self.autoriserNeige = False
        self.autoriserDesert = True


    def setType(self, entier):
        self.type=entier
    
    
    def getType(self):
        return self.type

    def getProbaMer(self):
        return self.probaSup_mer
    
    def getProbaDesert(self):
        return self.probaSup_desert

    def getProbaRoche(self):
        return self.probaSup_roche

    def getProbaNeige(self):
        return self.probaSup_neige

    def getProbaForet(self):
        return self.probaSup_foret

    def getCanon(self):
        return self.canon

    def getAutoriserNeige(self):
        return self.autoriserNeige
    
    def getAutoriserDesert(self):
        return self.autoriserDesert
    
    def setInterdireDesert(self):
        self.autoriserDesert = False
    
    def setAutoriserNeige(self):
        self.autoriserNeige = True
    
    def interdireNeige(self):
        self.autoriserNeige = False
    
    def augmenterProbaMer(self, entier):
        self.probaSup_mer += entier

    def augmenterProbaRoche(self, entier):
        self.probaSup_roche += entier

    def augmenterProbaForet(self, entier):
        self.probaSup_foret += entier
    def augmenterProbaDesert(self, entier):
        self.probaSup_desert += entier
    def augmenterProbaNeige(self, entier):
        self.probaSup_neige += entier
