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
        self.imageFog = self.openFog()
        self.mapImg = self.genererImg()
        
    
    
    def verifierCo(self, x, y):
        return  x<len(self.map[0]) and x >0 and y <len(self.map) and y>0
        



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
                if self.map[y][x].isExplored:
                    background_pil.paste(self.map[y][x].imageO, (self.map[y][x].getRectX(), self.map[y][x].getRectY()), self.map[y][x].imageO)
                else :
                    background_pil.paste(self.imageFog, (self.map[y][x].getRectX(), self.map[y][x].getRectY()), self.imageFog)


        return pygame.image.fromstring(background_pil.tobytes(), background_pil.size,'RGBA')
        


    def openFog(self):
        imgTemp = Image.open("data/tuiles/0exploration.png").convert('RGBA')
        imgTemp = imgTemp.resize((150, 150))
        return imgTemp
    

    def deleteFog(self,x,y, moveX, moveY):
        if self.verifierCo(x, y):
            self.map[x][y].setExplored(True)
            """if self.map[x][y].type==2 or self.map[x][y].type==7:
                self.map[x][y].rect.x = self.map[x][y].avoirX()+moveX
                self.map[x][y].rect.y = self.map[x][y].avoirY()+moveY"""
                
        self.mapImg = self.genererImg()
        
