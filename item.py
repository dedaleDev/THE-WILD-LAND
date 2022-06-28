from this import d
import pygame

class Item(pygame.sprite.Sprite):
    
    def __init__(self, game, nom, cout) :
        self.game = game
        self.image = game.images.returnImItem(nom)
        self.cout = cout
    
    