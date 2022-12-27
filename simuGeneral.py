

import random
import time
import numpy as np
import matplotlib.pyplot as plt
import statistics
global seconde, nombreMob, tempsGeneral, tempsMinSpawn,tempsSansGolem
tempsSansGolem=-2
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
    return (temps-3)/6

def fonctionDragon(temps):
    if temps<8:
        return 0
    re = (temps-8)/2
    if re>4:
        return 4
    return re

def fonctionYeti(temps:int):
    if temps<10:
        return 0
    return (temps-10)/5
    
def bonusGolem(tempsSansGolem):#en minute
    
    return tempsSansGolem*0.5

def fonctionGolem(temps:int):
    global tempsSansGolem
    
    if temps<3:
        return 0
    if temps>15:
        re= -temps/2.5+10
        if re <1:
            return 1
        return re
    return temps/6+1+bonusGolem(tempsSansGolem)


def tirerMob(fonctionP):
    global tempsGeneral, nombreMob,seconde, tempsSansGolem
    reussi=random.randint(0,150)
    spawn=False
    s=tempsGeneral*60+seconde
    t=s/60
    if reussi<fonctionP(t):
        nombreMob+=1
        tempsSansGolem=0
        spawn=True
    return spawn

def faireUneSimulation(nombreDeMinuteSimu, f):
    global seconde, nombreMob, tempsGeneral, tempsSansGolem
    seconde, nombreMob, tempsGeneral=0,0,0
    listesPlt=[[],[]]
    spawnMinute=False
    while tempsGeneral<nombreDeMinuteSimu:
        spawn=tirerMob(f)
        seconde+=1
        if spawn:
            spawnMinute=True
        if seconde==60:
            seconde=0
            tempsGeneral+=1
            if not spawnMinute:
                tempsSansGolem+=1
                
                #print("pas de spawn a la min", tempsGeneral)
            spawnMinute=False
            #print("a temps t=",tempsGeneral,"min, il y a eu", nombreMob, "mob qui ont spawn dans la derniere minute")
            listesPlt[0].append(tempsGeneral)
            listesPlt[1].append(nombreMob)
            nombreMob=0
    return listesPlt

def faireMultipleSimulation(nombreDeMinuteSimu, f, nombreDeSimu):
    global tempsSansGolem
    #listeEnCours=faireUneSimulation(nombreDeMinuteSimu, f)
    listeSomme=[]#listeEnCours[1][:]
    nombreTirage=0
    
    listeValeurQuartiles={}
    for i in range(nombreDeMinuteSimu): #pour chaque point, on va chercher les quartiles
        listeValeurQuartiles[i]=[]
        listeSomme.append(0)
    
    for i in range(nombreDeSimu):
        tempsSansGolem=-2
        listeEnCours = faireUneSimulation(nombreDeMinuteSimu, f)
        
        
        
        
        for x in range(len(listeEnCours[1])):
            listeSomme[x]+=listeEnCours[1][x]
            listeValeurQuartiles[x].append(listeEnCours[1][x])
            
        nombreTirage+=1
    for i in range(len(listeSomme)):
        listeSomme[i]=listeSomme[i]/nombreTirage
    
    listepltQuartile=[]
    #for minute in listeValeurQuartiles:
        #l=statistics.quantiles(listeValeurQuartiles[minute],n=4)
        #listepltQuartile.append([l[0], l[-1]])
        

    return [listeEnCours[0], listeSomme, listepltQuartile]


tempsPartie=30
"""listesPlt=faireUneSimulation(10, fonctionGolem)
listesPlt2=faireUneSimulation(10, fonctionOursin)"""
nombrePartie=1
test=faireMultipleSimulation(tempsPartie, fonctionGolem, nombrePartie)
"""test2=faireMultipleSimulation(tempsPartie, fonctionOursin, nombrePartie)
test3=faireMultipleSimulation(tempsPartie, fonctionMage, nombrePartie)
test4=faireMultipleSimulation(tempsPartie, fonctionDragon, nombrePartie)
test4=faireMultipleSimulation(tempsPartie, fonctionDragon, nombrePartie)
test5=faireMultipleSimulation(tempsPartie, fonctionYeti, nombrePartie)"""
plt.plot(test[0], test[1],"D", label="golem",alpha=1)
#plt.plot(test[0], test[2], label="golemQuartile",alpha=1)
"""plt.step(test[0], test2[1], label="oursin",alpha=0.25)
plt.step(test[0], test3[1], label="mage",alpha=0.25)
plt.step(test[0], test4[1], label="dragon",alpha=0.5)
plt.step(test[0], test5[1], label="yeti",alpha=0.25)"""
plt.legend()




plt.show() # affiche la figure à l'écran