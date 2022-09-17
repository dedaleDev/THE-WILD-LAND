import pygame

class Coffre(pygame.sprite.Sprite):
    def __init__(self, game, tuile, wood, stone, food, water):
          super().__init__()
          self.indice=0
          self.game = game
          self.tuile = tuile
          self.image = game.images.coffre
          self.rect = self.image[0].get_rect()
          self.rect.x = self.tuile.Xoriginal+80
          self.rect.y = self.tuile.Yoriginal+40
          self.wood = wood
          self.food = food
          self.stone = stone 
          self.water = water
          self.clock = 0
          self.clockMax = 10
          #PREMIERE ETOILE
          self.imEtoile = self.game.images.etoile
          self.etoileRect = self.imEtoile.get_rect()
          self.etoileRect.x = self.rect.x-30
          self.etoileRect.y = self.rect.y
          
          self.etoileRectXoriginal = self.rect.x
          self.etoileRectYoriginal = self.rect.y
          self.etoileMonte = True
          #DEUXIEME ETOILE
          
          self.imEtoile2 = self.game.images.etoile
          self.etoileRect2 = self.imEtoile2.get_rect()
          self.etoileRect2.x = self.rect.x+40
          self.etoileRect2.y = self.rect.y-20
          
          self.etoileRectXoriginal2 = self.etoileRect2.x
          self.etoileRectYoriginal2 = self.etoileRect2.y+3
          self.etoileMonte2 = True
          
          #TROISIEME ETOILE
          
          self.imEtoile3 = self.game.images.etoile
          self.etoileRect3 = self.imEtoile3.get_rect()
          self.etoileRect3.x = self.rect.x+78
          self.etoileRect3.y = self.rect.y+5
          
          self.etoileRectXoriginal3 = self.etoileRect3.x
          self.etoileRectYoriginal3 = self.etoileRect3.y-2
          self.etoileMonte3 = True
          
    def etoileAnnim(self):
        
        if abs(self.etoileRectYoriginal - self.etoileRect.y) == 5 :
            self.etoileMonte = not self.etoileMonte
        if self.etoileMonte :
            self.etoileRect.y+=1
        else :
            self.etoileRect.y-=1
        #DEUXIEME ETOILE
        if abs(self.etoileRectYoriginal2 - self.etoileRect2.y) == 5 :
            self.etoileMonte2 = not self.etoileMonte2
        if self.etoileMonte2 :
            self.etoileRect2.y+=1
        else :
            self.etoileRect2.y-=1
            
        #TROISIEME ETOILE
        
        if abs(self.etoileRectYoriginal3 - self.etoileRect3.y) == 5 :
            self.etoileMonte3 = not self.etoileMonte3
        if self.etoileMonte3 :
            self.etoileRect3.y+=1
        else :
            self.etoileRect3.y-=1