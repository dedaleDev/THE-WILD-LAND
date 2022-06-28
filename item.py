
import pygame

class Item(pygame.sprite.Sprite):
    
    def __init__(self, game, nom, cout) :
        self.game = game
        self.nom = nom
        self.image = game.images.returnImItem(nom)
        self.cout = cout
        self.rect = self.image.get_rect()
    
    