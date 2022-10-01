import pygame

class Build(pygame.sprite.Sprite):
    def __init__(self, game, nomBatiment):
          super().__init__()
          self.game = game
          self.nomBatiment=nomBatiment
    
    
    