import random
import pygame
from tuile import Tuile
taille_matriceX = 12#Y
taille_matriceY = 18#X
proba_roche = 15  # en %
proba_mer = 5
proba_foret = 15
proba_desert = 10
proba_neige= 5

nombre_biome = 5




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
        majProba(matriceMap, i, j, -100, "neige")

def tirer_foret(matriceMap, i, j):
    temp = random.randint(1, 100)
    if temp <= proba_foret + matriceMap[i][j].getProba_foret():
        matriceMap[i][j] = Tuile(4)
        majProba(matriceMap, i, j, 50, "foret")


def tirer_neige(matriceMap, i, j):
    temp = random.randint(1, 100)
    if temp <= proba_neige + matriceMap[i][j].getProba_neige():
        matriceMap[i][j] = Tuile(5)
        #majProba(matriceMap, i, j, 25, "neige")
        majProba(matriceMap, i, j, -100, "desert")

def tirer_roche(matriceMap, i, j):
    temp = random.randint(1, 100)
    if temp <= proba_roche + matriceMap[i][j].getProba_roche():
        matriceMap[i][j] = Tuile(2)
        majProba(matriceMap, i, j, 25, nature= "roche")
        majProba(matriceMap, i, j, 100, nature= "neige")
        majProba(matriceMap, i, j, -100, "desert")

def tirer_biome(type, matriceMap, i, j):
    if type==2:
        tirer_roche(matriceMap, i, j)
    elif type == 3:
        tirer_mer(matriceMap, i, j)
    elif type == 4:
        tirer_foret(matriceMap, i, j)
    elif type == 5:
        tirer_neige(matriceMap, i, j)
    elif type == 6:
        tirer_desert(matriceMap, i, j)

def majProba(matriceMap, i, j, probaSup, nature):
    liste =[-1,1]
    for x in range(-1, 1):
        for y in range(-1, 1):
            if i+x < len(matriceMap) and j+y < len(matriceMap[0]):
                if nature == "roche":
                    matriceMap[i+x][j+y].augmenterProbaRoche(probaSup)
                if nature == "foret":
                    matriceMap[i+x][j+y].augmenterProbaForet(probaSup)
                if nature == "mer":
                    matriceMap[i+x][j+y].augmenterProbaMer(probaSup)
                if nature == "desert":
                    matriceMap[i+x][j+y].augmenterProbaDesert(probaSup)
                if nature == "neige" :
                    matriceMap[i+x][j+y].augmenterProbaNeige(probaSup)


def generation_matrice():
    #1 = terre
    #2 = roche
    #3 = mer
    #4 = foret
    #5 = neige
    #6 = desert
    
    liste_index = []
    for i in range(1, taille_matriceX-1):
        for j in range(1, taille_matriceY-1):
            liste_index.append((i,j))

    matriceMap = []
    for i in range(taille_matriceX):
        matriceMap.append([0]*taille_matriceY)

    for i in range(taille_matriceX):
        for j in range(len(matriceMap[i])):
            # initialisation d'une carte remplie de vide
            matriceMap[i][j] = Tuile(1)

    for i in range(taille_matriceX):
        matriceMap[i][0] = Tuile(7)
        matriceMap[i][taille_matriceY-1] = Tuile(7)
    for i in range (taille_matriceY):
        matriceMap[0][i] = Tuile(7)
        matriceMap[taille_matriceX-1][i] = Tuile(7)

    
    
    while len(liste_index) != 0: 
        num_case = random.randint(0, len(liste_index)-1)
        
        i=liste_index[num_case][0]
        j=liste_index[num_case][1]
        liste_index.pop(num_case)
        
        
        liste_type = [2,3,4,5,6]
        
        while len(liste_type)!=0: 
            biome = random.randint(0, len(liste_type)-1)
            tirer_biome(liste_type[biome], matriceMap, i, j)
            liste_type.pop(biome)
            print(liste_type)
    printMat(matriceMap)
    return matriceMap

def printMat(matriceMap):
    for i in range(len(matriceMap)):
        print("\n")
        for j in range(len(matriceMap[0])):
            print(matriceMap[i][j].getProba_desert(),", ", end='')

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