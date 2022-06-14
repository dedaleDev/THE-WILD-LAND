import random
import pygame
from tuile import Tuile
taille_matriceX = 12#Y
taille_matriceY = 18#X
proba_roche = 15  # en %
proba_mer = 5
proba_foret = 15
proba_desert = 10
proba_neige= 10
matricemapStorageInfo=[]

def tirer_mer(matriceMap, i, j):
    temp = random.randint(1, 100)
    if temp <= proba_mer + matriceMap[i][j].getProba_mer():
        matriceMap[i][j] = Tuile(3)
        majProba(matriceMap, i, j, 100, "mer")


def tirer_desert(matriceMap, i, j):
    temp = random.randint(1, 100)
    if temp <= proba_desert + matriceMap[i][j].getProba_desert():
        matriceMap[i][j] = Tuile(6)
        majProba(matriceMap, i, j, 100, "desert")

def tirer_foret(matriceMap, i, j):
    temp = random.randint(1, 100)
    if temp <= proba_foret + matriceMap[i][j].getProba_foret():
        matriceMap[i][j] = Tuile(4)
        majProba(matriceMap, i, j, 25, "foret")


def tirer_neige(matriceMap, i, j):
    temp = random.randint(1, 100)
    if temp <= proba_neige + matriceMap[i][j].getProba_neige():
        matriceMap[i][j] = Tuile(5)
        majProba(matriceMap, i, j, 25, "neige")

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
    global matricemapStorageInfo
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
        matriceMap[i][0] = Tuile(7)
        matriceMap[i][taille_matriceY-1] = Tuile(7)
    for i in range (taille_matriceY):
        matriceMap[0][i] = Tuile(7)
        matriceMap[taille_matriceX-1][i] = Tuile(7)

    for i in range(1, taille_matriceX-1):
        for j in range(1, taille_matriceY-1):
            a = random.randint(1, 3)
            if a == 1:
                tirer_foret(matriceMap, i, j)
                tirer_mer(matriceMap, i, j)
                tirer_desert(matriceMap, i, j)
                tirer_roche(matriceMap, i, j)
                tirer_neige(matriceMap, i, j)
            if a == 2:
                tirer_mer(matriceMap, i, j)
                tirer_roche(matriceMap, i, j)
                tirer_neige(matriceMap, i, j)
                tirer_foret(matriceMap, i, j)
                tirer_desert(matriceMap, i, j)
            if a == 3:
                tirer_desert(matriceMap, i, j)
                tirer_roche(matriceMap, i, j)
                tirer_foret(matriceMap, i, j)
                tirer_neige(matriceMap, i, j)
                tirer_mer(matriceMap, i, j)
    return matriceMap



def loadImg(matriceMap=[]):
    #fonction pour remplacer le plan de la map par des images
    matricemap = matriceMap[:]  # copie tout dans un nouvel espace mémoire.
    for i in range(len(matricemap)):
        for j in range(len(matricemap[i])):
            typeTemp = matricemap[i][j].getType()
            if typeTemp == 1:  # si Terre
                imgTemp = pygame.image.load("data/tuiles/1Terre.png")
            elif typeTemp == 2:#Roche
                imgTemp = pygame.image.load("data/tuiles/2Roche.png")
            elif typeTemp == 3:#eau
                if  random.randint(1, 2) ==1: 
                    imgTemp = pygame.image.load("data/tuiles/3EauClaire.png")
                else:
                    imgTemp = pygame.image.load("data/tuiles/3EauProfonde.png")
            elif typeTemp == 4:#Foret
                imgTemp = pygame.image.load("data/tuiles/4Foret.png")
            elif typeTemp == 5: #neige
                imgTemp = pygame.image.load("data/tuiles/5Neige.png")
            elif typeTemp == 6: #Desert
                imgTemp = pygame.image.load("data/tuiles/6Desert.png")
            elif typeTemp == 7: #Barriere
                imgTemp = pygame.image.load("data/tuiles/7Barriere.png")
            imgTemp = pygame.transform.scale(imgTemp, (150, 150))
            matricemap[i][j] = imgTemp
    return matricemap
