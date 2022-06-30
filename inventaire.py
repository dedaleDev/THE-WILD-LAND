import pygame

class Inventaire(pygame.sprite.Sprite):
    def __init__(self, rectX, rectY, listeItem):
        self.image = self.loadInventaire()
        self.listeItem = listeItem
        
        self.rect = self.image.get_rect()
        self.rect.x = rectX
        self.rect.y = rectY
        for i in range(len(listeItem)):
            if i==0:
                listeItem[i].rect.x = self.rect.x+12
                listeItem[i].rect.y = self.rect.y+12
            if i==1:
                listeItem[i].rect.x = self.rect.x+14+60
                listeItem[i].rect.y = self.rect.y+12
        
    def blitInventaire(self, fenetre):
        fenetre.blit(self.image, (self.rect.x, self.rect.y))
        for i in range (len(self.listeItem)) :

            fenetre.blit(self.listeItem[i].image, (self.listeItem[i].rect.x,self.listeItem[i].rect.y))

    def loadInventaire(self):
        im = pygame.image.load("data/menu/menu_tuile.png").convert_alpha()
        im = pygame.transform.scale(im, (643/2,178/2))
        return im

    def loadInfoBulle(self, source = "data/menu/infoBulleBatiment"):
        imgTemp = pygame.image.load(source)
        return imgTemp
    
    def blitInfoBulle(self, fenetre, item):
        fenetre.blit(item.infoBulle,(item.rect.x-175, self.rect.y-260))
