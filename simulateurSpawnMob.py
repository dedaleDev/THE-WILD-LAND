

import random
import time
global seconde, nombreMob, tempsGeneral
def fonction(temps): #Le temps doit etre egale a temps-tempsSpawnMin
    return temps/5


def tirerMob(fonctionP):
    global tempsGeneral, nombreMob
    for i in range(random.randint(0,10)): #le nombre de tuile present autour du joueur
        reussi=random.randint(0,200)
        if reussi<fonctionP(tempsGeneral):
            nombreMob+=1
            
def faireUneSimulation(nombreDeMinuteSimu):
    global seconde, nombreMob, tempsGeneral
    seconde, nombreMob, tempsGeneral=0,0,0
    while tempsGeneral<nombreDeMinuteSimu:
        tirerMob(fonction)
        seconde+=1
        if seconde==60:
            seconde=0
            tempsGeneral+=1
            print("a temps t=",tempsGeneral,"min, il y a eu", nombreMob, "mob qui ont spawn dans la derniere minute")
            nombreMob=0


faireUneSimulation(10)