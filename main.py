import main_menu
import pygame_gestion

while main_menu.load ==True :
    main_menu.Main_Menu() # si la partie est lancé
    if main_menu.startGame == True:
        print("Lancement du jeu")
        pygame_gestion.pygameInit()

