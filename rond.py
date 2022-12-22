import time
import pygame
import sys

pygame.init()

# Définit les dimensions de la fenêtre d'affichage
screen_width, screen_height = 1000, 800
screen = pygame.display.set_mode((screen_width, screen_height))

# Définit la couleur de fond de la fenêtre d'affichage
bg_color = (255, 255, 255)

# Définit les dimensions et la couleur de la barre de chargement
loading_bar_width, loading_bar_height = 100, 20
loading_bar_color = (0, 0, 0)

# Définit la vitesse de progression de la barre de chargement (en pourcentage par frame)
loading_bar_speed = 0.1

# Initialise le pourcentage de progression de la barre de chargement à 0
loading_bar_progress = 0

# Boucle principale du jeu
while True:
    # Gère les événements de Pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Efface l'écran en utilisant la couleur de fond
    screen.fill(bg_color)

    # Augmente le pourcentage de progression de la barre de chargement
    loading_bar_progress += loading_bar_speed

    # Dessine la barre de chargement en utilisant le pourcentage de progression actuel
    pygame.draw.rect(screen, loading_bar_color, (screen_width // 2 - loading_bar_width // 2, screen_height // 2 - loading_bar_height // 2, loading_bar_width, loading_bar_height))
    pygame.draw.rect(screen, (255,0,255), (screen_width // 2 - loading_bar_width // 2, screen_height // 2 - loading_bar_height // 2, int(loading_bar_width * loading_bar_progress), loading_bar_height))

    # Met à jour l'affichage
    pygame.display.flip()
    time.sleep(0.1)