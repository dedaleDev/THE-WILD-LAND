# gestion déplacement personnage et de pygame
import pygame
from pygame.locals import *
from PIL import *  # pour les images
import main_menu
fenetrePygame = ""

# stocke la largeur et la hauteur de l'écran de l'utilisateur
# initialise la taille de l'écran (largeur, hauteur) en pixel
largeurEtHauteur = (0, 0)


def pygameInit():  # foction servant à l'initialisation pygame
    global largeurEtHauteur, fenetrePygame
    # if Options.music == True:
    # pygame.mixer.init()
    #music = pygame.mixer.music.load("data/Music/level0.mp3")
    # pygame.mixer.music.play(10)
    BLACK = (0, 0, 0)
    continuer = True  # répeter à l'infini la fenetre pygame jusqu'a que continuer = false
    fenetrePygame = pygame.init()  # Initialisation de la bibliothèque Pygame
    pygame.HWSURFACE
    clock = pygame.time.Clock()  # créer un système permettant de gérer le temps
    # Si touche appuyée plus de 400ms répétition de 30ms
    pygame.key.set_repeat(400, 30)
    infoObject = pygame.display.Info()  # récupère la taille de l'écran
    # définit la taille de la fenetre pour qu'elle occupe tout l'écran --> sous Windows 10 et ultérieur elle passe même en plein écran mais pas sous Linux et MacOS
    fenetrePygame = pygame.display.set_mode(
        (infoObject.current_w, infoObject.current_h))
    # mise a l'echelle du perso les argument sont la surface qui est modifier et la taille
    # valeur de x qui place perso au milieu de l'ecran sur l'axe horizontale

    color_dark = (0, 0, 0)  # définit la couleur sombre du titre menu principal
    # définit la couleur claire du titre menu principal
    color_light = (255, 255, 255)
    smallfont = pygame.font.SysFont('Corbel', 50)  # definit la police utilisé
    text = smallfont.render('MENU PRINCIPAL', True,
                            color_dark)  # créer le texte en sombre
    while continuer == True:  # répete indefiniment le jeu
        # initialisation de la vitesse de raffraichissement (fps)
        clock.tick(30)

        for event in pygame.event.get():  # On parcours la liste de tous les événements reçus
            # Si un de ces événements est de type QUIT (Alt+F4) ou bouton fermeture alors on arrête la boucle
            if event.type == QUIT:
                continuer = False  # On arrête la boucle
            if event.type == KEYDOWN:  # Si touche appuyée
                print("")
            else:

                if event.key == K_RETURN:
                    enterIsOK = True
            if event.type == pygame.MOUSEBUTTONDOWN:  # si clic souris
                if mouse[0] <= 200 and mouse[1] <= 50:  # detection si clic sur menu pricipal
                    print("Main Menu loading")
                    main_menu.Main_Menu()
                    continuer = False
                    pygame.quit()  # ferme pygame et le jeu

        if continuer == True:  # récupère la position de la souris mais uniquement si la fenetre pygame est ouverte
            mouse = pygame.mouse.get_pos()

            # detection si clic sur menu pricipal, si la souris s'approche du texte menu principal, la couleur change. Noire->Blanc
            if mouse[0] <= 200 and mouse[1] <= 50:
                text = smallfont.render('MENU PRINCIPAL', True, color_light)
            else:
                text = smallfont.render('MENU PRINCIPAL', True, color_dark)

            # efface l'image pour pouvoir actualiser le jeu
            fenetrePygame.fill(BLACK)
            fenetrePygame.blit(text, (10, 10))
            pygame.display.flip()  # Rafraîchissement de l'écran
        else:
            print("Le jeu à été fermé via le menu principal")
    return
