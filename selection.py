import pygame
def majSelection(game):
    tuileSelect = False
    souris = pygame.mouse.get_pos()
   
    for i in range(len(game.map)):
        for j in range(len(game.map[i])):
            if game.map[i][j].rect.collidepoint(souris):
                game.map[i][j].setSelect(True)
                tuileSelect = game.map[i][j]
            else:
                game.map[i][j].setSelect(False)
    return tuileSelect