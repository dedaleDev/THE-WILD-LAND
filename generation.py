import random
taille_matrice = 64

def generation_matrice():
    #1 = terre
    #2 = roche
    #3 = mer
    #4 = foret
    proba_roche=6  #en %
    proba_mer = 4
    
    matriceMap = []
    for i in range(taille_matrice):
        matriceMap.append([0]*taille_matrice)
        
        
        
    for i in range(taille_matrice-1):
        for j in range(taille_matrice-1): 
            matriceMap[i][j] = 1
            
    
    for i in range(taille_matrice):
        matriceMap[i][0] = 2
        matriceMap[i][taille_matrice-1] = 2
        matriceMap[0][i] = 2
        matriceMap[taille_matrice-1][i] = 2
        
    for i in range(taille_matrice-1):
        for j in range(taille_matrice-1):
            temp = random.randint(1,100)
            if temp<= proba_roche :
                type = random.randint(1,2)
                if type == 1 :
                    roche1(matriceMap, i, j)
                if type == 2:
                    roche1(matriceMap, i, j)
            else :
                temp = random.randint(1,100)
                if temp<= proba_mer :
                    type = random.randint(1,2)
                    if type == 1 :
                        mer1(matriceMap, i, j)
                    if type == 2:
                        mer1(matriceMap, i, j)
                    


    print(matriceMap)
generation_matrice()
