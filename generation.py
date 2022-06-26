import copy
from operator import xor
import random
from tuile import Tuile
taille_matriceX = 25
taille_matriceY = 10


proba_roche = random.randint(10,15) # en %
proba_mer = random.randint(3,15)
proba_desert = random.randint(5,15)
if proba_mer<=6:
    proba_desert+=5
proba_foret = random.randint(10,15)
proba_neige= 0


nombre_biome = 5
GIGALISTE=[]
liste_index = []




def tirer_mer(matriceMap, i, j, game):
    temp = random.randint(1, 100)
    if temp <= proba_mer + matriceMap[j][i].getProbaMer():
        matriceMap[j][i] = Tuile(3, i, j, game)
        majProba(matriceMap, i, j, 70, "mer")
        return True
    return False


def tirer_desert(matriceMap, i, j, game):
    temp = random.randint(1, 100)
    if temp <= proba_desert + matriceMap[j][i].getProbaDesert() and matriceMap[j][i].getAutoriserDesert():
        matriceMap[j][i] = Tuile(6, i, j, game)
        majProba(matriceMap, i, j, 60, "desert")
        return True
    return False
        

def tirer_foret(matriceMap, i, j, game):
    temp = random.randint(1, 100)
    if temp <= proba_foret + matriceMap[j][i].getProbaForet():
        matriceMap[j][i] = Tuile(4, i, j, game)
        majProba(matriceMap, i, j, 30, "foret")
        return True
    return False


def tirer_neige(matriceMap, i, j, game) :
    temp = random.randint(1, 100)
    if temp <= proba_neige + matriceMap[j][i].getProbaNeige() and matriceMap[j][i].getAutoriserNeige():
        matriceMap[j][i] = Tuile(5, i, j, game)
        majNeigeAutoriser(matriceMap, i, j)
        majProba(matriceMap, i, j, 15, "neige")
        majDesertInterdire(matriceMap, i, j)
        return True
    return False

def tirer_roche(matriceMap, i, j, game):
    temp = random.randint(1, 100)
    if temp <= proba_roche + matriceMap[j][i].getProbaRoche():
        matriceMap[j][i] = Tuile(2, i, j, game)
        majProba(matriceMap, i, j, 25, nature= "roche")
        majNeigeAutoriser(matriceMap, i,j)
        majDesertInterdire(matriceMap, i,j)
        majProba(matriceMap, i,j,50, "neige")
        return True
    return False
        

def tirer_biome(type, matriceMap, i, j, game):
    if type==2:
        tire=tirer_roche(matriceMap, i, j, game)
    elif type == 3:
        tire=tirer_mer(matriceMap, i, j, game)
    elif type == 4:
        tire=tirer_foret(matriceMap, i, j, game)
    elif type == 5:
        tire=tirer_neige(matriceMap, i, j, game)
    elif type == 6:
        tire=tirer_desert(matriceMap, i, j, game)
    return tire

def majProba(matriceMap, i, j, probaSup, nature):
    for y in range(-1, 2):
        for x in range(-1, 2):
            if i+x < taille_matriceX and j+y < taille_matriceY and i+x>= 0 and y+j>=0  and not (y==-1 and x == -1):
                                                                                        #SUPPRESSION DE PROBA EN HAUT A GAUCHE
                if nature == "roche":
                    matriceMap[j+y][i+x].augmenterProbaRoche(probaSup)
                if nature == "foret":
                    matriceMap[j+y][i+x].augmenterProbaForet(probaSup)
                if nature == "mer":
                    matriceMap[j+y][i+x].augmenterProbaMer(probaSup)
                if nature == "desert":
                    matriceMap[j+y][i+x].augmenterProbaDesert(probaSup)
                if nature == "neige" :
                    matriceMap[j+y][i+x].augmenterProbaNeige(probaSup)


def majNeigeAutoriser(matriceMap, i, j):
    for y in range(-1, 2):
        for x in range(-1, 2):
            if i+x < taille_matriceX and j+y < taille_matriceY and i+x>= 0 and y+j>=0:
                matriceMap[j+y][i+x].setAutoriserNeige()


def majDesertInterdire(matriceMap, i, j):
    for y in range(-1, 2):
        for x in range(-1, 2):
            if i+x <  taille_matriceX and i+x >=0 and j+y < taille_matriceY and j+y >= 0:
                
                matriceMap[j+y][i+x].setInterdireDesert()
                if matriceMap[j+y][i+x].getType()==6:
                    matriceMap[j+y][i+x].setType(1)
                    matriceMap[j+y][i+x].imageO = matriceMap[j+y][i+x].openImg(1)


def generation_matrice(game):
    #1 = terre
    #2 = roche
    #3 = mer
    #4 = foret
    #5 = neige
    #6 = desert
    
    
    for i in range(1, taille_matriceX-1):
        for j in range(1, taille_matriceY-1):
            liste_index.append((j,i))

    matriceMap = []

    for i in range(taille_matriceY):
        matriceMap.append([0]*taille_matriceX)


    for j in range(taille_matriceY):
        for i in range(taille_matriceX):
            # initialisation d'une carte remplie de vide
            matriceMap[j][i] = Tuile(1, i, j, game)

    for i in range(taille_matriceX):
        matriceMap[0][i] = Tuile(7, i, 0, game)
        matriceMap[taille_matriceY-1][i] = Tuile(7, i, taille_matriceY-1, game)

    for i in range (taille_matriceY):
        matriceMap[i][0] = Tuile(7, 0, i, game)
        matriceMap[i][taille_matriceX-1] = Tuile(7,taille_matriceX-1, i, game)


    
    while len(liste_index) != 0:
        num_case = random.randint(0, len(liste_index)-1)
        y=liste_index[num_case][0]
        x=liste_index[num_case][1]
        liste_index.pop(num_case)
        
        
        liste_type = [2,3,4,5,6]
        
        Tire=False
        while len(liste_type)!=0 and not Tire:
            biome = random.randint(0, len(liste_type)-1)
            Tire = tirer_biome(liste_type[biome], matriceMap, x, y, game)
            liste_type.pop(biome)
        #GIGALISTE.append(copy.deepcopy(matriceMap))

    #printMat(matriceMap)
    return (matriceMap)

def printMat(matriceMap):
    for i in range(taille_matriceY):
        print("\n")
        for j in range(taille_matriceX):
            print("(",matriceMap[i][j].rect.x, matriceMap[i][j].rect.y,")",end=' ')
    print("fin\n\n\n\n\n")