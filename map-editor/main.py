import pygame
from pygame.locals import *
import sys
from button import Button

background_colour = (255, 0, 0)

pygame.init()
screen = pygame.display.set_mode((1500, 800))


pygame.display.set_caption('editeur de map')
info  = pygame.image.load("infoBulle.png").convert_alpha()
info = pygame.transform.scale(info, (info.get_width()/1.5,info.get_height()/1.5))
pygame.display.flip()
taille_matriceY = 25
taille_matriceX = 25
running = True
theMap=[]

for i in range(taille_matriceY):
        theMap.append([0]*taille_matriceX)





for j in range(taille_matriceY):
    for i in range(taille_matriceX):
        # initialisation d'une carte remplie de vide
        theMap[j][i] = Button((30*i+30, 30*j+30), 1)
        
for i in range(taille_matriceX):
        theMap[0][i] = Button((30*i+30, 30), 7)
        theMap[taille_matriceY-1][i] = Button((30*i+30, 30*(taille_matriceY-1)+30), 7)

for i in range (taille_matriceY):
    theMap[i][0] = Button((30, 30*i+30), 7)
    theMap[i][taille_matriceX-1] = Button((30*(taille_matriceX-1)+30, 30+30*i), 7)



    
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

select = pygame.image.load("selection.png")
select = pygame.transform.scale(select,(30,30,))
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
valEnCours=1
while running:
    
    screen.fill("white")
    for y in range(taille_matriceY):
        for x in range(taille_matriceX):  
            
            if not theMap[y][x].pressed:
                pygame.draw.rect(screen, getColor(theMap[y][x].valeur), pygame.Rect(30*x+30, 30*y+30, 30, 30))
            else:
                posSelect = (30*x+30, 30*y+30)
                pygame.draw.rect(screen, getColor(theMap[y][x].valeur), pygame.Rect(30*x+30, 30*y+30, 30, 30))

    screen.blit(select, posSelect)
    screen.blit(info, (1500-600,100))
    
    pygame.display.flip()
    clock.tick(60)

    
    
    
    for event in pygame.event.get():
        if event.type==pygame.MOUSEBUTTONDOWN:
            for y in range(taille_matriceY):
                for x in range(taille_matriceX):
                    mouse = pygame.mouse.get_pos()
                    theMap[y][x].pressed = theMap[y][x].checkForInput(mouse)
                    if theMap[y][x].pressed:
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
                            valEnCours =7
            if event.key == pygame.K_9:
                printMat(theMap)
        keys = keys=pygame.key.get_pressed()
        if keys[K_LALT] :
            for y in range(taille_matriceY):
                for x in range(taille_matriceX):
                    mouse = pygame.mouse.get_pos()
                    theMap[y][x].pressed = theMap[y][x].checkForInput(mouse)
                    if theMap[y][x].pressed:
                        theMap[y][x].valeur = valEnCours
        if event.type == pygame.QUIT:
            running = False


            
            
