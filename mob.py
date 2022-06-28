from random import randint
from PIL import Image
import pygame
from joueur import Player
class Mob(Player):

     def __init__(self, game, nom):
          super().__init__(game, nom)
     def randmove(self):
          rand = randint(1,4)
          if rand == 1:
               if super().deplacementAutorise("droite") :
                    self.goRight()
          if rand == 2:
               if super().deplacementAutorise("gauche") :
                    self.goLeft()
          if rand == 3:
               if super().deplacementAutorise("haut") :
                    self.goUp()
          if rand == 4:
               if super().deplacementAutorise("bas") :
                    self.goDown()
          