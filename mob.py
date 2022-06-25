from PIL import Image
import pygame
from joueur import Player
class Mob(Player):

     def __init__(self, game, nom):
          super().__init__(game, nom)
          
          