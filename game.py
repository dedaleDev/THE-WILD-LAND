import pygame

import generation
from imageLoad import ImageLoad
from PIL import Image
class Game(pygame.sprite.Sprite):
    def __init__(self, infoObject):
        self.infoObject=infoObject
        self.tailleEcran = [(3840, 2160), (2560, 1440), (1920, 1080),(1536,864),(1280, 720), (800, 600), (640, 480)]
        self.affichageTuile = [(0.19, 2.77), (0.19, 2.77), (0.19, 2.77),(0.19, 4),(0.19, 2.77), (0.19, 2.77), (0, 0)]
        self.affichagePersonalise = self.affichage()
        self.decalageMontagneX = self.getAffichageTuile()[self.affichagePersonalise][0]/100*self.infoObject.current_w
        self.decalageMontagneY = self.affichageTuile[self.affichagePersonalise][1]/100*self.infoObject.current_h
        self.images = ImageLoad()

        self.map = 0
        self.imageFog = self.openFog()
        self.mapImg = 0


    def verifierCo(self, x, y):
        return  x<generation.taille_matriceX and x >0 and y < generation.taille_matriceY and y>0
        
    def genererMatrice(self):
        self.map = generation.generation_matrice(self)



    def affichage(self):
        for i in range(len(self.tailleEcran)):
            if self.tailleEcran[i][0] == self.infoObject.current_w and self.tailleEcran[i][1] == self.infoObject.current_h:
                return i
        return 2
    
    def getAffichageTuile(self):
        return self.affichageTuile

    
    def genererImg(self):
        background_pil = Image.new('RGBA',(170*generation.taille_matriceX,170*generation.taille_matriceY), 0) 
        dx = round(self.decalageMontagneX)
        dy = round(self.decalageMontagneY)
        for y in range(generation.taille_matriceY):
            for x in range(generation.taille_matriceX):
                if self.map[y][x].isExplored:
                    background_pil.paste(self.map[y][x].imageO, (self.map[y][x].Xoriginal, self.map[y][x].Yoriginal), self.map[y][x].imageO)
                
                #elif self.map[y][x].tuileHaute():
                #        background_pil.paste(self.imageFog, (self.map[y][x].Xoriginal+dx, self.map[y][x].Yoriginal+20+dy), self.imageFog)
                else :
                    background_pil.paste(self.imageFog, (self.map[y][x].Xoriginal, self.map[y][x].Yoriginal), self.imageFog)
        

        self.mapImg = pygame.image.fromstring(background_pil.tobytes(), background_pil.size,'RGBA').convert_alpha()



    def openFog(self):
        imgTemp = Image.open("data/tuiles/0exploration.png").convert('RGBA')
        imgTemp = imgTemp.resize((150, 150))
        return imgTemp
    

    def deleteFog(self,x,y):
        modification=False
        if self.verifierCo(x, y):
            if not self.map[y][x].isExplored:
                self.map[y][x].setExplored(True)
                modification=True
                #pygame_gestion.joueur.setWater(-10)
        return modification
        