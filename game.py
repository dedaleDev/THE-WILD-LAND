import pygame
import generation
from PIL import Image
class Game(pygame.sprite.Sprite):
    def __init__(self, infoObject):
        self.infoObject=infoObject
        self.tailleEcran = [(3840, 2160), (2560, 1440), (1920, 1080),(1536,864),(1280, 720), (800, 600), (640, 480)]
        self.affichageTuile = [(0.19, 2.77), (0.19, 2.77), (0.19, 2.77),(0.19, 4),(0.19, 2.77), (0.19, 2.77), (0, 0)]
        self.affichagePersonalise = self.affichage()
        self.matrice = generation.generation_matrice(self)
        self.map = self.matrice[0]
        self.mapImg = 0
        self.mapExploration = self.matrice[1]
        self.fogIMG = self.genererFogIMG()
        



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
                if self.map[y][x].type == 2 or self.map[y][x].type == 7:
                    background_pil.paste(self.map[y][x].imageO, (self.map[y][x].getRectX()+20, self.map[y][x].getRectY()+20), self.map[y][x].imageO)
                background_pil.paste(self.map[y][x].imageO, (self.map[y][x].getRectX()+20, self.map[y][x].getRectY()+20), self.map[y][x].imageO)
                
        self.mapImg = pygame.image.fromstring(background_pil.tobytes(), background_pil.size,'RGBA')
            
    def genererFogIMG(self):
        fogIMG_pil = Image.new('RGBA', (150*generation.taille_matriceX, 190*generation.taille_matriceY), 0)
        decalage =0
        for y in range(generation.taille_matriceX):
            for x in range(generation.taille_matriceY):
                if self.mapExploration[y][x] == True: #si est decouvert
                    decalage+=150
                else:
                    fogIMG_pil.paste(self.map[y][x].imageO, (self.map[y][x].getRectX()+20+decalage, self.map[y][x].getRectY()+20), self.map[y][x].imageO)
                    fogIMG_pil.paste(self.mapExploration[y][x].imageO, (self.map[y][x].getRectX(), self.mapExploration[y][x].getRectY()), self.mapExploration[y][x].imageO)
        self.fogIMG= pygame.image.fromstring(fogIMG_pil.tobytes(), fogIMG_pil.size, 'RGBA')

    def deleteFog(self,x,y):
        self.mapExploration[y][x] = True
            
