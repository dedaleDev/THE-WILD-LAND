import random
from tuile import Tuile
taille_matrice = 16

def majProba(matriceMap, i, j, probaSup):
    for x in range(-1,1):
        for y in range(-1, 1):
            if i+x<len(matriceMap) and j+y <len(matriceMap):
                matriceMap[i+x][j+y].augmenterProba(probaSup)

def generation_matrice():
    #1 = terre
    #2 = roche
    #3 = mer
    #4 = foret
    proba_roche=6  #en %
    proba_mer = 4
    proba_foret = 4
    
    matriceMap = []
    for i in range(taille_matrice):
        matriceMap.append([0]*taille_matrice)
        
    
    
    for i in range(taille_matrice):
        for j in range(len(matriceMap[i])): 
            matriceMap[i][j] = Tuile(1) #initialisation d'une carte remplie de terre
    
    
    for i in range(taille_matrice):
        matriceMap[i][0] = Tuile(2)
        matriceMap[i][taille_matrice-1] = Tuile(2)
        matriceMap[0][i] = Tuile(2)
        matriceMap[taille_matrice-1][i] = Tuile(2)
    
    for i in range(1, taille_matrice-1):
        for j in range(1, taille_matrice-1):
            
            
            temp = random.randint(1,100)
            if temp<= proba_roche + matriceMap[i][j].getProba() :
                matriceMap[i][j] = Tuile(2)
                majProba(matriceMap, i, j, 75)
            
            temp = random.randint(1,100)
            if temp<= proba_mer + matriceMap[i][j].getProba() :
                matriceMap[i][j] = Tuile(3)
                majProba(matriceMap, i, j, 75)

            temp = random.randint(1,100)
            if temp <= proba_foret + matriceMap[i][j].getProba() :
                matriceMap[i][j] = Tuile(4)
                majProba(matriceMap, i, j, 75)

    printMap(matriceMap)
    return matriceMap

def printMap(matriceMap):
    for i in range(len(matriceMap)):
        print('\n')
        for j in range(len(matriceMap[0])):
            print(matriceMap[i][j].getProba(), ', ', end='')

generation_matrice()
