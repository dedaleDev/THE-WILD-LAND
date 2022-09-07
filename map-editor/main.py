from math import sqrt
import pygame
from pygame.locals import *
from button import Button
import os 
import filecmp
background_colour = (255, 0, 0)

pygame.init()
infoObject = pygame.display.Info()
screen = pygame.display.set_mode((infoObject.current_w, infoObject.current_h))

pygame.display.set_caption('editeur de map')

scaleInfo = infoObject.current_w/1.2

info  = pygame.image.load("data/infoBulle.png").convert_alpha()
diag = sqrt(infoObject.current_w**2+infoObject.current_h**2)
tailleInfoX = info.get_width()*0.0005*diag
tailleinfoY = info.get_height()*0.0005*diag
info = pygame.transform.scale(info, (tailleInfoX, tailleinfoY))
buttonSave = pygame.image.load("data/buttonSave.png").convert_alpha()
buttonSave = pygame.transform.scale(buttonSave,(buttonSave.get_width()/4,buttonSave.get_height()/4))
buttonErase = pygame.image.load("data/buttonErase.png").convert_alpha()
buttonErase = pygame.transform.scale(buttonErase,(buttonErase.get_width()/4,buttonErase.get_height()/4))
buttonLoad = pygame.image.load("data/buttonLoad.png").convert_alpha()
buttonLoad = pygame.transform.scale(buttonLoad,(buttonLoad.get_width()/4,buttonLoad.get_height()/4))
pygame.display.flip()
taille_matriceY = 25
taille_matriceX = 25
scale =diag//60
running = True
theMap=[]

export = Button((50,5),(200,42), 9)
importMap = Button((250,5),(200,42), "o")
erase = Button((infoObject.current_w-202,5),(200,42), "e")
for i in range(taille_matriceY):
        theMap.append([0]*taille_matriceX)





for j in range(taille_matriceY):
    for i in range(taille_matriceX):
        # initialisation d'une carte remplie de vide
        theMap[j][i] = Button((scale*i+scale, scale*j+scale),(scale,scale), 1)
        
for i in range(taille_matriceX):
        theMap[0][i] = Button((scale*i+scale, scale),(scale,scale),  7)
        theMap[taille_matriceY-1][i] = Button((scale*i+scale, scale*(taille_matriceY-1)+scale), (scale,scale), 7)

for i in range (taille_matriceY):
    theMap[i][0] = Button((scale, scale*i+scale),(scale,scale),  7)
    theMap[i][taille_matriceX-1] = Button((scale*(taille_matriceX-1)+scale, scale+scale*i),(scale,scale),  7)

def getColor(i):
    if i == 1:
        color= (145, 236, 0)
    if i == 2:
        color = (114, 114, 114)
    if i == 3:
        color = (45,130,223)
    if i == 4:
        color = (7, 152, 59)
    if i==5:
        color = (194,218,225)
    if i == 6:
        color = (246,182, 27)
    if i == 7:
        color = (177, 48, 19)
    return color

clock = pygame.time.Clock()
posSelect=(0,0)

def printMat(matriceMap):
    print("[", end='')
    for i in range(taille_matriceY):
        print()
        for j in range(taille_matriceX):
            if j==0:
                print("[", end ='')
            if j!=taille_matriceX-1:
                print(str(matriceMap[i][j].valeur)+',' ,end=' ')
            else :
                if i!=taille_matriceY-1:
                    print(str(matriceMap[i][j].valeur)+'],' ,end=' ')
                else :
                    print(str(matriceMap[i][j].valeur)+']' ,end=' ')
    print("]", end='')
    print("\n\nmerci d'avoir utilisé le generateur de map, la voici\n\n\n\n\n")



def stringMap(map) :
    listeSpawn = []
    string =""
    string += "[["
    for i in range(taille_matriceY):
        for j in range(taille_matriceX):
            if map[i][j].spawn:
                listeSpawn.append([j,i])
            if j==0:
                string += "["
            if j!=taille_matriceX-1:
                string += str(map[i][j].valeur)+ ","
            else :
                if i!=taille_matriceY-1:
                    string += str(map[i][j].valeur)+'],'
                else :
                    string += str(map[i][j].valeur)+']' 
    string += "],"
    #POINTS DE SPAWN
    string += str(listeSpawn)
    string += "]"
    return string


valEnCours=1
while running:
    
    screen.fill("white")
    for y in range(taille_matriceY):
        for x in range(taille_matriceX):  
            
            if not theMap[y][x].pressed:
                pygame.draw.rect(screen, getColor(theMap[y][x].valeur), pygame.Rect(scale*x+scale, scale*y+scale, scale, scale))
            else:
                posSelect = (scale*x+scale, scale*y+scale)
                pygame.draw.rect(screen, getColor(theMap[y][x].valeur), pygame.Rect(scale*x+scale, scale*y+scale, scale, scale))
                pygame.draw.rect(screen, (255,255,255), pygame.Rect(scale*x+scale, scale*y+scale, scale, scale),1)
            if theMap[y][x].spawn:
                pygame.draw.circle(screen, (255,255,255),(scale*x+scale+scale//2, scale*y+scale+scale//2), scale//4)

    screen.blit(buttonSave,(50,5))
    screen.blit(buttonLoad,(250,5))
    screen.blit(buttonErase,(infoObject.current_w-203,5))
    screen.blit(info, (infoObject.current_w-info.get_width()-100,100))
    
    pygame.display.flip()
    clock.tick(60)

    
    
    
    for event in pygame.event.get():
        if event.type==pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            fichierSuppr = 0
            if export.checkForInput(mouse) :#exporter map 
                nbMap = 0
                path = os.path.dirname(__file__)
                path = path[:-10] 
                path += "data/map/"
                for filename in os.listdir(path):
                    f = os.path.join(path, filename)
                    nbMap +=1
                nomMap = "map"+str(nbMap+1)+".txt"
                map = open(path+nomMap, "w+")
                map.write(stringMap(theMap))
                map.close()
                
                f = os.path.join(path, "map"+str(nbMap+1)+".txt")
                for filename in os.listdir(path):
                    f2 =  os.path.join(path, filename)
                    if filecmp.cmp(f,f2, False) and f!= f2:
                        fichierSuppr = f
                if fichierSuppr:
                    os.remove(fichierSuppr)    


            if erase.checkForInput(mouse) : #erase map 
                for j in range(taille_matriceY):
                    for i in range(taille_matriceX):
                        # initialisation d'une carte remplie de vide
                        theMap[j][i] = Button((scale*i+scale, scale*j+scale),(scale,scale), 1)
            
                for i in range(taille_matriceX):
                    theMap[0][i] = Button((scale*i+scale, scale),(scale,scale),  7)
                    theMap[taille_matriceY-1][i] = Button((scale*i+scale, scale*(taille_matriceY-1)+scale), (scale,scale), 7)

                for i in range (taille_matriceY):
                    theMap[i][0] = Button((scale, scale*i+scale),(scale,scale),  7)
                    theMap[i][taille_matriceX-1] = Button((scale*(taille_matriceX-1)+scale, scale+scale*i),(scale,scale),  7)


            for y in range(taille_matriceY):
                for x in range(taille_matriceX):
                    theMap[y][x].pressed = theMap[y][x].checkForInput(mouse)
                    if theMap[y][x].pressed:
                        if valEnCours == "spawn":
                            theMap[y][x].spawn = not theMap[y][x].spawn
                        else:
                            theMap[y][x].valeur = valEnCours 

        if event.type==pygame.KEYDOWN:
            if event.key == pygame.K_1:
                for y in range(taille_matriceY):
                    for x in range(taille_matriceX):
                        if theMap[y][x].pressed :
                            theMap[y][x].valeur=1
                            valEnCours = 1
            if event.key == pygame.K_2:
                for y in range(taille_matriceY):
                    for x in range(taille_matriceX):
                        if theMap[y][x].pressed :
                            theMap[y][x].valeur=2
                            valEnCours = 2
            if event.key == pygame.K_3:
                for y in range(taille_matriceY):
                    for x in range(taille_matriceX):
                        if theMap[y][x].pressed :
                            theMap[y][x].valeur=3
                            valEnCours = 3
            if event.key == pygame.K_4:
                for y in range(taille_matriceY):
                    for x in range(taille_matriceX):
                        if theMap[y][x].pressed :
                            theMap[y][x].valeur=4
                            valEnCours = 4
            if event.key == pygame.K_5:
                for y in range(taille_matriceY):
                    for x in range(taille_matriceX):
                        if theMap[y][x].pressed :
                            theMap[y][x].valeur=5
                            valEnCours = 5
            if event.key == pygame.K_6:
                for y in range(taille_matriceY):
                    for x in range(taille_matriceX):
                        if theMap[y][x].pressed :
                            theMap[y][x].valeur=6
                            valEnCours = 6
            if event.key == pygame.K_7:
                for y in range(taille_matriceY):
                    for x in range(taille_matriceX):
                        if theMap[y][x].pressed :
                            theMap[y][x].valeur=7
                            valEnCours = 7
            if event.key == pygame.K_s :
                for y in range(taille_matriceY):
                    for x in range(taille_matriceX):
                        if theMap[y][x].pressed :
                            theMap[y][x].spawn = not theMap[y][x].spawn
                            valEnCours = "spawn"
                            
        keys = keys=pygame.key.get_pressed()
        if keys[K_LALT] :
            for y in range(taille_matriceY):
                for x in range(taille_matriceX):
                    mouse = pygame.mouse.get_pos()
                    theMap[y][x].pressed = theMap[y][x].checkForInput(mouse)
                    if theMap[y][x].pressed:
                        if valEnCours == "spawn":
                            theMap[y][x].spawn = True
                        else:
                            theMap[y][x].valeur = valEnCours

        if event.type == pygame.QUIT:
            running = False