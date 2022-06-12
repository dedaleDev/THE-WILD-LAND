import pygame


class Tuile(pygame.sprite.Sprite):
    def __init__(self, type):
        self.type = type
        self.canon = False
        self.probaSup_mer = 0
        self.probaSup_roche = 0
        self.probaSup_foret = 0

    def getType(self):
        return self.type

    def getProba_mer(self):
        return self.probaSup_mer

    def getProba_roche(self):
        return self.probaSup_roche

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
