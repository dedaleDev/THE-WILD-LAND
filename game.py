import pygame
import generation
from PIL import Image
class Game(pygame.sprite.Sprite):
    def __init__(self, infoObject):
        self.infoObject=infoObject
        self.tailleEcran = [(3840, 2160), (2560, 1440), (1920, 1080),(1536,864),(1280, 720), (800, 600), (640, 480)]
        self.affichageTuile = [(0.19, 2.77), (0.19, 2.77), (0.19, 2.77),(0.19, 4),(0.19, 2.77), (0.19, 2.77), (0, 0)]
        self.affichagePersonalise = self.affichage()
        self.map = generation.generation_matrice(self)
        self.mapImg = 0
        
        



    def affichage(self):
        for i in range(len(self.tailleEcran)):
            if self.tailleEcran[i][0] == self.infoObject.current_w and self.tailleEcran[i][1] == self.infoObject.current_h:
                return i
        return 2
    
    def getAffichageTuile(self):
        return self.affichageTuile

    
    def genererImg(self):
        background_pil = Image.new('RGBA',(150*generation.taille_matriceX,190*generation.taille_matriceY), 0) 
        for y in range(generation.taille_matriceX):
            for x in range(generation.taille_matriceY):
                print(self.map[y][x].getRectX())
                print(self.map[y][x].getRectY())
                if self.map[y][x].type == 2 or self.map[y][x].type == 7:
                    background_pil.paste(self.map[y][x].imageO, (self.map[y][x].getRectX(), self.map[y][x].getRectY()), self.map[y][x].imageO)
                background_pil.paste(self.map[y][x].imageO, (self.map[y][x].getRectX(), self.map[y][x].getRectY()), self.map[y][x].imageO)
                
        self.mapImg = pygame.image.fromstring(background_pil.tobytes(), background_pil.size,'RGBA')
            
            
            

            
