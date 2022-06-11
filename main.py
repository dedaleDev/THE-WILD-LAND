import main_menu
import pygame_gestion
import generation

def main():
    while main_menu.load ==True :
        main_menu.Main_Menu() # si la partie est lancé
        if main_menu.startGame == True:
            main_menu.startGame =False
            print("Lancement du jeu")
            map = generation.generation_matrice()
            pygame_gestion.pygameInit(map)

main()
