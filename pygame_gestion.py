# gestion déplacement personnage et de pygame
import pygame
from pygame.locals import *
from PIL import *  # pour les images
from PIL import Image
import main_menu

from selection import majSelection
from tuile import Tuile
from joueur import Player
from game import Game
fenetrePygame = ""
infoObject = 0
tailleEcran = [(3840, 2160), (2560, 1440), (1920, 1080),(1536,864),(1280, 720), (800, 600), (640, 480)]
# stocke la largeur et la hauteur de l'écran de l'utilisateur
# initialise la taille de l'écran (largeur, hauteur) en pixel
largeurEtHauteur = (0, 0)


def pygameInit():  # foction servant à l'initialisation pygame
    global infoObject
    print("lancement jeu")
    global largeurEtHauteur, fenetrePygame
    # if Options.music == True:
    # pygame.mixer.init()
    #music = pygame.mixer.music.load("data/Music/level0.mp3")
    # pygame.mixer.music.play(10)
    print("Génération de la map")
    
    BLACK = (0, 0, 0)
    continuer = True  # répeter à l'infini la fenetre pygame jusqu'a que continuer = false
    fenetrePygame = pygame.init()  # Initialisation de la bibliothèque Pygame

    clock = pygame.time.Clock()  # créer un système permettant de gérer le temps
    # Si touche appuyée plus de 400ms répétition de 30ms
    pygame.key.set_repeat(400, 30)


    
    
    infoObject= pygame.display.Info()  # récupère la taille de l'écran
    affichagePersonalise = affichage()
    
    # définit la taille de la fenetre pour qu'elle occupe tout l'écran --> sous Windows 10 et ultérieur elle passe même en plein écran mais pas sous Linux et MacOS
    fenetrePygame = pygame.display.set_mode(
        (tailleEcran[affichagePersonalise][0], tailleEcran[affichagePersonalise][1]), pygame.DOUBLEBUF)
    game = Game(infoObject)
    
    
    # mise a l'echelle du perso les argument sont la surface qui est modifier et la taille
    # valeur de x qui place perso au milieu de l'ecran sur l'axe horizontale
    Imselection = pygame.image.load("data/tuiles/selection.png").convert_alpha()
    Imselection = pygame.transform.scale(Imselection, (150,135))
    color_dark = (0, 0, 200)  # définit la couleur sombre du titre menu principal
    # définit la couleur claire du titre menu principal
    color_light = (255, 255, 255)
    smallfont = pygame.font.SysFont('Corbel', 50)  # definit la police utilisé
    text = smallfont.render('MENU PRINCIPAL', True,
                            color_dark)  # créer le texte en sombre

    game.genererImg()
    moveY = 0
    moveX = 0
    tuile=False
    joueur = Player(game)
    
    
    
    while continuer == True:  # répete indefiniment le jeu
        
        # initialisation de la vitesse de raffraichissement (fps)
        clock.tick(30)
        for event in pygame.event.get():  # On parcours la liste de tous les événements reçus
            # Si un de ces événements est de type QUIT (Alt+F4) ou bouton fermeture alors on arrête la boucle
            if event.type == QUIT:
                continuer = False  # On arrête la boucle

            move_ticker = 0
            keys=pygame.key.get_pressed()
            if keys[K_RIGHT]:
                if move_ticker == 0:
                    move_ticker = 10
                    if joueur.deplacementAutorise("droite"):
                        joueur.goRight()
            if keys[K_LEFT]:
                if move_ticker == 0:
                    move_ticker = 10
                    if joueur.deplacementAutorise("gauche"):
                        joueur.goLeft()
            
            if keys[K_UP]:
                if move_ticker == 0:
                    move_ticker = 10
                    if joueur.deplacementAutorise("haut"):
                        joueur.goUp()   

            if keys[K_DOWN]:
                if move_ticker == 0:
                    move_ticker = 10
                    if joueur.deplacementAutorise("bas"):
                        joueur.goDown()   
            

          
            
            if event.type == pygame.MOUSEBUTTONDOWN:  # si clic souris
                if mouse[0] <= 200 and mouse[1] <= 50:  # detection si clic sur menu pricipal
                    continuer = False
                    main_menu.load =False
                tuile = majSelection(game)

            # detection si clic sur menu pricipal, si la souris s'approche du texte menu principal, la couleur change. Noire->Blanc
        if continuer == True:  # récupère la position de la souris mais uniquement si la fenetre pygame est ouverte
            mouse = pygame.mouse.get_pos()
            if mouse[0] <= 200 and mouse[1] <= 50:
                text = smallfont.render('MENU', True, color_light)
            else:
                text = smallfont.render('MENU', True, color_dark)

            #gestion du déplacement de la caméra :
            if mouse[1] <= 200 : #Si souris en haut
                for i in range(len(game.map)):
                    for j in range(len(game.map[0])):
                        game.map[i][j].decalerY(4)
                moveY+=4
                        

            if mouse[1] >= infoObject.current_h-200:  # Si souris en bas
                for i in range(len(game.map)):
                    for j in range(len(game.map[0])):
                        game.map[i][j].decalerY(-4)
                moveY-=4
                        

            if mouse[0] >= infoObject.current_w-200:  # Si souris à droite
                for i in range(len(game.map)):
                    for j in range(len(game.map[0])):
                        game.map[i][j].decalerX(-4)
                moveX-=4
            if mouse[0] <= 200:  # Si souris à gauche
                for i in range(len(game.map)):
                    for j in range(len(game.map[0])):
                        game.map[i][j].decalerX(4)
                moveX+=4



            
            if move_ticker>0:
                move_ticker-=1

            # efface l'image pour pouvoir actualiser le jeu
            fenetrePygame.fill(BLACK)

            #affichage de la map


            fenetrePygame.blit(game.mapImg, (moveX, moveY))
            print(game.fogIMG)
            fenetrePygame.blit(game.fogIMG, (moveX, moveY))
            fenetrePygame.blit(text, (10, 10))
              # Rafraîchissement de l'écran
            
            #affichage selection
            if tuile!=False:
                if tuile.type == 2 or tuile.type == 7:
                    fenetrePygame.blit(Imselection, (tuile.getRectX()+game.affichageTuile[game.affichagePersonalise][0]/100*game.infoObject.current_w, tuile.getRectY()+(game.getAffichageTuile()[game.affichagePersonalise][1]/100*game.infoObject.current_h)))
                else : 
                    fenetrePygame.blit(Imselection, (tuile.getRectX(), tuile.getRectY()))
                    
            #affichage personnage
            
            fenetrePygame.blit(joueur.skin, (game.map[joueur.posY][joueur.posX].rect.x, game.map[joueur.posY][joueur.posX].rect.y-10))
            
            pygame.display.flip()
        else:
            print("Fermeture du jeu & Lancement du menu principal")
            main_menu.Main_Menu()
            pygame.display.quit()
            pygame.quit()  # ferme pygame et le jeu
            fenetrePygame=""
            return
def affichage():
        for i in range(len(tailleEcran)):
            if tailleEcran[i][0] == infoObject.current_w and tailleEcran[i][1] == infoObject.current_h:
                return i
        return 2
    
