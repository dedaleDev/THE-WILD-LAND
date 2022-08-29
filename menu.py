import pygame
from pygame.constants import KEYDOWN, K_ESCAPE, MOUSEBUTTONDOWN
import math


def scale(im, scale):
    return pygame.transform.scale(im, (im.get_width()*scale, im.get_height()*scale))

def load_image(file):
    im = pygame.image.load('data/menu' + file).convert_alpha()
    if file=="start" or file=="title" or file=="button_options" or file=="button_quit":
        im = pygame.transform.scale(im, (30, 30))
        return im
    return im

def load_sound(file):
    return pygame.mixer.Sound('data/son/musiques'+file)
 