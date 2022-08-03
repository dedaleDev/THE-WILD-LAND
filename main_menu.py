import pygame
from pygame.constants import KEYDOWN, K_ESCAPE, MOUSEBUTTONDOWN
import math
import os
"""
pygame.init()

GAME_RESOLUTION = (pygame.display.Info().current_w,pygame.display.Info().current_h)
DISPLAY = pygame.display.set_mode(GAME_RESOLUTION)
MUSIC = pygame.mixer.Channel(0)
MUSIC.set_volume(0.2)

def scale(im, scale):
    return pygame.transform.scale(im, (im.get_width()*scale, im.get_height()*scale))

def load_image(file):
    im = pygame.image.load(os.path.join(os.path.dirname(__file__), 'data/menu', file))
    if file=="start" or file=="title" or file=="button_options" or file=="button_quit":
        im = pygame.transform.scale(im, (30, 30))
        return im
    return im

def load_sound(file):
    return pygame.mixer.Sound(os.path.join(os.path.dirname(__file__), 'data/son/musiques', file))
 
def fullscreen():
    DISPLAY = pygame.display.set_mode(GAME_RESOLUTION, pygame.SCALED | pygame.FULLSCREEN)
 
def windowed():
    DISPLAY = pygame.display.set_mode(GAME_RESOLUTION)

class Window():
 
    def run(self):
 
        if hasattr(self, 'music'):
            MUSIC.play(self.music, -1)
 
        self.running = True
        while self.running:
 
            if hasattr(self, 'background'):
                DISPLAY.blit(self.background, self.pos)
 
            if hasattr(self, 'title'):
                self.bobbing()
                #DISPLAY.blit(self.title, self.title_rect)
 
            if hasattr(self, 'buttons'):
                for button in self.buttons:
                    DISPLAY.blit(button.image, button.rect)
 
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.running = False
                if event.type == MOUSEBUTTONDOWN:
                    for button in self.buttons:
                        button.run()
 
            pygame.display.update()

    def close(self):
        self.running = False
 
class Button():
    def __init__(self, pos, image, function = None):
 
        self.image = load_image(image)

        self.rect = self.image.get_rect()
        self.rect.topleft = pos
 
        self.function = function
 
    def run(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            self.function()

########################
#       WINDOWS        #
########################

class MainMenu(Window):
    def __init__(self):
        self.buttons = [
            (Button((880, 460), 'button_quit.png', pygame.quit)),
            (Button((416, 460), "start.png", self.close)),
            (Button((20, 460), 'button_options.png', OPTIONS_MENU.run)),
        ]
        self.background = pygame.transform.scale(load_image('menu_1.png'), GAME_RESOLUTION)
        self.pos = (0,0)
        self.title = pygame.transform.scale(load_image('title.png'), GAME_RESOLUTION)
        self.music = load_sound('menu.mp3')

        self.deg = 0
        self.sin = 0
 
    def bobbing(self):
        self.deg += 0.1
        if self.deg >= 180:
            self.deg = 0
        self.sin = math.sin(self.deg)
        self.title_rect = self.title.get_rect()
        self.title_rect.y += self.sin * 5
 
class OptionsMenu(Window):
    def __init__(self):
        self.buttons = [
            Button((416, 300), "fullscreen.png", fullscreen),
            Button((416, 400), "windowed.png", windowed),
            Button((20, 460), 'back.png', self.close),
        ]
        self.background = pygame.transform.scale(load_image('menu_2.png'), GAME_RESOLUTION)
        self.pos = (0,0)

OPTIONS_MENU = OptionsMenu()
MAIN_MENU = MainMenu()
MAIN_MENU.run()"""