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
taillePolice = round(4/100*diagonalEcran)
scaleButton = 1/3 * tailleEcran[0], 1/9*tailleEcran[1] #TAILLE DES BOUTONS

SCREEN = pygame.display.set_mode(tailleEcran)
pygame.display.set_caption("Menu")
BG=pygame.image.load("data/menu/background.png")
BG = pygame.transform.scale(BG, (tailleEcran[0], tailleEcran[1]))

def get_font(size):
    return pygame.font.Font("assets/font.ttf", size)

def options():
    continu=True
    volume = 0.4
    volumeM = 0.5
    OPTIONS_BACK = Button(image=pygame.transform.scale(pygame.image.load("assets/backButton.png"), (scaleButton[0]//2, scaleButton[1]//2)), pos=(tailleEcran[0]*1/2, tailleEcran[1]*1/1.2), 
                    text_input="BACK", font=get_font(taillePolice//2), base_color="white", hovering_color="#999999")
    volumeHigh = Button(image=pygame.transform.scale(pygame.image.load("assets/backButton.png"), (scaleButton[0]//2, scaleButton[1]//2)), pos=(tailleEcran[0]*1/1.2, tailleEcran[1]*1/2), 
                    text_input="haut", font=get_font(taillePolice//2), base_color="white", hovering_color="#999999")
    volumeMedium = Button(image=pygame.transform.scale(pygame.image.load("assets/backButton.png"), (scaleButton[0]//2, scaleButton[1]//2)), pos=(tailleEcran[0]*1/2, tailleEcran[1]*1/2), 
                    text_input="moyen", font=get_font(taillePolice//2), base_color="white", hovering_color="#999999")
    volumeLow = Button(image=pygame.transform.scale(pygame.image.load("assets/backButton.png"), (scaleButton[0]//2, scaleButton[1]//2)), pos=(tailleEcran[0]*1/5, tailleEcran[1]*1/2), 
                    text_input="faible", font=get_font(taillePolice//2), base_color="white", hovering_color="#999999")
    volumeHighM = Button(image=pygame.transform.scale(pygame.image.load("assets/backButton.png"), (scaleButton[0]//2, scaleButton[1]//2)), pos=(tailleEcran[0]*1/1.2, tailleEcran[1]*1/2+tailleEcran[1]*1/10), 
                    text_input="haut", font=get_font(taillePolice//2), base_color="white", hovering_color="#999999")
    volumeMediumM = Button(image=pygame.transform.scale(pygame.image.load("assets/backButton.png"), (scaleButton[0]//2, scaleButton[1]//2)), pos=(tailleEcran[0]*1/2, tailleEcran[1]*1/2+tailleEcran[1]*1/10), 
                    text_input="moyen", font=get_font(taillePolice//2), base_color="white", hovering_color="#999999")
    volumeLowM = Button(image=pygame.transform.scale(pygame.image.load("assets/backButton.png"), (scaleButton[0]//2, scaleButton[1]//2)), pos=(tailleEcran[0]*1/5, tailleEcran[1]*1/2+tailleEcran[1]*1/10), 
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
    continu=True
    
    
    PLAY_BUTTON = Button(image=pygame.transform.scale(pygame.image.load("assets/backButton.png"), (scaleButton)), pos=(tailleEcran[0]*1/5, tailleEcran[1]*1/5), 
                        text_input="JOUER", font=get_font(taillePolice), base_color="#fffffd", hovering_color="#999999")
    OPTIONS_BUTTON = Button(image=pygame.transform.scale(pygame.image.load("assets/backButton.png"), (scaleButton)), pos=(tailleEcran[0]*1/5, tailleEcran[1]*1/3), 
                        text_input="OPTIONS", font=get_font(taillePolice), base_color="#fffffd", hovering_color="#999999")
    QUIT_BUTTON = Button(image=pygame.transform.scale(pygame.image.load("assets/backButton.png"), (scaleButton)), pos=(tailleEcran[0]*1/5, tailleEcran[1]*1/2), 
                        text_input="QUITTER", font=get_font(taillePolice), base_color="#fffffd", hovering_color="#999999")

    while continu:
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
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.mixer.Sound.play(PLAY_BUTTON.sonBoutonPress)
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
