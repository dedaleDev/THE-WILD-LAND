import math
import pathlib
import webbrowser
import pygame, sys
from button import Button
import pygame_gestion
import aideCSV
import os
import mainEditor
from map import MapEditor
from scaleBar import ScrollBar

global diagonalEcran, scaleButton, tailleEcran, taillePolice, scaleButtonMap, BG, SCREEN, scaleButtonBarre, scaleButtonR

transi = 7
def get_font(size):
    return pygame.font.Font("data/menu/font.ttf", size)



def optionPartie():
    global diagonalEcran, scaleButton, tailleEcran, taillePolice, scaleButtonMap, BG, SCREEN, scaleButtonBarre, scaleButtonR
    mapPropose = []
    path = os.path.dirname(__file__)
    fondMap =pygame.image.load("data/menu/fondMap.png").convert_alpha()
    fondMap = pygame.transform.scale(fondMap, (diagonalEcran*fondMap.get_width()*0.0002, diagonalEcran*fondMap.get_height()*0.0002))
    fissure = pygame.image.load("data/menu/fissure.png").convert_alpha()
    fissure = pygame.transform.scale(fissure, (diagonalEcran*fissure.get_width()*0.000235, diagonalEcran*fissure.get_height()*0.000235))
    path += "/data/map/"
    al=0
    indiceMap=None
    for filename in os.listdir(path):
        if str(filename)[-4:]== ".txt" : 
            
            f = str(pathlib.Path(__file__).parent.absolute())+"/data/map/"+  filename
            map = open(f, "r")
            listeType, pointSpawnTemp = eval(map.read())
            map.close()
            if str(filename)=="aleatoire.txt":
                indiceMap=al
            al+=1
            if pathlib.Path(map.name).stem=="aleatoire" and aideCSV.valCorrespondante("langue")=="en":
                mapPropose.append(MapEditor(listeType, None, pointSpawnTemp, "random"))
            else:
                mapPropose.append(MapEditor(listeType, None, pointSpawnTemp, pathlib.Path(map.name).stem)) #dernier argument = nom du fichier sans .txt
                
    
    if indiceMap==None:
        indiceMap = 0
    posYMap = 0.6
    posYDiff = 0.3
    posYMapChoix = 0.47
    posYMapTXT=0.655
    posYDiffTXT=0.3
    continu = True
    back = False
    if aideCSV.valCorrespondante("langue")=="fr":
        OPTIONS_BACK = Button(image=pygame.transform.scale(pygame.image.load("data/menu/backButton.png").convert_alpha(), (scaleButton[0]//2, scaleButton[1]//2)), pos=(tailleEcran[0]*1.5/10, tailleEcran[1]*1/1.1), 
                        text_input="retour", font=get_font(taillePolice//2), base_color="white", hovering_color="#999999")
        OPTIONS_GO = Button(image=pygame.transform.scale(pygame.image.load("data/menu/backButton.png").convert_alpha(), (scaleButton[0]//2, scaleButton[1]//2)), pos=(tailleEcran[0]*9/10, tailleEcran[1]*1/1.1), 
                        text_input="demarrer", font=get_font(taillePolice//2), base_color="white", hovering_color="#999999")
        
        
        
        OPTIONS_TEXT = get_font(taillePolice).render(" Nouvelle partie ", True, "Black")
        PETITE_TEXT = get_font(taillePolice//5).render(" Petite ", True, "Black")
        MOYENNE_TEXT = get_font(taillePolice//4).render(" Moyenne ", True, "Black")
        GRANDE_TEXT = get_font(taillePolice//3).render(" Grande ", True, "Black")
        EXTREME_TEXT = get_font(taillePolice//2).render(" Extreme ", True, "Black")
        PETITEDIFF_TEXT = get_font(taillePolice//5).render(" Facile ", True, "Black")
        MOYENNEDIFF_TEXT = get_font(taillePolice//4).render(" Normale ", True, "Black")
        GRANDEDIFF_TEXT = get_font(taillePolice//3).render(" Difficile ", True, "Black")
        EXTREMEDIFF_TEXT = get_font(taillePolice//2).render(" Extreme ", True, "Black")
        MAP_TEXT = get_font(taillePolice//2).render(" Taille de la carte ", True, "Black")
        DIFF_TEXT = get_font(taillePolice//2).render(" Difficulte ", True, "Black")
    else:
        OPTIONS_BACK = Button(image=pygame.transform.scale(pygame.image.load("data/menu/backButton.png").convert_alpha(), (scaleButton[0]//2, scaleButton[1]//2)), pos=(tailleEcran[0]*1.5/10, tailleEcran[1]*1/1.1), 
                        text_input="back", font=get_font(taillePolice//2), base_color="white", hovering_color="#999999")
        OPTIONS_GO = Button(image=pygame.transform.scale(pygame.image.load("data/menu/backButton.png").convert_alpha(), (scaleButton[0]//2, scaleButton[1]//2)), pos=(tailleEcran[0]*9/10, tailleEcran[1]*1/1.1), 
                        text_input="go", font=get_font(taillePolice//2), base_color="white", hovering_color="#999999")
        
        OPTIONS_TEXT = get_font(taillePolice).render(" New game ", True, "Black")
        PETITE_TEXT = get_font(taillePolice//5).render(" Little ", True, "Black")
        MOYENNE_TEXT = get_font(taillePolice//4).render(" Medium ", True, "Black")
        GRANDE_TEXT = get_font(taillePolice//3).render(" Big ", True, "Black")
        EXTREME_TEXT = get_font(taillePolice//2).render(" Huge ", True, "Black")
        PETITEDIFF_TEXT = get_font(taillePolice//5).render(" Easy ", True, "Black")
        MOYENNEDIFF_TEXT = get_font(taillePolice//4).render(" Normal ", True, "Black")
        GRANDEDIFF_TEXT = get_font(taillePolice//3).render(" Hard ", True, "Black")
        EXTREMEDIFF_TEXT = get_font(taillePolice//2).render(" Hardcore ", True, "Black")
        MAP_TEXT = get_font(taillePolice//2).render(" Map size ", True, "Black")
        DIFF_TEXT = get_font(taillePolice//2).render(" Difficulty ", True, "Black")
    OPTIONS_RECT = OPTIONS_TEXT.get_rect()
    OPTIONS_RECT.x = tailleEcran[0]*0.3/10
    OPTIONS_RECT.y = tailleEcran[1]*0.6/10
    
    PETITE_RECT = PETITE_TEXT.get_rect(center=(tailleEcran[0]*1.21/10, tailleEcran[1]*posYMapTXT-5))
    
    
    MOYENNE_RECT = MOYENNE_TEXT.get_rect(center=((tailleEcran[0]*1.25/10+tailleEcran[0]*0.5/10, tailleEcran[1]*posYMapTXT-5)))
    
    
    GRANDE_RECT = GRANDE_TEXT.get_rect(center=(tailleEcran[0]*1.25/10+tailleEcran[0]*1.3/10, tailleEcran[1]*posYMapTXT-5))
    
    
    EXTREME_RECT = EXTREME_TEXT.get_rect(center=(tailleEcran[0]*1.25/10+tailleEcran[0]*2.45/10, 0.06+tailleEcran[1]*posYMapTXT-5))
    
    
    PETITEDIFF_RECT = PETITEDIFF_TEXT.get_rect(center=(tailleEcran[0]*1/7, tailleEcran[1]*posYDiffTXT))
    
    
    MOYENNEDIFF_RECT = MOYENNEDIFF_TEXT.get_rect(center=((tailleEcran[0]*1/7+tailleEcran[0]*10//100, tailleEcran[1]*posYDiffTXT)))
    
    
    GRANDEDIFF_RECT = GRANDEDIFF_TEXT.get_rect(center=(tailleEcran[0]*1/7+tailleEcran[0]*20//100, tailleEcran[1]*posYDiffTXT))
    
    
    EXTREMEDIFF_RECT = EXTREMEDIFF_TEXT.get_rect(center=(tailleEcran[0]*1/7+tailleEcran[0]*30//100, 0.06+tailleEcran[1]*posYDiffTXT))
    
    
    
    MAP_RECT = OPTIONS_TEXT.get_rect()
    MAP_RECT.x = tailleEcran[0]*1/10
    MAP_RECT.y = tailleEcran[1]*4.5/10
    
    
    DIFF_RECT = OPTIONS_TEXT.get_rect()
    DIFF_RECT.x = tailleEcran[0]*1/10
    DIFF_RECT.y = tailleEcran[1]*2/10
    
    tailleMap = 25
    
    
    gaucheMap = Button(image=pygame.transform.scale(pygame.image.load("data/menu/angle-left.png").convert_alpha(), (scaleButtonMap[0]//4-scaleButtonMap[0]//7, scaleButtonMap[1]//4-scaleButtonMap[1]//7)), pos=(tailleEcran[0]*6.15/10, tailleEcran[1]*posYMapChoix), 
                    text_input="", font=get_font(taillePolice//2), base_color="white", hovering_color="#999999")
    
    droiteMap = Button(image=pygame.transform.scale(pygame.image.load("data/menu/angle-right.png").convert_alpha(), (scaleButtonMap[0]//4-scaleButtonMap[0]//7, scaleButtonMap[1]//4-scaleButtonMap[1]//7)), pos=(tailleEcran[0]*8.7/10, tailleEcran[1]*posYMapChoix), 
                    text_input="", font=get_font(taillePolice//2), base_color="white", hovering_color="#999999")
    
    Map = Button(image=mapPropose[indiceMap].image, pos=(tailleEcran[0]*7.5/10, tailleEcran[1]*posYMapChoix), 
                    text_input=mapPropose[indiceMap].nom, font=get_font(taillePolice//2), base_color="black", hovering_color="#999999", listeType=mapPropose[indiceMap].listeType)
    
    Map.image=None #A cause d'un leger bug d'initialisation d'un bouton, pas important


    miniMap = Button(image=pygame.transform.scale(pygame.image.load("data/menu/backButtonMap.png").convert_alpha(), (scaleButtonMap[0]//4-scaleButtonMap[0]//7, scaleButtonMap[1]//4-scaleButtonMap[1]//7)), pos=(tailleEcran[0]*1.21/10, tailleEcran[1]*posYMap), 
                    text_input="", font=get_font(taillePolice//2), base_color="white", hovering_color="#999999")
    
    moyenneMap = Button(image=pygame.transform.scale(pygame.image.load("data/menu/backButtonMap.png").convert_alpha(), (scaleButtonMap[0]//4-scaleButtonMap[0]//10, scaleButtonMap[1]//4-scaleButtonMap[1]//10)), pos=(tailleEcran[0]*1.25/10+tailleEcran[0]*0.5/10, tailleEcran[1]*posYMap-tailleEcran[1]*0.01), 
                    text_input="", font=get_font(taillePolice//2), base_color="white", hovering_color="#999999")
    
    grandeMap = Button(image=pygame.transform.scale(pygame.image.load("data/menu/backButtonMap.png").convert_alpha(), (scaleButtonMap[0]//4, scaleButtonMap[1]//4)), pos=(tailleEcran[0]*1.25/10+tailleEcran[0]*1.3/10, tailleEcran[1]*posYMap-tailleEcran[1]*0.035), 
                    text_input="", font=get_font(taillePolice//2), base_color="white", hovering_color="#999999")
                  
    ExtremeMap = Button(image=pygame.transform.scale(pygame.image.load("data/menu/backButtonMap.png").convert_alpha(), (scaleButtonMap[0]//4+scaleButtonMap[0]//10, scaleButtonMap[1]//4+scaleButtonMap[1]//10)), pos=(tailleEcran[0]*1.25/10+tailleEcran[0]*2.45/10, tailleEcran[1]*posYMap-tailleEcran[1]*0.06), 
                    text_input="", font=get_font(taillePolice//2), base_color="white", hovering_color="#999999")
    miniMap.image.set_alpha(150)
    moyenneMap.image.set_alpha(255)
    grandeMap.image.set_alpha(150)
    ExtremeMap.image.set_alpha(150)


    diff = "facile"

    facile = Button(image=pygame.transform.scale(pygame.image.load("data/menu/facile.png").convert_alpha(), (scaleButtonMap[0]//4, scaleButtonMap[1]//4)), pos=(tailleEcran[0]*1/7, tailleEcran[1]*posYDiff), 
                    text_input="", font=get_font(taillePolice//2), base_color="white", hovering_color="#999999")
    normal = Button(image=pygame.transform.scale(pygame.image.load("data/menu/normal.png").convert_alpha(), (scaleButtonMap[0]//4, scaleButtonMap[1]//4)), pos=(tailleEcran[0]*1/7+tailleEcran[0]*10//100, tailleEcran[1]*posYDiff), 
                    text_input="", font=get_font(taillePolice//2), base_color="white", hovering_color="#999999")
    difficile = Button(image=pygame.transform.scale(pygame.image.load("data/menu/difficile.png").convert_alpha(), (scaleButtonMap[0]//4, scaleButtonMap[1]//4)), pos=(tailleEcran[0]*1/7+tailleEcran[0]*20//100, tailleEcran[1]*posYDiff), 
                    text_input="", font=get_font(taillePolice//2), base_color="white", hovering_color="#999999")
    extreme = Button(image=pygame.transform.scale(pygame.image.load("data/menu/extreme.png").convert_alpha(), (scaleButtonMap[0]//4, scaleButtonMap[1]//4)), pos=(tailleEcran[0]*1/7+tailleEcran[0]*30//100, tailleEcran[1]*posYDiff), 
                text_input="", font=get_font(taillePolice//2), base_color="white", hovering_color="#999999")
    facile.image.set_alpha(255)
    normal.image.set_alpha(150)
    difficile.image.set_alpha(150)
    extreme.image.set_alpha(150)
    mapChoisie = mapPropose[indiceMap].listeType
    pointSpawn = mapPropose[indiceMap].listePointSpawn
    clock = pygame.time.Clock()
    while continu:
        clock.tick(60)
        if BG.get_alpha()>80:
            
            BG.set_alpha(BG.get_alpha()-transi)
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")
        SCREEN.blit(BG, (0,0))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)
        SCREEN.blit(MAP_TEXT, MAP_RECT)
        SCREEN.blit(DIFF_TEXT, DIFF_RECT)
        SCREEN.blit(PETITE_TEXT, PETITE_RECT)
        SCREEN.blit(MOYENNE_TEXT, MOYENNE_RECT)
        SCREEN.blit(GRANDE_TEXT, GRANDE_RECT)
        SCREEN.blit(EXTREME_TEXT, EXTREME_RECT)
        
        if diff!="facile" and facile.pressed2:
            SCREEN.blit(PETITEDIFF_TEXT, PETITEDIFF_RECT)
        if diff!="normale" and normal.pressed2:
            SCREEN.blit(MOYENNEDIFF_TEXT, MOYENNEDIFF_RECT)
        
        
        if diff!="difficile" and difficile.pressed2:
            SCREEN.blit(GRANDEDIFF_TEXT, GRANDEDIFF_RECT)
        if diff!="extreme" and extreme.pressed2:
            SCREEN.blit(EXTREMEDIFF_TEXT, EXTREMEDIFF_RECT)
        
        OPTIONS_GO.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        
        
        OPTIONS_GO.update(SCREEN)
        OPTIONS_BACK.update(SCREEN)
        grandeMap.update(SCREEN)
        moyenneMap.update(SCREEN)
        ExtremeMap.update(SCREEN)
        miniMap.update(SCREEN)
        facile.update(SCREEN)
        normal.update(SCREEN)
        difficile.update(SCREEN)
        extreme.update(SCREEN)
        
        
        SCREEN.blit(fondMap, (56/100*pygame.display.Info().current_w, 25 /100*pygame.display.Info().current_h))
        Map.update(SCREEN)
        if Map.listeType:
            SCREEN.blit(fissure, (60.2/100*pygame.display.Info().current_w, 22.6 /100*pygame.display.Info().current_h))
        SCREEN.blit(Map.text, (58/100*pygame.display.Info().current_w, 27 /100*pygame.display.Info().current_h))
        droiteMap.update(SCREEN)
        gaucheMap.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    continu=False
                    back=True
                    
                if OPTIONS_GO.checkForInput(OPTIONS_MOUSE_POS):
                    continu=False
                    back=False
                
                if miniMap.checkForInput(OPTIONS_MOUSE_POS):
                
                    miniMap.image.set_alpha(255)
                    tailleMap = 10
                    moyenneMap.image.set_alpha(150)
                    grandeMap.image.set_alpha(150)
                    ExtremeMap.image.set_alpha(150)
                    
                if moyenneMap.checkForInput(OPTIONS_MOUSE_POS):
                    tailleMap= 25
                    miniMap.image.set_alpha(150)
                    moyenneMap.image.set_alpha(255)
                    grandeMap.image.set_alpha(150)
                    ExtremeMap.image.set_alpha(150)
                if grandeMap.checkForInput(OPTIONS_MOUSE_POS):
                    tailleMap = 30
                    miniMap.image.set_alpha(150)
                    moyenneMap.image.set_alpha(150)
                    grandeMap.image.set_alpha(255)
                    ExtremeMap.image.set_alpha(150)
                if ExtremeMap.checkForInput(OPTIONS_MOUSE_POS):
                    tailleMap=40
                    miniMap.image.set_alpha(150)
                    moyenneMap.image.set_alpha(150)
                    grandeMap.image.set_alpha(150)
                    ExtremeMap.image.set_alpha(255)
                ##DIFFICULTE
                    
                if facile.checkForInput(OPTIONS_MOUSE_POS):
                    diff = "facile"
                    facile.image.set_alpha(255)
                    normal.image.set_alpha(150)
                    difficile.image.set_alpha(150)
                    extreme.image.set_alpha(150)
                    
                if normal.checkForInput(OPTIONS_MOUSE_POS):
                    diff = "normal"
                    facile.image.set_alpha(150)
                    normal.image.set_alpha(255)
                    difficile.image.set_alpha(150)
                    extreme.image.set_alpha(150)
                if difficile.checkForInput(OPTIONS_MOUSE_POS):
                    diff = "difficile"
                    facile.image.set_alpha(150)
                    normal.image.set_alpha(150)
                    difficile.image.set_alpha(255)
                    extreme.image.set_alpha(150)
                if extreme.checkForInput(OPTIONS_MOUSE_POS):
                    diff = "extreme"
                    facile.image.set_alpha(150)
                    normal.image.set_alpha(150)
                    difficile.image.set_alpha(150)
                    extreme.image.set_alpha(255)
                if droiteMap.checkForInput(OPTIONS_MOUSE_POS):
                    indiceMap+=1
                    if indiceMap>=len(mapPropose):
                        indiceMap=0
                    Map.image=mapPropose[indiceMap].image
                    Map.listeType=mapPropose[indiceMap].listeType
                    Map.text = Map.font.render(mapPropose[indiceMap].nom, True, (0,0,0)) 
                    mapChoisie = mapPropose[indiceMap].listeType
                    
                    
                    pointSpawn = mapPropose[indiceMap].listePointSpawn
                if gaucheMap.checkForInput(OPTIONS_MOUSE_POS):
                    indiceMap-=1
                    if indiceMap<0:
                        indiceMap=len(mapPropose)-1
                    Map.image=mapPropose[indiceMap].image
                    Map.listeType=mapPropose[indiceMap].listeType
                    Map.text = Map.font.render(mapPropose[indiceMap].nom, True, (0,0,0)) 
                    mapChoisie = mapPropose[indiceMap].listeType
                    pointSpawn = mapPropose[indiceMap].listePointSpawn
            
            if droiteMap.checkForInput(OPTIONS_MOUSE_POS):
                droiteMap.image.set_alpha(100)
                gaucheMap.image.set_alpha(255)
            
            elif gaucheMap.checkForInput(OPTIONS_MOUSE_POS):
                droiteMap.image.set_alpha(255)
                gaucheMap.image.set_alpha(100)
            else:
                droiteMap.image.set_alpha(255)
                gaucheMap.image.set_alpha(255)
            if miniMap.checkForInput(OPTIONS_MOUSE_POS):
                miniMap.pressed2=True
                moyenneMap.pressed2=False
                grandeMap.pressed2=False
                ExtremeMap.pressed2=False
            elif moyenneMap.checkForInput(OPTIONS_MOUSE_POS):
                miniMap.pressed2=False
                moyenneMap.pressed2=True
                grandeMap.pressed2=False
                ExtremeMap.pressed2=False
            elif grandeMap.checkForInput(OPTIONS_MOUSE_POS):
                miniMap.pressed2=False
                moyenneMap.pressed2=False
                grandeMap.pressed2=True
                ExtremeMap.pressed2=False
            elif ExtremeMap.checkForInput(OPTIONS_MOUSE_POS):
                miniMap.pressed2=False
                moyenneMap.pressed2=False
                grandeMap.pressed2=False
                ExtremeMap.pressed2=True
            
            elif facile.checkForInput(OPTIONS_MOUSE_POS):
                facile.pressed2=True
                normal.pressed2=False
                difficile.pressed2=False
                extreme.pressed2=False
            elif normal.checkForInput(OPTIONS_MOUSE_POS):
                facile.pressed2=False
                normal.pressed2=True
                difficile.pressed2=False
                extreme.pressed2=False
            elif difficile.checkForInput(OPTIONS_MOUSE_POS):
                facile.pressed2=False
                normal.pressed2=False
                difficile.pressed2=True
                extreme.pressed2=False
            elif extreme.checkForInput(OPTIONS_MOUSE_POS):
                facile.pressed2=False
                normal.pressed2=False
                difficile.pressed2=False
                extreme.pressed2=True
            else :
                facile.pressed2=False
                normal.pressed2=False
                difficile.pressed2=False
                extreme.pressed2=False
                miniMap.pressed2=False
                moyenneMap.pressed2=False
                grandeMap.pressed2=False
                ExtremeMap.pressed2=False
        pygame.display.update()
    return back, diff, tailleMap, mapChoisie, pointSpawn


def options():
    choixMusique = int(aideCSV.valCorrespondante("musique"))
    global diagonalEcran, scaleButton, tailleEcran, taillePolice, scaleButtonMap, BG, SCREEN, scaleButtonBarre, scaleButtonR
    barre = pygame.transform.scale(pygame.image.load("data/menu/barre.png"), scaleButtonBarre)
    
    
    continu=True
    volume = aideCSV.valCorrespondante("volumeBruitage")
    volumeM = aideCSV.valCorrespondante("volumeMusique")
    print(volume, volumeM)
    if aideCSV.valCorrespondante("langue")=="fr":
        langue = "fr"
        OPTIONS_BACK = Button(image=pygame.transform.scale(pygame.image.load("data/menu/backButton.png").convert_alpha(), (scaleButton[0]//2, scaleButton[1]//2)), pos=(tailleEcran[0]*1/2, tailleEcran[1]*1/1.2), 
                        text_input="retour", font=get_font(taillePolice//2), base_color="white", hovering_color="#999999")
        if choixMusique==1:
        
            MUSIQUE1 = Button(image=pygame.transform.scale(pygame.image.load("data/menu/backButton.png").convert_alpha(), (scaleButton[0]//2, scaleButton[1]//2)), pos=(tailleEcran[0]*1/2, tailleEcran[1]*1/1.4), 
                            text_input="musique1", font=get_font(taillePolice//2), base_color="white", hovering_color="#999999")
        else:
            MUSIQUE1 = Button(image=pygame.transform.scale(pygame.image.load("data/menu/backButton.png").convert_alpha(), (scaleButton[0]//2, scaleButton[1]//2)), pos=(tailleEcran[0]*1/2, tailleEcran[1]*1/1.4), 
                            text_input="musique0", font=get_font(taillePolice//2), base_color="white", hovering_color="#999999")
        scrollBarMusic=ScrollBar((26, 0, 172), (tailleEcran[0]*0.35, tailleEcran[1]//2.2), round(float(volumeM)*100),(tailleEcran[0]*0.117, tailleEcran[1]*0.01),tailleEcran[0]*0.0058)
        scrollBarSound=ScrollBar((26, 0, 172), (tailleEcran[0]*0.53, tailleEcran[1]//2.2), round(float(volume)*100),(tailleEcran[0]*0.117, tailleEcran[1]*0.01),tailleEcran[0]*0.0058)
        
        bas = Button(image=pygame.transform.scale(pygame.image.load("data/menu/backButtonRond.png").convert_alpha(),(scaleButtonR[0]//6, scaleButtonR[1]//6)), pos=(tailleEcran[0]*3.93/10, tailleEcran[1]*0.26), 
                        text_input="bas", font=get_font(taillePolice//4), base_color="white", hovering_color="#999999")
        moyen = Button(image=pygame.transform.scale(pygame.image.load("data/menu/backButtonRond.png").convert_alpha(),(scaleButtonR[0]//5, scaleButtonR[1]//5)), pos=(tailleEcran[0]*3.93/10+tailleEcran[0]*1/10, tailleEcran[1]*0.26), 
                        text_input="moyen", font=get_font(taillePolice//4), base_color="white", hovering_color="#999999")
        haut = Button(image=pygame.transform.scale(pygame.image.load("data/menu/backButtonRond.png").convert_alpha(),(scaleButtonR[0]//4, scaleButtonR[1]//4)), pos=(tailleEcran[0]*3.93/10+tailleEcran[0]*2/10, tailleEcran[1]*0.26), 
                        text_input="haut", font=get_font(taillePolice//4), base_color="white", hovering_color="#999999")
    else:
        langue = "en"
        OPTIONS_BACK = Button(image=pygame.transform.scale(pygame.image.load("data/menu/backButton.png").convert_alpha(), (scaleButton[0]//2, scaleButton[1]//2)), pos=(tailleEcran[0]*1/2, tailleEcran[1]*1/1.2), 
                        text_input="back", font=get_font(taillePolice//2), base_color="white", hovering_color="#999999")
        scrollBarMusic=ScrollBar((26, 0, 172), (tailleEcran[0]*0.35, tailleEcran[1]//2.2), round(float(volumeM)*100),(tailleEcran[0]*0.117, tailleEcran[1]*0.01),tailleEcran[0]*0.0058)
        scrollBarSound=ScrollBar((26, 0, 172), (tailleEcran[0]*0.53, tailleEcran[1]//2.2), round(float(volume)*100),(tailleEcran[0]*0.117, tailleEcran[1]*0.01),tailleEcran[0]*0.0058)
        
        
        
        bas = Button(image=pygame.transform.scale(pygame.image.load("data/menu/backButtonRond.png").convert_alpha(),(scaleButtonR[0]//6, scaleButtonR[1]//6)), pos=(tailleEcran[0]*3.93/10, tailleEcran[1]*0.26), 
                        text_input="low", font=get_font(taillePolice//4), base_color="white", hovering_color="#999999")
        moyen = Button(image=pygame.transform.scale(pygame.image.load("data/menu/backButtonRond.png").convert_alpha(),(scaleButtonR[0]//5, scaleButtonR[1]//5)), pos=(tailleEcran[0]*3.93/10+tailleEcran[0]*1/10, tailleEcran[1]*0.26), 
                        text_input="medium", font=get_font(taillePolice//4), base_color="white", hovering_color="#999999")
        haut = Button(image=pygame.transform.scale(pygame.image.load("data/menu/backButtonRond.png").convert_alpha(),(scaleButtonR[0]//4, scaleButtonR[1]//4)), pos=(tailleEcran[0]*3.93/10+tailleEcran[0]*2/10, tailleEcran[1]*0.26), 
                        text_input="high", font=get_font(taillePolice//4), base_color="white", hovering_color="#999999")
    opti = int(aideCSV.valCorrespondante("optimisation"))
    if opti==0:
        moyen.image.set_alpha(150)
        haut.image.set_alpha(255)
        bas.image.set_alpha(150)
    elif opti==1:
        moyen.image.set_alpha(255)
        haut.image.set_alpha(150)
        bas.image.set_alpha(150)
    elif opti==2:
        moyen.image.set_alpha(150)
        haut.image.set_alpha(150)
        bas.image.set_alpha(255)
    clock = pygame.time.Clock()
    optiVerif=False
    while continu:
        clock.tick(60)
        if BG.get_alpha()>80:
            BG.set_alpha(BG.get_alpha()-transi)
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")
        SCREEN.blit(BG, (0,0))
        
        OPTIONS_TEXT = get_font(taillePolice).render(" OPTIONS ", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(tailleEcran[0]*1/2, tailleEcran[1]*1/10))

        if langue == "en":
            volume_TEXT = get_font(int(taillePolice*0.6)).render(" Sound ", True, "Black")
            music_TEXT = get_font(int(taillePolice*0.4)).render(" Music ", True, "Black")
            sound_TEXT = get_font(int(taillePolice*0.4)).render(" Sound ", True, "Black")
            graphisme_TEXT = get_font(int(taillePolice*0.4)).render(" Graphics ", True, "Black")
        else:
            volume_TEXT = get_font(int(taillePolice*0.6)).render(" Volume ", True, "Black")
            music_TEXT = get_font(int(taillePolice*0.4)).render(" Musique ", True, "Black")
            sound_TEXT = get_font(int(taillePolice*0.4)).render(" Bruitage ", True, "Black")
            graphisme_TEXT = get_font(int(taillePolice*0.4)).render(" Graphisme ", True, "Black")
        volume_RECT = OPTIONS_TEXT.get_rect(center=(tailleEcran[0]*0.54, tailleEcran[1]*0.36))
        music_RECT = OPTIONS_TEXT.get_rect(center=(tailleEcran[0]*0.46, tailleEcran[1]*0.45))
        sound_RECT = OPTIONS_TEXT.get_rect(center=(tailleEcran[0]*0.64, tailleEcran[1]*0.45))
        graphisme_RECT = OPTIONS_TEXT.get_rect(center=(tailleEcran[0]*0.54, tailleEcran[1]*0.23))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)
        SCREEN.blit(volume_TEXT, volume_RECT)
        SCREEN.blit(music_TEXT, music_RECT)
        SCREEN.blit(sound_TEXT, sound_RECT)
        SCREEN.blit(graphisme_TEXT, graphisme_RECT)

        
        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        MUSIQUE1.changeColor(OPTIONS_MOUSE_POS)
        bas.changeColor(OPTIONS_MOUSE_POS)
        moyen.changeColor(OPTIONS_MOUSE_POS)
        haut.changeColor(OPTIONS_MOUSE_POS)
        
        SCREEN.blit(barre, (tailleEcran[0]*0.345, tailleEcran[1]*0.25))
        
        OPTIONS_BACK.update(SCREEN)
        MUSIQUE1.update(SCREEN)
        bas.update(SCREEN)
        moyen.update(SCREEN)
        haut.update(SCREEN)

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    continu=False
                if MUSIQUE1.checkForInput(OPTIONS_MOUSE_POS):
                    choixMusique=1-choixMusique
                    aideCSV.remplacerVal("musique", choixMusique, True)
                    MUSIQUE1 = Button(image=pygame.transform.scale(pygame.image.load("data/menu/backButton.png").convert_alpha(), (scaleButton[0]//2, scaleButton[1]//2)), pos=(tailleEcran[0]*1/2, tailleEcran[1]*1/1.4), 
                            text_input="musique"+str(choixMusique), font=get_font(taillePolice//2), base_color="white", hovering_color="#999999")
                    
                volumeM = scrollBarMusic.getValue()/100
                volume = scrollBarSound.getValue()/100
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Vérifier si le clic de souris est sur le curseur
                    if scrollBarMusic.cursor_rect.collidepoint(event.pos):#gestion scroll barre
                        scrollBarMusic.dragging = True
                    if scrollBarSound.cursor_rect.collidepoint(event.pos):#gestion scroll barre
                        scrollBarSound.dragging = True
                    
                if bas.checkForInput(OPTIONS_MOUSE_POS):
                    aideCSV.remplacerVal("optimisation", 2)
                    moyen.image.set_alpha(150)
                    haut.image.set_alpha(150)
                    bas.image.set_alpha(255)
                    optiVerif=True
                if moyen.checkForInput(OPTIONS_MOUSE_POS):
                    aideCSV.remplacerVal("optimisation", 1)
                    bas.image.set_alpha(150)
                    haut.image.set_alpha(150)
                    moyen.image.set_alpha(255)
                    optiVerif=True
                if haut.checkForInput(OPTIONS_MOUSE_POS):
                    aideCSV.remplacerVal("optimisation", 0)
                    bas.image.set_alpha(150)
                    moyen.image.set_alpha(150)
                    haut.image.set_alpha(255)
                    optiVerif=True
            elif event.type == pygame.MOUSEBUTTONUP:
                scrollBarMusic.dragging = False
                scrollBarSound.dragging = False
            elif event.type == pygame.MOUSEMOTION:
                    # Déplacer le curseur si on est en train de le tirer
                    if scrollBarMusic.dragging:
                        scrollBarMusic.CURSOR_POS = event.pos[0] - scrollBarMusic.CURSOR_RADIUS, scrollBarMusic.CURSOR_POS[1]
                        # Limiter la position du curseur à la barre de défilement
                        if scrollBarMusic.CURSOR_POS[0] < scrollBarMusic.bar_pos[0]:
                            scrollBarMusic.CURSOR_POS = scrollBarMusic.bar_pos[0] - scrollBarMusic.CURSOR_RADIUS, scrollBarMusic.CURSOR_POS[1]
                        elif scrollBarMusic.CURSOR_POS[0] > scrollBarMusic.bar_pos[0] + scrollBarMusic.BAR_WIDTH - scrollBarMusic.CURSOR_RADIUS*2:
                            scrollBarMusic.CURSOR_POS = scrollBarMusic.bar_pos[0] + scrollBarMusic.BAR_WIDTH - scrollBarMusic.CURSOR_RADIUS*2, scrollBarMusic.CURSOR_POS[1]
                        # Calculer la valeur correspondante
                        scrollBarMusic.value = int((scrollBarMusic.CURSOR_POS[0] - scrollBarMusic.bar_pos[0]) / (scrollBarMusic.BAR_WIDTH - scrollBarMusic.CURSOR_RADIUS*2) * 100)
                    if scrollBarSound.dragging:
                        scrollBarSound.CURSOR_POS = event.pos[0] - scrollBarSound.CURSOR_RADIUS, scrollBarSound.CURSOR_POS[1]
                        # Limiter la position du curseur à la barre de défilement
                        if scrollBarSound.CURSOR_POS[0] < scrollBarSound.bar_pos[0]:
                            scrollBarSound.CURSOR_POS = scrollBarSound.bar_pos[0] - scrollBarSound.CURSOR_RADIUS, scrollBarSound.CURSOR_POS[1]
                        elif scrollBarSound.CURSOR_POS[0] > scrollBarSound.bar_pos[0] + scrollBarSound.BAR_WIDTH - scrollBarSound.CURSOR_RADIUS*2:
                            scrollBarSound.CURSOR_POS = scrollBarSound.bar_pos[0] + scrollBarSound.BAR_WIDTH - scrollBarSound.CURSOR_RADIUS*2, scrollBarSound.CURSOR_POS[1]
                        # Calculer la valeur correspondante
                        scrollBarSound.value = int((scrollBarSound.CURSOR_POS[0] - scrollBarSound.bar_pos[0]) / (scrollBarSound.BAR_WIDTH - scrollBarSound.CURSOR_RADIUS*2) * 100)
        # Dessiner la barre de défilement
        pygame.draw.rect(SCREEN, scrollBarMusic.GRAY, scrollBarMusic.bar_rect)
        pygame.draw.rect(SCREEN, scrollBarMusic.bar_color, (scrollBarMusic.bar_pos[0], scrollBarMusic.bar_pos[1], (scrollBarMusic.BAR_WIDTH-scrollBarMusic.CURSOR_RADIUS*2)*(scrollBarMusic.value/100), scrollBarMusic.BAR_HEIGHT))
        pygame.draw.rect(SCREEN, scrollBarSound.GRAY, scrollBarSound.bar_rect)
        pygame.draw.rect(SCREEN, scrollBarSound.bar_color, (scrollBarSound.bar_pos[0], scrollBarSound.bar_pos[1], (scrollBarSound.BAR_WIDTH-scrollBarSound.CURSOR_RADIUS*2)*(scrollBarSound.value/100), scrollBarSound.BAR_HEIGHT))

        # Dessiner le curseur
        scrollBarMusic.cursor_rect = pygame.draw.circle(SCREEN, scrollBarMusic.WHITE, scrollBarMusic.CURSOR_POS, scrollBarMusic.CURSOR_RADIUS)
        pygame.draw.circle(SCREEN, scrollBarMusic.WHITE, scrollBarMusic.CURSOR_POS, scrollBarMusic.CURSOR_RADIUS-2)
        scrollBarSound.cursor_rect = pygame.draw.circle(SCREEN, scrollBarSound.WHITE, scrollBarSound.CURSOR_POS, scrollBarSound.CURSOR_RADIUS)
        pygame.draw.circle(SCREEN, scrollBarSound.WHITE, scrollBarSound.CURSOR_POS, scrollBarSound.CURSOR_RADIUS-2)
          
        pygame.display.update()
    if optiVerif:
        majEcranOpti()
    return volume, volumeM, optiVerif

def main_menu():
    global diagonalEcran, scaleButton, tailleEcran, taillePolice, scaleButtonMap, BG, SCREEN, scaleButtonBarre, scaleButtonR
    pygame.init()

    majEcranOpti()
    
    #tailleEcran = tailleEcran[0]//2, tailleEcran[1]//2
    tailleEcran = avoirEcran()
    diagonalEcran = math.sqrt(tailleEcran[0]**2 + tailleEcran[1]**2)
    taillePolice = round(3/100*diagonalEcran)
    scaleButton = 1/3 * tailleEcran[0], 1/9*tailleEcran[1] #TAILLE DES BOUTONS
    scaleButtonMini = scaleButton[0]/6, scaleButton[1]/4
    scaleButtonBarre = 0.6/2 * tailleEcran[0], 0.6/30*tailleEcran[1]
    scaleButtonR = 0.6/3.5 * tailleEcran[0], 0.6/2*tailleEcran[1]
    scaleButtonMap = 1/3 * tailleEcran[0], 1/2*tailleEcran[1] #TAILLE DES BOUTONS
    scaleButtonSon = 1/3 * tailleEcran[0], 1/2*tailleEcran[1]
    flags = pygame.FULLSCREEN | pygame.DOUBLEBUF | pygame.SCALED | pygame.HWSURFACE
    SCREEN = pygame.display.set_mode(tailleEcran, flags)
    pygame.display.set_caption("Menu")
    pygame.display.set_caption("THE WILD LAND")
    pygame_icon = pygame.image.load('data/logo/icon_WL.png').convert_alpha()
    pygame.display.set_icon(pygame_icon)
    BG=pygame.image.load("data/menu/background.png").convert_alpha()
    BG = pygame.transform.scale(BG, (tailleEcran[0], tailleEcran[1]))

    
    
    pygame.mixer.music.load("data/son/musiques/menu.mp3")
    pygame.mixer.music.set_volume(float(aideCSV.valCorrespondante("volumeMusique")))
    pygame.mixer.music.play(loops=-1)
    continu=True
    
    if aideCSV.valCorrespondante("langue")=="fr":
        
        PLAY_BUTTON = Button(image=pygame.transform.scale(pygame.image.load("data/menu/backButton.png").convert_alpha(), (scaleButton)), pos=(tailleEcran[0]*1/5, tailleEcran[1]*1/5), 
                            text_input="JOUER", font=get_font(taillePolice), base_color="#fffffd", hovering_color="#999999")
        OPTIONS_BUTTON = Button(image=pygame.transform.scale(pygame.image.load("data/menu/backButton.png").convert_alpha(), (scaleButton)), pos=(tailleEcran[0]*1/5, tailleEcran[1]*1/3), 
                            text_input="OPTIONS", font=get_font(taillePolice), base_color="#fffffd", hovering_color="#999999")
        QUIT_BUTTON = Button(image=pygame.transform.scale(pygame.image.load("data/menu/backButton.png").convert_alpha(), (scaleButton)), pos=(tailleEcran[0]*1/5, tailleEcran[1]*6/7), 
                            text_input="QUITTER", font=get_font(taillePolice), base_color="#fffffd", hovering_color="#999999")
        EDITOR_BUTTON = Button(image=pygame.transform.scale(pygame.image.load("data/menu/backButton.png").convert_alpha(), (scaleButton)), pos=(tailleEcran[0]*1/5, tailleEcran[1]*1/2), 
                            text_input="EDITEUR", font=get_font(taillePolice), base_color="#fffffd", hovering_color="#999999")
        HELP_BUTTON = Button(image=pygame.transform.scale(pygame.image.load("data/menu/backButton mini.png").convert_alpha(), (scaleButtonMini)), pos=(tailleEcran[0]*0.03, tailleEcran[1]*0.98), 
                            text_input="Aide", font=get_font(20), base_color="#fffffd", hovering_color="#999999")
        LICENCE_BUTTON = Button(image=pygame.transform.scale(pygame.image.load("data/menu/backButton mini.png").convert_alpha(), (scaleButtonMini)), pos=(tailleEcran[0]*0.09, tailleEcran[1]*0.98), 
                            text_input="Licence", font=get_font(20), base_color="#fffffd", hovering_color="#999999")
    else:
        PLAY_BUTTON = Button(image=pygame.transform.scale(pygame.image.load("data/menu/backButton.png").convert_alpha(), (scaleButton)), pos=(tailleEcran[0]*1/5, tailleEcran[1]*1/5), 
                            text_input="PLAY", font=get_font(taillePolice), base_color="#fffffd", hovering_color="#999999")
        OPTIONS_BUTTON = Button(image=pygame.transform.scale(pygame.image.load("data/menu/backButton.png").convert_alpha(), (scaleButton)), pos=(tailleEcran[0]*1/5, tailleEcran[1]*1/3), 
                            text_input="OPTIONS", font=get_font(taillePolice), base_color="#fffffd", hovering_color="#999999")
        QUIT_BUTTON = Button(image=pygame.transform.scale(pygame.image.load("data/menu/backButton.png").convert_alpha(), (scaleButton)), pos=(tailleEcran[0]*1/5, tailleEcran[1]*6/7), 
                            text_input="QUIT", font=get_font(taillePolice), base_color="#fffffd", hovering_color="#999999")
        EDITOR_BUTTON = Button(image=pygame.transform.scale(pygame.image.load("data/menu/backButton.png").convert_alpha(), (scaleButton)), pos=(tailleEcran[0]*1/5, tailleEcran[1]*1/2), 
                            text_input="EDIT", font=get_font(taillePolice), base_color="#fffffd", hovering_color="#999999")
        HELP_BUTTON = Button(image=pygame.transform.scale(pygame.image.load("data/menu/backButton mini.png").convert_alpha(), (scaleButtonMini)), pos=(tailleEcran[0]*0.03, tailleEcran[1]*0.98), 
                            text_input="Help", font=get_font(20), base_color="#fffffd", hovering_color="#999999")
        LICENCE_BUTTON = Button(image=pygame.transform.scale(pygame.image.load("data/menu/backButton mini.png").convert_alpha(), (scaleButtonMini)), pos=(tailleEcran[0]*0.09, tailleEcran[1]*0.98), 
                            text_input="Licence", font=get_font(20), base_color="#fffffd", hovering_color="#999999")
    clock = pygame.time.Clock()
    transition=0
    while True:

        clock.tick(60)
        if BG.get_alpha()<255:
            
            BG.set_alpha(BG.get_alpha()+transi)
        SCREEN.fill("white")
        SCREEN.blit(BG, (0, 0))
        
        MENU_MOUSE_POS = pygame.mouse.get_pos()


        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON, EDITOR_BUTTON, HELP_BUTTON, LICENCE_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                continu=False
                sys.exit()
                
            if event.type == pygame.MOUSEBUTTONDOWN :
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):

                    pygame.mixer.Sound.play(PLAY_BUTTON.sonBoutonPress)
                    back, difficulte, tailleMap, mapChoisie, pointSpawn  = optionPartie()
                    aideCSV.remplacerVal("difficulte", difficulte, True)
                    aideCSV.remplacerVal("taille_matriceX", tailleMap, True)
                    aideCSV.remplacerVal("taille_matriceY", tailleMap, True)
                    if not back :
                        pygame.mixer.music.stop()
                        pygame_gestion.pygameInit(mapChoisie, pointSpawn)
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.mixer.Sound.play(PLAY_BUTTON.sonBoutonPress)
                    volume, volumeM, optiVerif = options()
                    print(volume, volumeM)
                    aideCSV.remplacerVal("volumeBruitage", volume, True)
                    aideCSV.remplacerVal("volumeMusique", volumeM, True)
                    if optiVerif:
                        tailleEcran = avoirEcran()
                        diagonalEcran = math.sqrt(tailleEcran[0]**2 + tailleEcran[1]**2)
                        taillePolice = round(3/100*diagonalEcran)
                        scaleButton = 1/3 * tailleEcran[0], 1/9*tailleEcran[1] #TAILLE DES BOUTONS
                        scaleButtonBarre = 0.6/2 * tailleEcran[0], 0.6/30*tailleEcran[1]
                        scaleButtonR = 0.6/3.5 * tailleEcran[0], 0.6/2*tailleEcran[1]
                        scaleButtonMap = 1/3 * tailleEcran[0], 1/2*tailleEcran[1] #TAILLE DES BOUTONS
                        scaleButtonSon = 1/3 * tailleEcran[0], 1/2*tailleEcran[1]
                        flags = pygame.FULLSCREEN | pygame.DOUBLEBUF | pygame.SCALED | pygame.HWSURFACE
                        SCREEN = pygame.display.set_mode(tailleEcran, flags)
                        if aideCSV.valCorrespondante("langue")=="fr" : 
                            pygame.display.set_caption("Menu")
                        else :
                            pygame.display.set_caption("Main Menu")
                        pygame.display.set_caption("THE WILD LAND")
                        pygame_icon = pygame.image.load('data/logo/icon_WL.png').convert_alpha()
                        pygame.display.set_icon(pygame_icon)
                        BG=pygame.image.load("data/menu/background.png").convert_alpha()
                        BG = pygame.transform.scale(BG, (tailleEcran[0], tailleEcran[1]))
                        PLAY_BUTTON = Button(image=pygame.transform.scale(pygame.image.load("data/menu/backButton.png").convert_alpha(), (scaleButton)), pos=(tailleEcran[0]*1/5, tailleEcran[1]*1/5), 
                        text_input="JOUER", font=get_font(taillePolice), base_color="#fffffd", hovering_color="#999999")
                        OPTIONS_BUTTON = Button(image=pygame.transform.scale(pygame.image.load("data/menu/backButton.png").convert_alpha(), (scaleButton)), pos=(tailleEcran[0]*1/5, tailleEcran[1]*1/3), 
                                            text_input="OPTIONS", font=get_font(taillePolice), base_color="#fffffd", hovering_color="#999999")
                        QUIT_BUTTON = Button(image=pygame.transform.scale(pygame.image.load("data/menu/backButton.png").convert_alpha(), (scaleButton)), pos=(tailleEcran[0]*1/5, tailleEcran[1]*6/7), 
                                            text_input="QUITTER", font=get_font(taillePolice), base_color="#fffffd", hovering_color="#999999")
                        EDITOR_BUTTON = Button(image=pygame.transform.scale(pygame.image.load("data/menu/backButton.png").convert_alpha(), (scaleButton)), pos=(tailleEcran[0]*1/5, tailleEcran[1]*1/2), 
                                            text_input="Editeur", font=get_font(taillePolice), base_color="#fffffd", hovering_color="#999999")
                        HELP_BUTTON = Button(image=pygame.transform.scale(pygame.image.load("data/menu/backButton mini.png").convert_alpha(), (scaleButtonMini)), pos=(tailleEcran[0]*0.03, tailleEcran[1]*0.98), 
                                            text_input="Aide", font=get_font(20), base_color="#fffffd", hovering_color="#999999")
                        LICENCE_BUTTON = Button(image=pygame.transform.scale(pygame.image.load("data/menu/backButton mini.png").convert_alpha(), (scaleButtonMini)), pos=(tailleEcran[0]*0.09, tailleEcran[1]*0.98), 
                            text_input="Licence", font=get_font(20), base_color="#fffffd", hovering_color="#999999")
                        
                if EDITOR_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.mixer.Sound.play(PLAY_BUTTON.sonBoutonPress)
                    mainEditor.editor()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.mixer.Sound.play(PLAY_BUTTON.sonBoutonPress)
                    pygame.quit()
                    sys.exit()
                    continu=False
                if HELP_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.mixer.Sound.play(PLAY_BUTTON.sonBoutonPress)
                    webbrowser.open('http://bit.ly/3Mzt2FP')

                if LICENCE_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.mixer.Sound.play(PLAY_BUTTON.sonBoutonPress)
                    webbrowser.open('https://melon-people-c90.notion.site/User-licence-4810d50a980c45698bdfdb99d6f40035')

        if continu:
            pygame.display.update()
    return 

def majEcranOpti():
    if not int(aideCSV.valCorrespondante("optimisation")):
        pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        aideCSV.remplacerVal("largeurEcran", pygame.display.Info().current_w)
        aideCSV.remplacerVal("hauteurEcran", pygame.display.Info().current_h)
    elif int(aideCSV.valCorrespondante("optimisation"))==1:
        aideCSV.remplacerVal("largeurEcran", 1920)
        aideCSV.remplacerVal("hauteurEcran", 1080)
    else :
        aideCSV.remplacerVal("largeurEcran", 1280)
        aideCSV.remplacerVal("hauteurEcran", 720)

    
def avoirEcran():
    return int(aideCSV.valCorrespondante("largeurEcran")), int(aideCSV.valCorrespondante("hauteurEcran"))