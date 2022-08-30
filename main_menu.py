import math
import pygame, sys
from button import Button
import pygame_gestion
import aideCSV


pygame.init()

#TEXTE ET BOUTONS RESPONSIVE

tailleEcran = pygame.display.Info().current_w, pygame.display.Info().current_h
#tailleEcran = tailleEcran[0]//2, tailleEcran[1]//2
diagonalEcran = math.sqrt(tailleEcran[0]**2 + tailleEcran[1]**2)
taillePolice = round(3/100*diagonalEcran)
scaleButton = 1/3 * tailleEcran[0], 1/9*tailleEcran[1] #TAILLE DES BOUTONS
scaleButtonMap = 1/3 * tailleEcran[0], 1/2*tailleEcran[1] #TAILLE DES BOUTONS
SCREEN = pygame.display.set_mode(tailleEcran)
pygame.display.set_caption("Menu")
pygame.display.set_caption("THE WILD LAND")
pygame_icon = pygame.image.load('data/logo/icon_WL.png')
pygame.display.set_icon(pygame_icon)
BG=pygame.image.load("data/menu/background.png").convert_alpha()
BG = pygame.transform.scale(BG, (tailleEcran[0], tailleEcran[1]))

def get_font(size):
    return pygame.font.Font("data/menu/font.ttf", size)


def optionPartie():
    continu = True
    back = False
    OPTIONS_BACK = Button(image=pygame.transform.scale(pygame.image.load("data/menu/backButton.png").convert_alpha(), (scaleButton[0]//2, scaleButton[1]//2)), pos=(tailleEcran[0]*1.5/10, tailleEcran[1]*1/1.1), 
                    text_input="retour", font=get_font(taillePolice//2), base_color="white", hovering_color="#999999")
    OPTIONS_GO = Button(image=pygame.transform.scale(pygame.image.load("data/menu/backButton.png").convert_alpha(), (scaleButton[0]//2, scaleButton[1]//2)), pos=(tailleEcran[0]*9/10, tailleEcran[1]*1/1.1), 
                    text_input="demarrer", font=get_font(taillePolice//2), base_color="white", hovering_color="#999999")
    
    OPTIONS_TEXT = get_font(taillePolice).render(" Nouvelle partie ", True, "Black")
    OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(tailleEcran[0]*1/4, tailleEcran[1]*1/10))
    
    
    MAP_TEXT = get_font(taillePolice//2).render(" Taille de la carte ", True, "Black")
    MAP_RECT = OPTIONS_TEXT.get_rect(center=(tailleEcran[0]*1/4, tailleEcran[1]*4.5/10))
    posYMap = 0.6
    posYDiff = 0.3
    
    tailleMap = 25
    
    miniMap = Button(image=pygame.transform.scale(pygame.image.load("data/menu/backButtonMap.png").convert_alpha(), (scaleButtonMap[0]//4-scaleButtonMap[0]//7, scaleButtonMap[1]//4-scaleButtonMap[1]//7)), pos=(tailleEcran[0]*1.25/10, tailleEcran[1]*posYMap), 
                    text_input="", font=get_font(taillePolice//2), base_color="white", hovering_color="#999999")
    
    moyenneMap = Button(image=pygame.transform.scale(pygame.image.load("data/menu/backButtonMap.png").convert_alpha(), (scaleButtonMap[0]//4-scaleButtonMap[0]//10, scaleButtonMap[1]//4-scaleButtonMap[1]//10)), pos=(tailleEcran[0]*1.25/10+tailleEcran[0]*0.5/10, tailleEcran[1]*posYMap-tailleEcran[1]*0.01), 
                    text_input="", font=get_font(taillePolice//2), base_color="white", hovering_color="#999999")
    
    grandeMap = Button(image=pygame.transform.scale(pygame.image.load("data/menu/backButtonMap.png").convert_alpha(), (scaleButtonMap[0]//4, scaleButtonMap[1]//4)), pos=(tailleEcran[0]*1.25/10+tailleEcran[0]*1.3/10, tailleEcran[1]*posYMap-tailleEcran[1]*0.035), 
                    text_input="", font=get_font(taillePolice//2), base_color="white", hovering_color="#999999")
                  
    ExtremeMap = Button(image=pygame.transform.scale(pygame.image.load("data/menu/backButtonMap.png").convert_alpha(), (scaleButtonMap[0]//4+scaleButtonMap[0]//10, scaleButtonMap[1]//4+scaleButtonMap[1]//10)), pos=(tailleEcran[0]*1.25/10+tailleEcran[0]*2.45/10, tailleEcran[1]*posYMap-tailleEcran[1]*0.06), 
                    text_input="", font=get_font(taillePolice//2), base_color="white", hovering_color="#999999")
    miniMap.image.set_alpha(50)
    moyenneMap.image.set_alpha(255)
    grandeMap.image.set_alpha(50)
    ExtremeMap.image.set_alpha(50)


    diff = "normal"

    facile = Button(image=pygame.transform.scale(pygame.image.load("data/menu/facile.png").convert_alpha(), (scaleButtonMap[0]//4, scaleButtonMap[1]//4)), pos=(tailleEcran[0]*1/7, tailleEcran[1]*posYDiff), 
                    text_input="", font=get_font(taillePolice//2), base_color="white", hovering_color="#999999")
    normal = Button(image=pygame.transform.scale(pygame.image.load("data/menu/normal.png").convert_alpha(), (scaleButtonMap[0]//4, scaleButtonMap[1]//4)), pos=(tailleEcran[0]*1/7+tailleEcran[0]*10//100, tailleEcran[1]*posYDiff), 
                    text_input="", font=get_font(taillePolice//2), base_color="white", hovering_color="#999999")
    difficile = Button(image=pygame.transform.scale(pygame.image.load("data/menu/difficile.png").convert_alpha(), (scaleButtonMap[0]//4, scaleButtonMap[1]//4)), pos=(tailleEcran[0]*1/7+tailleEcran[0]*20//100, tailleEcran[1]*posYDiff), 
                    text_input="", font=get_font(taillePolice//2), base_color="white", hovering_color="#999999")
    extreme = Button(image=pygame.transform.scale(pygame.image.load("data/menu/extreme.png").convert_alpha(), (scaleButtonMap[0]//4, scaleButtonMap[1]//4)), pos=(tailleEcran[0]*1/7+tailleEcran[0]*30//100, tailleEcran[1]*posYDiff), 
                text_input="", font=get_font(taillePolice//2), base_color="white", hovering_color="#999999")
    facile.image.set_alpha(255)
    normal.image.set_alpha(50)
    difficile.image.set_alpha(50)
    extreme.image.set_alpha(50)
    
    while continu:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")
        
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)
        SCREEN.blit(MAP_TEXT, MAP_RECT)
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
                    tailleMap = 10
                    miniMap.image.set_alpha(255)
                    moyenneMap.image.set_alpha(50)
                    grandeMap.image.set_alpha(50)
                    ExtremeMap.image.set_alpha(50)
                if moyenneMap.checkForInput(OPTIONS_MOUSE_POS):
                    tailleMap= 25
                    miniMap.image.set_alpha(50)
                    moyenneMap.image.set_alpha(255)
                    grandeMap.image.set_alpha(50)
                    ExtremeMap.image.set_alpha(50)
                if grandeMap.checkForInput(OPTIONS_MOUSE_POS):
                    tailleMap = 30
                    miniMap.image.set_alpha(50)
                    moyenneMap.image.set_alpha(50)
                    grandeMap.image.set_alpha(255)
                    ExtremeMap.image.set_alpha(50)
                if ExtremeMap.checkForInput(OPTIONS_MOUSE_POS):
                    tailleMap=40
                    miniMap.image.set_alpha(50)
                    moyenneMap.image.set_alpha(50)
                    grandeMap.image.set_alpha(50)
                    ExtremeMap.image.set_alpha(255)
                ##DIFFICULTE
                    
                if facile.checkForInput(OPTIONS_MOUSE_POS):
                    diff = "facile"
                    facile.image.set_alpha(255)
                    normal.image.set_alpha(50)
                    difficile.image.set_alpha(50)
                    extreme.image.set_alpha(50)
                    
                if normal.checkForInput(OPTIONS_MOUSE_POS):
                    diff = "normal"
                    facile.image.set_alpha(50)
                    normal.image.set_alpha(255)
                    difficile.image.set_alpha(50)
                    extreme.image.set_alpha(50)
                if difficile.checkForInput(OPTIONS_MOUSE_POS):
                    diff = "difficile"
                    facile.image.set_alpha(50)
                    normal.image.set_alpha(50)
                    difficile.image.set_alpha(255)
                    extreme.image.set_alpha(50)
                if extreme.checkForInput(OPTIONS_MOUSE_POS):
                    diff = "extreme"
                    facile.image.set_alpha(50)
                    normal.image.set_alpha(50)
                    difficile.image.set_alpha(50)
                    extreme.image.set_alpha(255)
        pygame.display.update()

    
    return back, diff, tailleMap


def options():
    continu=True
    volume = 0.4
    volumeM = 0.5
    OPTIONS_BACK = Button(image=pygame.transform.scale(pygame.image.load("data/menu/backButton.png").convert_alpha(), (scaleButton[0]//2, scaleButton[1]//2)), pos=(tailleEcran[0]*1/2, tailleEcran[1]*1/1.2), 
                    text_input="BACK", font=get_font(taillePolice//2), base_color="white", hovering_color="#999999")
    volumeHigh = Button(image=pygame.transform.scale(pygame.image.load("data/menu/backButton.png").convert_alpha(), (scaleButton[0]//2, scaleButton[1]//2)), pos=(tailleEcran[0]*1/1.2, tailleEcran[1]*1/2), 
                    text_input="haut", font=get_font(taillePolice//2), base_color="white", hovering_color="#999999")
    volumeMedium = Button(image=pygame.transform.scale(pygame.image.load("data/menu/backButton.png").convert_alpha(), (scaleButton[0]//2, scaleButton[1]//2)), pos=(tailleEcran[0]*1/2, tailleEcran[1]*1/2), 
                    text_input="moyen", font=get_font(taillePolice//2), base_color="white", hovering_color="#999999")
    volumeLow = Button(image=pygame.transform.scale(pygame.image.load("data/menu/backButton.png").convert_alpha(), (scaleButton[0]//2, scaleButton[1]//2)), pos=(tailleEcran[0]*1/5, tailleEcran[1]*1/2), 
                    text_input="faible", font=get_font(taillePolice//2), base_color="white", hovering_color="#999999")
    volumeHighM = Button(image=pygame.transform.scale(pygame.image.load("data/menu/backButton.png").convert_alpha(), (scaleButton[0]//2, scaleButton[1]//2)), pos=(tailleEcran[0]*1/1.2, tailleEcran[1]*1/2+tailleEcran[1]*1/10), 
                    text_input="haut", font=get_font(taillePolice//2), base_color="white", hovering_color="#999999")
    volumeMediumM = Button(image=pygame.transform.scale(pygame.image.load("data/menu/backButton.png").convert_alpha(), (scaleButton[0]//2, scaleButton[1]//2)), pos=(tailleEcran[0]*1/2, tailleEcran[1]*1/2+tailleEcran[1]*1/10), 
                    text_input="moyen", font=get_font(taillePolice//2), base_color="white", hovering_color="#999999")
    volumeLowM = Button(image=pygame.transform.scale(pygame.image.load("data/menu/backButton.png").convert_alpha(), (scaleButton[0]//2, scaleButton[1]//2)), pos=(tailleEcran[0]*1/5, tailleEcran[1]*1/2+tailleEcran[1]*1/10), 
                    text_input="faible", font=get_font(taillePolice//2), base_color="white", hovering_color="#999999")
    
    while continu:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        OPTIONS_TEXT = get_font(taillePolice).render(" OPTIONS ", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(tailleEcran[0]*1/2, tailleEcran[1]*1/10))
        volume_TEXT = get_font(taillePolice-5).render(" Volume ", True, "Black")
        volume_RECT = OPTIONS_TEXT.get_rect(center=(tailleEcran[0]*1/2, tailleEcran[1]*1/3))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)
        SCREEN.blit(volume_TEXT, volume_RECT)

        
        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        volumeHigh.changeColor(OPTIONS_MOUSE_POS)
        volumeMedium.changeColor(OPTIONS_MOUSE_POS)
        volumeLow.changeColor(OPTIONS_MOUSE_POS)
        volumeHighM.changeColor(OPTIONS_MOUSE_POS)
        volumeMediumM.changeColor(OPTIONS_MOUSE_POS)
        volumeLowM.changeColor(OPTIONS_MOUSE_POS)
        
        volumeHigh.update(SCREEN)
        volumeLow.update(SCREEN)
        volumeMedium.update(SCREEN)
        volumeHighM.update(SCREEN)
        volumeLowM.update(SCREEN)
        volumeMediumM.update(SCREEN)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    continu=False
                if volumeHigh.checkForInput(OPTIONS_MOUSE_POS):
                    volume = 1
                if volumeLow.checkForInput(OPTIONS_MOUSE_POS):
                    volume = 0.05
                if volumeMedium.checkForInput(OPTIONS_MOUSE_POS):
                    volume = 0.5
                    
                    
                if volumeHighM.checkForInput(OPTIONS_MOUSE_POS):
                    volumeM = 1
                if volumeLowM.checkForInput(OPTIONS_MOUSE_POS):
                    volumeM = 0.05
                if volumeMediumM.checkForInput(OPTIONS_MOUSE_POS):
                    volumeM = 0.5
        pygame.display.update()
    return volume, volumeM

def main_menu():
    pygame.mixer.music.load("data/son/musiques/menu.mp3")
    pygame.mixer.music.set_volume(float(aideCSV.valCorrespondante("volumeMusique")))
    pygame.mixer.music.play(loops=-1)
    continu=True
    
    
    PLAY_BUTTON = Button(image=pygame.transform.scale(pygame.image.load("data/menu/backButton.png").convert_alpha(), (scaleButton)), pos=(tailleEcran[0]*1/5, tailleEcran[1]*1/5), 
                        text_input="JOUER", font=get_font(taillePolice), base_color="#fffffd", hovering_color="#999999")
    OPTIONS_BUTTON = Button(image=pygame.transform.scale(pygame.image.load("data/menu/backButton.png").convert_alpha(), (scaleButton)), pos=(tailleEcran[0]*1/5, tailleEcran[1]*1/3), 
                        text_input="OPTIONS", font=get_font(taillePolice), base_color="#fffffd", hovering_color="#999999")
    QUIT_BUTTON = Button(image=pygame.transform.scale(pygame.image.load("data/menu/backButton.png").convert_alpha(), (scaleButton)), pos=(tailleEcran[0]*1/5, tailleEcran[1]*1/2), 
                        text_input="QUITTER", font=get_font(taillePolice), base_color="#fffffd", hovering_color="#999999")

    while True:
        SCREEN.blit(BG, (0, 0))
        
        MENU_MOUSE_POS = pygame.mouse.get_pos()


        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
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
                    back, difficulte, tailleMap  = optionPartie()
                    aideCSV.remplacerVal("difficulte", difficulte, True)
                    aideCSV.remplacerVal("taille_matriceX", tailleMap, True)
                    aideCSV.remplacerVal("taille_matriceY", tailleMap, True)
                    if not back :
                        pygame.mixer.music.stop()
                        pygame_gestion.pygameInit()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.mixer.Sound.play(PLAY_BUTTON.sonBoutonPress)
                    volume, volumeM = options()
                    aideCSV.remplacerVal("volumeBruitage", volume, True)
                    aideCSV.remplacerVal("volumeMusique", volumeM, True)
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.mixer.Sound.play(PLAY_BUTTON.sonBoutonPress)
                    pygame.quit()
                    sys.exit()
                    continu=False

        if continu:
            pygame.display.update()
    return 
