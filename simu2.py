

import random
import time
import numpy as np
import matplotlib.pyplot as plt
global seconde, nombreMob, tempsGeneral, tempsMinSpawn

tempsMinSpawn=3
def fonctionGolem(temps, tempsMinSpawn): 
    if temps<tempsMinSpawn:
        return 0
    
    return 1.7**((temps-tempsMinSpawn)/5)


def tirerMob(fonctionP):
    global tempsGeneral, nombreMob, tempsMinSpawn
    for i in range(random.randint(0,10)): #le nombre de tuile present autour du joueur
        reussi=random.randint(0,200)
        if reussi<fonctionP(tempsGeneral, tempsMinSpawn):
            nombreMob+=1
            
def faireUneSimulation(nombreDeMinuteSimu, f):
    global seconde, nombreMob, tempsGeneral
    seconde, nombreMob, tempsGeneral=0,0,0
    listesPlt=[[],[]]
    while tempsGeneral<nombreDeMinuteSimu:
        tirerMob(f)
        seconde+=1
        if seconde==60:
            seconde=0
            tempsGeneral+=1
            #print("a temps t=",tempsGeneral,"min, il y a eu", nombreMob, "mob qui ont spawn dans la derniere minute")
            listesPlt[0].append(tempsGeneral)
            listesPlt[1].append(nombreMob)
            nombreMob=0
    return listesPlt
    

listesPlt=faireUneSimulation(10, fonctionGolem)



plt.plot(listesPlt[0], listesPlt[1])

plt.show() # affiche la figure à l'écran