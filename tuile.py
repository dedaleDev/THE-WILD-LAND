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

    def getType(self):
        return self.type

    def getProba_mer(self):
        return self.probaSup_mer
    def getProba_desert(self):
        return self.probaSup_desert

    def getProba_roche(self):
        return self.probaSup_roche

    def getProba_neige(self):
        return self.probaSup_neige

    def getProba_foret(self):
        return self.probaSup_foret

    def getCanon(self):
        return self.canon

    def augmenterProbaMer(self, entier):
        self.probaSup_mer += entier
        print()
    def augmenterProbaRoche(self, entier):
        self.probaSup_roche += entier

    def augmenterProbaForet(self, entier):
        self.probaSup_foret += entier
    def augmenterProbaDesert(self, entier):
        self.probaSup_desert += entier
    def augmenterProbaNeige(self, entier):
        self.probaSup_neige += entier
