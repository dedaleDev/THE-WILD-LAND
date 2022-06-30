import pygame

class Item(pygame.sprite.Sprite):
    
    def __init__(self, game, nom, cout, infoBulle) :
        self.game = game
        self.nom = nom
        self.image = game.images.returnImItem(nom)
        self.cout = cout
        self.infoBulle =game.images.ImInfoBullItem(nom)
        self.rect = self.image.get_rect()