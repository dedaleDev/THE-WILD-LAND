import pygame
import generation
def majSelection(game, pos):
    tuileSelect = False
    souris = pos
    for i in range(generation.taille_matriceY):
        for j in range(generation.taille_matriceX):
            pos_in_mask = souris[0] - game.map[i][j].rect.x, souris[1] - game.map[i][j].rect.y
            touching = game.map[i][j].rect.collidepoint(souris) and game.map[i][j].mask.get_at(pos_in_mask)
            if touching :
                game.map[i][j].setSelect(True)
                tuileSelect = game.map[i][j]
            else :
                game.map[i][j].setSelect(False)
    return tuileSelect