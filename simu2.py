

import random
import time
import numpy as np
import matplotlib.pyplot as plt
global seconde, nombreMob, tempsGeneral, tempsMinSpawn

tempsMinSpawn=3
def fonctionGolem(temps): 
    if temps<2:
        return 0
    if temps>15:
        re= -temps/2.5+10
        if re <1:
            return 1
        return re
    return temps/6+1

def convertir_temps(temps_en_secondes):
  minutes = temps_en_secondes // 60
  secondes = temps_en_secondes % 60
  return minutes, secondes

def tirerMob(fonctionP):
    global tempsGeneral, nombreMob, tempsMinSpawn,seconde
    reussi=random.randint(0,150)
    s=tempsGeneral*60+seconde
    t=s/60

    if reussi<fonctionP(t):
        nombreMob+=1
        print("un mob spawn a t=",convertir_temps(s)[0],":", convertir_temps(s)[1])

def faireUneSimulation(nombreDeMinuteSimu, f):
    global seconde, nombreMob, tempsGeneral,seconde
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
    

listesPlt=faireUneSimulation(20, fonctionGolem)



plt.step(listesPlt[0], listesPlt[1])

plt.show() # affiche la figure à l'écran