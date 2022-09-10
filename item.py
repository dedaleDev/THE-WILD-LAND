from multiprocessing.util import info
import pygame

class Item(pygame.sprite.Sprite):

    def __init__(self, game, nom, coutWater, coutFood, coutWood, coutStone, infobulle=True) :
        self.game = game
        self.nom = nom
        self.image = game.images.returnImItem(nom)
        self.coutWater = coutWater
        self.coutWood = coutWood
        self.coutFood = coutFood
        self.coutStone = coutStone
        if infobulle:
            self.infoBulle =game.images.ImInfoBullItem(nom)
        else :
            self.infoBulle=None
        self.rect = self.image.get_rect()