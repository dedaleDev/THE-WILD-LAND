import pygame

class Inventaire(pygame.sprite.Sprite):
    def __init__(self, rectX, rectY, listeItem):
        self.image = self.loadInventaire()
        self.listeItem = listeItem
        
        self.rect = self.image.get_rect()
        self.rect.x = rectX
        self.rect.y = rectY
        
        self.listePosItem = [(self.rect.x+12, self.rect.y+12), (self.rect.x+14+60, self.rect.y+12)]
        
    def blitInventaire(self, fenetre):
        fenetre.blit(self.image, (self.rect.x, self.rect.y))
        for i in range (len(self.listeItem)) :

            fenetre.blit(self.listeItem[i].image, self.listePosItem[i])

    def loadInventaire(self):
        im = pygame.image.load("data/menu/menu_tuile.png").convert_alpha()
        im = pygame.transform.scale(im, (643/2,178/2))
        return im
    
