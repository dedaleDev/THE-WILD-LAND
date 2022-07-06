import generation
from item import Item
def majSelection(game, pos, joueur=False):
    tuileSelect = False
    souris = pos
    if not joueur:
        for i in range(generation.taille_matriceY):
            for j in range(generation.taille_matriceX):
                pos_in_mask = souris[0] - game.map[i][j].rect.x, souris[1] - game.map[i][j].rect.y
                touching = game.map[i][j].rect.collidepoint(souris) and game.map[i][j].mask.get_at(pos_in_mask)
                if touching :
                    if game.map[i][j].estSelect:
                        game.map[i][j].setSelect(False)
                    else:
                        game.map[i][j].setSelect(True)
                        tuileSelect = game.map[i][j]
                else :
                    game.map[i][j].setSelect(False)
    else:
        for i in range(-1, 2):
            for j in range(-1, 2):
                pos_in_mask = souris[0] - game.map[joueur.posY+i][joueur.posX+j].rect.x, souris[1] - game.map[joueur.posY+i][joueur.posX+j].rect.y
                touching = game.map[joueur.posY+i][joueur.posX+j].rect.collidepoint(souris) and game.map[joueur.posY+i][joueur.posX+j].mask.get_at(pos_in_mask)
                if touching :
                    if game.map[joueur.posY+i][joueur.posX+j].estSelect:
                        game.map[joueur.posY+i][joueur.posX+j].setSelect(False)
                    else:
                        game.map[joueur.posY+i][joueur.posX+j].setSelect(True)
                        tuileSelect = game.map[joueur.posY+i][joueur.posX+j]
                else :
                    game.map[joueur.posY+i][joueur.posX+j].setSelect(False)
    return tuileSelect

def majSelectionJoueur(game, pos):
    tuileSelect = False
    souris = pos
    for i in range(generation.taille_matriceY):
        for j in range(generation.taille_matriceX):
            pos_in_mask = souris[0] - game.map[i][j].rect.x, souris[1] - game.map[i][j].rect.y
            touching = game.map[i][j].rect.collidepoint(souris) and game.map[i][j].mask.get_at(pos_in_mask)
            if touching :
                tuileSelect = game.map[i][j]

    return tuileSelect

def selectionDispoItem(game, tuile, joueur):
    optionDIspo = []
    if tuile.isExplored and not joueur.bateau:
        if tuile.type==1:
            optionDIspo.append(Item(game, "elevage", 175, 75,0,0))
            optionDIspo.append(Item(game, "champs", 50, 25,0,0))
            optionDIspo.append(Item(game, "tour", 0, 0, 0, 300 ))
            optionDIspo.append(Item(game, "pieux", 0,0, 50, 50))
        elif tuile.type==2:
            optionDIspo.append(Item(game, "forge", 0,0,0,0))
            optionDIspo.append(Item(game, "mine", 0,0,50,50))
            optionDIspo.append(Item(game, "mortier", 0,0,0,200))
        elif tuile.type==3:
            optionDIspo.append(Item(game, "moulin", 0,0,100,0))
            if not game.avoirTuileJoueur(joueur).port:
                optionDIspo.append(Item(game, "port", 0,0,250,0))
        elif tuile.type==4:
            optionDIspo.append(Item(game, "scierie", 0,0,100,0))
        elif tuile.type==5:
            #optionDIspo.append(Item(game, "igloo", 20))
            pass
        elif tuile.type==6:
            optionDIspo.append(Item(game, "sableMouvant", 200, 100,0,0))

    return optionDIspo
    
    
def colisionItem(item, pos):
    return item.rect.collidepoint(pos)
