

import random
import time
import numpy as np
import matplotlib.pyplot as plt
global seconde, nombreMob, tempsGeneral, tempsMinSpawn

tempsMinSpawnGolem=0
tempsMinSpawnOursin=0
def fonctionOursin(temps): 
    if temps<tempsMinSpawnOursin:
        return 0
    return temps/9
    return 1.7**((temps-tempsMinSpawnOursin)/7)

def fonctionKraken(temps): 
    if temps<tempsMinSpawnOursin:
        return 0
    return temps/9

def fonctionMage(temps):
    if temps<3:
        return 0
    return (temps-3)/5

def fonctionDragon(temps):
    if temps<8:
        return 0
    return (temps-8)/2

def fonctionYeti(temps):
    if temps<10:
        return 0
    return (temps-10)/4
    

def fonctionGolem(temps): 
    if temps<tempsMinSpawnGolem:
        return 0
    if temps>15:
        return -temps/4+10
    return temps/4
    return 1.7**((temps-tempsMinSpawnGolem)/6)


def tirerMob(fonctionP):
    global tempsGeneral, nombreMob, tempsMinSpawn
    for i in range(random.randint(0,10)): #le nombre de tuile present autour du joueur
        reussi=random.randint(0,500)
        
        if reussi<round(fonctionP(tempsGeneral)):
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

def faireMultipleSimulation(nombreDeMinuteSimu, f, nombreDeSimu):
    listeEnCours=faireUneSimulation(nombreDeMinuteSimu, f)
    listeSomme=listeEnCours[1][:]
    nombreTirage=1
    for i in range(nombreDeSimu):
        listeEnCours=faireUneSimulation(nombreDeMinuteSimu, f)
        for x in range(len(listeEnCours[1])):
            listeSomme[x]+=listeEnCours[1][x]
        nombreTirage+=1
    for i in range(len(listeSomme)):
        listeSomme[i]=listeSomme[i]/nombreTirage
    return [listeEnCours[0], listeSomme]
        

tempsPartie=30
"""listesPlt=faireUneSimulation(10, fonctionGolem)
listesPlt2=faireUneSimulation(10, fonctionOursin)"""
test=faireMultipleSimulation(tempsPartie, fonctionGolem, 100)
test2=faireMultipleSimulation(tempsPartie, fonctionOursin, 100)
test3=faireMultipleSimulation(tempsPartie, fonctionMage, 100)
test4=faireMultipleSimulation(tempsPartie, fonctionDragon, 100)
test4=faireMultipleSimulation(tempsPartie, fonctionDragon, 100)
test5=faireMultipleSimulation(tempsPartie, fonctionYeti, 100)
plt.step(test[0], test[1], label="golem",alpha=0.25)
plt.step(test[0], test2[1], label="oursin",alpha=0.25)
plt.step(test[0], test3[1], label="mage",alpha=0.25)
plt.step(test[0], test4[1], label="dragon",alpha=0.5)
plt.step(test[0], test5[1], label="yeti",alpha=1)
plt.legend()
"""plt.plot(listesPlt[0], listesPlt[1], label="golem")
plt.plot(listesPlt[0], listesPlt2[1], label="oursin")
"""
plt.show() # affiche la figure à l'écran