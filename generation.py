import random
from tuile import Tuile
import pygame
taille_matrice = 16


def majProba(matriceMap, i, j, probaSup):
    for x in range(-1, 1):
        for y in range(-1, 1):
            if i+x < len(matriceMap) and j+y < len(matriceMap):
                matriceMap[i+x][j+y].augmenterProba(probaSup)


def generation_matrice():
    #1 = terre
    #2 = roche
    #3 = mer
    #4 = foret
    proba_roche = 50  # en %
    proba_mer = 50
    proba_foret = 25

    matriceMap = []
    for i in range(taille_matrice):
        matriceMap.append([0]*taille_matrice)

    for i in range(taille_matrice):
        for j in range(len(matriceMap[i])):
            # initialisation d'une carte remplie de terre
            matriceMap[i][j] = Tuile(1)

    for i in range(taille_matrice):
        matriceMap[i][0] = Tuile(2)
        matriceMap[i][taille_matrice-1] = Tuile(2)
        matriceMap[0][i] = Tuile(2)
        matriceMap[taille_matrice-1][i] = Tuile(2)

    for i in range(1, taille_matrice-1):
        for j in range(1, taille_matrice-1):

            temp = random.randint(1, 100)
            if temp <= proba_roche + matriceMap[i][j].getProba():
                matriceMap[i][j] = Tuile(2)
                majProba(matriceMap, i, j, 25)

            temp = random.randint(1, 100)
            if temp <= proba_mer + matriceMap[i][j].getProba():
                matriceMap[i][j] = Tuile(3)
                majProba(matriceMap, i, j, 25)

            temp = random.randint(1, 100)
            if temp <= proba_foret + matriceMap[i][j].getProba():
                matriceMap[i][j] = Tuile(4)
                majProba(matriceMap, i, j, 25)
    return matriceMap


def printMap(matriceMap):
    for i in range(len(matriceMap)):
        print('\n')
        for j in range(len(matriceMap[0])):
            print(matriceMap[i][j].getProba(), ', ', end='')

def  loadImg(matriceMap=[]):
    #fonction pour remplacer le plan de la map par des images
    matricemap=matriceMap[:]#copie tout dans un nouvel espace mémoire.
    for i in range(len(matricemap)):
        for j in range(len(matricemap[i])):
            typeTemp = matricemap[i][j].getType()
            if typeTemp == 1 :# si Terre
                imgTemp = pygame.image.load("data/tuiles/#1_terre.png")
            elif typeTemp ==2 : 
                imgTemp = pygame.image.load("data/tuiles/#2_roche.png")
            elif typeTemp == 3:
                imgTemp = pygame.image.load("data/tuiles/#3_mer.png")
            elif typeTemp == 4:
                imgTemp = pygame.image.load("data/tuiles/#4_foret.png")
            imgTemp = pygame.transform.scale(imgTemp, (64, 64))
            matricemap[i][j] = imgTemp
    return matricemap
