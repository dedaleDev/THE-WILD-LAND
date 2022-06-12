import random
import pygame
from tuile import Tuile
taille_matriceX = 12#Y
taille_matriceY = 18#X
proba_roche = 15  # en %
proba_mer = 5
proba_foret = 15


def tirer_mer(matriceMap, i, j):
    temp = random.randint(1, 100)
    if temp <= proba_mer + matriceMap[i][j].getProba_mer():
        matriceMap[i][j] = Tuile(3)
        majProba(matriceMap, i, j, 100, "mer")


def tirer_foret(matriceMap, i, j):
    temp = random.randint(1, 100)
    if temp <= proba_foret + matriceMap[i][j].getProba_foret():
        matriceMap[i][j] = Tuile(4)
        majProba(matriceMap, i, j, 25, "foret")


def tirer_roche(matriceMap, i, j):
    temp = random.randint(1, 100)
    if temp <= proba_roche + matriceMap[i][j].getProba_roche():
        matriceMap[i][j] = Tuile(2)
        majProba(matriceMap, i, j, 25, nature= "roche")


def majProba(matriceMap, i, j, probaSup, nature):
    liste =[-1,1]
    for x in range(-1, 1):
        for y in range(-1, 1):
            if i+x < len(matriceMap) and j+y < len(matriceMap):
                if nature == "roche":
                    matriceMap[i+x][j+y].augmenterProbaRoche(probaSup)
                if nature == "foret":
                    matriceMap[i+x][j+y].augmenterProbaForet(probaSup)
                if nature == "mer" and not(x in liste and y in liste) :

                    matriceMap[i+x][j+y].augmenterProbaMer(probaSup)


def generation_matrice():
    #1 = terre
    #2 = roche
    #3 = mer
    #4 = foret

    matriceMap = []
    for i in range(taille_matriceX):
        matriceMap.append([0]*taille_matriceY)

    for i in range(taille_matriceX):
        for j in range(len(matriceMap[i])):
            # initialisation d'une carte remplie de terre
            matriceMap[i][j] = Tuile(1)

    for i in range(taille_matriceX):
        matriceMap[i][0] = Tuile(2)
        matriceMap[i][taille_matriceY-1] = Tuile(2)
    for i in range (taille_matriceY):
        matriceMap[0][i] = Tuile(2)
        matriceMap[taille_matriceX-1][i] = Tuile(2)

    for i in range(1, taille_matriceX-1):
        for j in range(1, taille_matriceY-1):
            a = random.randint(1, 3)
            if a == 1:
                tirer_foret(matriceMap, i, j)
                tirer_mer(matriceMap, i, j)
                tirer_roche(matriceMap, i, j)
            if a == 2:
                tirer_mer(matriceMap, i, j)
                tirer_roche(matriceMap, i, j)
                tirer_foret(matriceMap, i, j)
            if a == 3:
                tirer_roche(matriceMap, i, j)
                tirer_foret(matriceMap, i, j)
                tirer_mer(matriceMap, i, j)

    return matriceMap



def loadImg(matriceMap=[]):
    #fonction pour remplacer le plan de la map par des images
    matricemap = matriceMap[:]  # copie tout dans un nouvel espace mémoire.
    for i in range(len(matricemap)):
        for j in range(len(matricemap[i])):
            typeTemp = matricemap[i][j].getType()
            if typeTemp == 1:  # si Terre
                imgTemp = pygame.image.load("data/tuiles/1terre.png")
            elif typeTemp == 2:
                imgTemp = pygame.image.load("data/tuiles/2roche.png")
            elif typeTemp == 3:
                imgTemp = pygame.image.load("data/tuiles/3mer.png")
            elif typeTemp == 4:
                imgTemp = pygame.image.load("data/tuiles/4foret.png")
            imgTemp = pygame.transform.scale(imgTemp, (150, 150))
            matricemap[i][j] = imgTemp
    return matricemap
