import pygame
import generation
from item import Item
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

def selectionDispoItem(game, tuile):
    optionDIspo = []
    if tuile.type==1:
        pass
    elif tuile.type==2:
        optionDIspo.append(Item(game, "forge", 20))
    elif tuile.type==3:
        optionDIspo.append(Item(game, "moulin", 20))
    elif tuile.type==4:
        optionDIspo.append(Item(game, "scierie", 20))
    elif tuile.type==5:
        optionDIspo.append(Item(game, "igloo", 20))
    elif tuile.type==6:
        optionDIspo.append(Item(game, "puit", 20))
    return optionDIspo
    