import pygame

class Loot(pygame.sprite.Sprite): #Classe servant a annimer un loot (de mob, coffre...)
    def __init__(self, bois, pierre, eau, food, x, y, game, coffre=False, coffreX=False, coffreY=False):
        super().__init__()
        
        
        self.game = game
        
        self.bois = bois
        self.pierre = pierre
        self.eau = eau
        self.food = food
        
        self.tempsBois = True
        self.tempsPierre = False
        self.tempsEau = False
        self.tempsFood = False
        
        self.indice = 0
        self.image = pygame.transform.scale(pygame.image.load("data/ressources/r_wood.png"), (100, 30)).convert_alpha()
        #self.image.set_alpha(100)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        self.rectXoriginal = self.rect.x #stockage des valeurs initiale pour revenir au point de depart lors de changement de ressources
        self.rectYoriginal = self.rect.y
        
        self.clockAnnim = 0
        self.clockAnnimMax = 3
        self.font =pygame.font.SysFont("Corbel", 25)  # definit la police utilisé
        self.fontBois = self.font.render("+"+str(self.bois), True, "black")
        self.fontPierre = self.font.render("+"+str(self.pierre), True, "black")
        self.fontEau = self.font.render("+"+str(self.eau), True, "black")
        self.fontFood = self.font.render("+"+str(self.food), True, "black")
        self.coffre=coffre
        self.coffreX=coffreX
        self.coffreY=coffreY
        
    def update(self, screen, moveX, moveY):
        self.clockAnnim+=1
        
        if self.clockAnnim>= self.clockAnnimMax:
            self.clockAnnim=0
            
            if self.tempsBois:
                
                self.indice+=1
                self.rect.y-=1
                if self.indice>=len(self.game.images.lootBois) or self.bois==0:
                    self.tempsBois=False
                    self.tempsPierre=True
                    self.indice=0
                    self.rect.y=self.rectYoriginal
                    
            elif self.tempsPierre:
                self.image = pygame.transform.scale(pygame.image.load("data/ressources/r_stone.png"), (100, 30)).convert_alpha()
                #self.image.set_alpha(100)
                self.rect.y-=1
                self.indice+=1
                if self.indice>=len(self.game.images.lootPierre) or self.pierre==0:
                    self.tempsPierre=False
                    self.tempsEau = True
                    self.indice=0
                    self.rect.y=self.rectYoriginal
                    
            elif self.tempsEau:
                self.image = pygame.transform.scale(pygame.image.load("data/ressources/r_water.png"), (100, 30)).convert_alpha()
                #self.image.set_alpha(100)
                self.rect.y-=1
                self.indice+=1
                if self.indice>=len(self.game.images.lootEau) or self.eau==0:
                    self.tempsEau=False
                    self.tempsFood = True
                    self.indice=0
                    self.rect.y=self.rectYoriginal
                    
            elif self.tempsFood:
                self.image = pygame.transform.scale(pygame.image.load("data/ressources/r_food.png"), (100, 30)).convert_alpha()
                #self.image.set_alpha(100)
                self.rect.y-=1
                self.indice+=1
                if self.indice>=len(self.game.images.lootFood) or self.food==0:
                    self.tempsFood=False
                    self.indice=0
                    self.rect.y=self.rectYoriginal
        continu = False
        if self.tempsBois and self.bois!=0:
            screen.blit(self.game.images.lootBois[self.indice], (self.rect.x+moveX-50, self.rect.y+moveY-150))
            screen.blit(self.image, (self.rect.x+moveX, self.rect.y+moveY))
            screen.blit(self.fontBois, (self.rect.x+moveX+35, self.rect.y+moveY))
            continu = True

        
        if self.tempsPierre and self.pierre:
            screen.blit(self.game.images.lootPierre[self.indice], (self.rect.x+moveX-50, self.rect.y+moveY-150))
            screen.blit(self.image, (self.rect.x+moveX, self.rect.y+moveY))
            screen.blit(self.fontPierre, (self.rect.x+moveX+35, self.rect.y+moveY))
            continu = True
            
        if self.tempsEau and self.eau!=0:
            screen.blit(self.game.images.lootEau[self.indice], (self.rect.x+moveX-50, self.rect.y+moveY-150))
            screen.blit(self.image, (self.rect.x+moveX, self.rect.y+moveY))
            screen.blit(self.fontEau, (self.rect.x+moveX+35, self.rect.y+moveY))
            continu = True

        if self.tempsFood and self.food!=0:
            screen.blit(self.game.images.lootFood[self.indice], (self.rect.x+moveX-50, self.rect.y+moveY-150))
            screen.blit(self.image, (self.rect.x+moveX, self.rect.y+moveY))
            screen.blit(self.fontFood, (self.rect.x+moveX+35, self.rect.y+moveY))
            continu = True

        if not continu and self.tempsFood:
            self.kill() #fini le loot, destruction de l'objet et fin de l'annim