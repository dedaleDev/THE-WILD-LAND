import random
from tuile import Tuile
taille_matrice = 16

def tirer_mer():
    temp = random.randint(1,100)
    if temp<= proba_mer + matriceMap[i][j].getProba_mer() :
        matriceMap[i][j] = Tuile(3)
        majProba(matriceMap, i, j, 25, "mer")

def tirer_foret():
    temp = random.randint(1,100)
    if temp <= proba_foret + matriceMap[i][j].getProba_foret() :
        matriceMap[i][j] = Tuile(4)
        majProba(matriceMap, i, j, 25, "foret")


def tirer_roche():
    temp = random.randint(1,100)
    if temp<= proba_roche + matriceMap[i][j].getProba_roche() :
        matriceMap[i][j] = Tuile(2)
        majProba(matriceMap, i, j, 25, "roche")

def majProba(matriceMap, i, j, probaSup, nature):
    for x in range(-1,1):
        for y in range(-1, 1):
            if i+x<len(matriceMap) and j+y <len(matriceMap):
                if nature=="roche":
                    matriceMap[i+x][j+y].augmenterProba_roche(probaSup)
                if nature=="foret":
                    matriceMap[i+x][j+y].augmenterProba_foret(probaSup)
                if nature=="mer":
                    matriceMap[i+x][j+y].augmenterProba_mer(probaSup)

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
            a = random.randint(1,3)
            if a==1:
                tirer_foret()
                tirer_mer()
                tirer_roche()
            if a==2:
                tirer_mer()
                tirer_roche()
                tirer_foret()
            if a==3:
                tirer_roche()
                tirer_foret()
                tirer_mer()

    printMap(matriceMap)
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