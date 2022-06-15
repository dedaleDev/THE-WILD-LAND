import main_menu
import pygame_gestion
import generation
import sys

def main():
    while main_menu.loadMainMenu == True :
        if main_menu.loadMainMenu==True :
            main_menu.Main_Menu()  # si la partie est lancé
        if main_menu.startGame == True:
            main_menu.loadMainMenu = False
            main_menu.startGame = False
            print("Lancement du jeu")

            pygame_gestion.pygameInit()
            
    sys.exit()


main()
