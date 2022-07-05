import pygame

import generation
from imageLoad import ImageLoad
from PIL import Image
background_pil = Image.new('RGBA',(170*generation.taille_matriceX,170*generation.taille_matriceY), 0)
premierPAss=True
class Game(pygame.sprite.Sprite):
    def __init__(self, infoObject, fenetre):
        self.infoObject=infoObject
        self.tailleEcran = [(3840, 2160), (2560, 1440), (1920, 1080),(1536,864),(1280, 720), (800, 600), (640, 480)]
        self.affichageTuile = [(0.19, 2.77), (0.19, 2.77), (0.19, 2.77),(0.19, 4),(0.19, 2.77), (0.19, 2.77), (0, 0)]
        self.affichagePersonalise = self.affichage()
        self.decalageMontagneX = self.getAffichageTuile()[self.affichagePersonalise][0]/100*self.infoObject.current_w
        self.decalageMontagneY = self.affichageTuile[self.affichagePersonalise][1]/100*self.infoObject.current_h
        self.images = ImageLoad()
        self.imCollision = self.images.getImCollision()
        self.map = 0
        self.mapMontagneMer = 0
        self.imageFog = self.openFog()
        self.mapImg = 0
        self.mapImgO = 0
        self.mapMer = 0
        self.listeCaseMer = 0
        self.fenetre = fenetre
        
        self.groupMob = pygame.sprite.Group()
        self.groupProjectile = pygame.sprite.Group()
        self.groupDefense = pygame.sprite.Group()
        

    def verifierCo(self, x, y):
        return  x<generation.taille_matriceX and x >0 and y < generation.taille_matriceY and y>0
        
    def genererMatrice(self):
        self.map = generation.generation_matrice(self)
        self.mapMontagneMer, self.listeCaseMer, self.mapMer = generation.generation_matriceMontagneMer(self.map)
        
    def checkCollision(self, joueur, listeMob):
        listeColide=[]
        now = pygame.time.get_ticks()
        for mob in listeMob :
            colide = mob.rect.colliderect(joueur.rect)
            if colide and now-joueur.lastDamage>joueur.cooldownDamage:
                joueur.takeDamage(mob.attack)
                joueur.lastDamage=now
                listeColide.append(colide)
        return listeColide
                

    def affichage(self):
        for i in range(len(self.tailleEcran)):
            if self.tailleEcran[i][0] == self.infoObject.current_w and self.tailleEcran[i][1] == self.infoObject.current_h:
                return i
        return 2
    
    def getAffichageTuile(self):
        return self.affichageTuile

    def avoirTuileJoueur(self, joueur):
        return self.map[joueur.posY][joueur.posX]
    def genererImg(self):
        global background_pil, premierPAss
        modification=False
        for y in range(generation.taille_matriceY):
            for x in range(generation.taille_matriceX):
                if self.map[y][x].aEteModifie:        
                    #print(self.map[y][x].posY, self.map[y][x].posX)
                    if self.map[y][x].isExplored:
                        background_pil.paste(self.map[y][x].imageO, (self.map[y][x].Xoriginal, self.map[y][x].Yoriginal), self.map[y][x].imageO)
                    else :
                        background_pil.paste(self.imageFog, (self.map[y][x].Xoriginal, self.map[y][x].Yoriginal), self.imageFog)
                    self.map[y][x].aEteModifie=False
                    modification=True                    
        if modification:

            if premierPAss:
                self.mapImg = pygame.image.frombuffer(background_pil.tobytes(), background_pil.size, "RGBA").convert_alpha()

            self.mapImgO = background_pil


    def collerImageBackground(self, tuile):
        
        if tuile.isExplored:
            self.mapImgO.paste(tuile.imageO, (tuile.Xoriginal, tuile.Yoriginal), tuile.imageO)
        else:
            self.mapImgO.paste(self.imageFog, (tuile.Xoriginal, tuile.Yoriginal), self.imageFog)
        self.mapImg = pygame.image.fromstring(self.mapImgO.tobytes(),self.mapImgO.size,'RGBA').convert_alpha()
            

    def openFog(self):
        imgTemp = Image.open("data/tuiles/0exploration.png").convert('RGBA')
        imgTemp = imgTemp.resize((150, 150))
        return imgTemp
    

    def deleteFog(self,x,y):
        modification = False
        if self.verifierCo(x, y):
            if not self.map[y][x].isExplored:
                self.map[y][x].setExplored(True)
                modification=True
        return modification
                #pygame_gestion.joueur.setWater(-10)
        
