import pygame

class ScrollBar:
    def __init__(self, bar_color, bar_pos, default_value, scale=(300,10)):
        # Enregistrer la fenêtre pygame, la couleur de la barre et sa position
        self.bar_color = bar_color
        self.bar_pos = bar_pos
        
        # Définir les couleurs
        self.WHITE = (255, 255, 255)
        self.GRAY = (128, 128, 128)

        # Définir les paramètres de la barre de défilement
        self.BAR_WIDTH = 300
        self.BAR_HEIGHT = 10
        self.BAR_MARGIN = 40
        self.bar_rect = pygame.Rect(self.bar_pos[0], self.bar_pos[1], self.BAR_WIDTH, self.BAR_HEIGHT)

        # Définir les paramètres du curseur
        self.CURSOR_RADIUS = 15
        self.CURSOR_POS = (self.bar_pos[0]+(default_value*self.BAR_WIDTH)//100, self.bar_pos[1] + self.BAR_HEIGHT//2)

        # Enregistrer la valeur par défaut
        self.value = default_value

        # Initialiser les états de fonctionnement de la barre
        self.running = True
        self.dragging = False
        self.cursor_rect=""

    def getValue(self):
        if self.value<0:
            return 0
        elif self.value>100:
            return 100
        return self.value