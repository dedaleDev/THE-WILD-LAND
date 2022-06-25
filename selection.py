import pygame
import generation
def majSelection(game):
    tuileSelect = False
    souris = pygame.mouse.get_pos()
    
    for i in range(generation.taille_matriceY):
        for j in range(generation.taille_matriceX):
            decalageX=0
            decalageY=0
            if abs(game.map[i][j].rect.y-souris[1])<75:
                decalageX=-50
            if game.map[i][j].type==2:
                decalageY=-50
            
            if game.map[i][j].rect.collidepoint(souris[0]+decalageX, souris[1]+decalageY):
                if game.map[i][j].estSelect:
                    game.map[i][j].setSelect(False)
                else:
                    game.map[i][j].setSelect(True)
                    tuileSelect = game.map[i][j]
            else:
                game.map[i][j].setSelect(False)
    return tuileSelect