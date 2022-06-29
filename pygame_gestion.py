from random import randint
from time import sleep
import pygame
from pygame.locals import *
from PIL import *  # pour les images
from PIL import Image
from inventaire import Inventaire
import main_menu
from generation import *
from mob import Mob
from selection import colisionItem, majSelection, majSelectionJoueur, selectionDispoItem
from tuile import Tuile
from joueur import Player
from game import Game
from item import Item

fenetrePygame = ""
infoObject = 0
joueur =""
global moveY, moveX
moveY=0
moveX=0



tailleEcran = [(3840, 2160), (2560, 1440), (1920, 1080),(1536,864),(1280, 720), (800, 600), (640, 480)]
# stocke la largeur et la hauteur de l'écran de l'utilisateur
# initialise la taille de l'écran (largeur, hauteur) en pixel
largeurEtHauteur = (0, 0)
modification = False
timeComtpeur=0
def pygameInit():  # foction servant à l'initialisation pygame
    
    global infoObject, modification, joueur,timeComtpeur
    print("lancement jeu")
    global largeurEtHauteur, fenetrePygame, moveX, moveY
    # if Options.music == True:
    # pygame.mixer.init()
    #music = pygame.mixer.music.load("data/Music/level0.mp3")
    # pygame.mixer.music.play(10)
    print("Génération de la map")
    imDebug = pygame.image.load("data/tuiles/debug.png")
    imDebug = pygame.transform.scale(imDebug, (4,4))
    BLACK = (0, 0, 0)
    continuer = True  # répeter à l'infini la fenetre pygame jusqu'a que continuer = false
    fenetrePygame = pygame.init()  # Initialisation de la bibliothèque Pygame

    clock = pygame.time.Clock()  # créer un système permettant de gérer le temps
        # Si touche appuyée plus de 400ms répétition de 30ms
    pygame.key.set_repeat(1, 30)


    
    
    infoObject= pygame.display.Info()  # récupère la taille de l'écran
    affichagePersonalise = affichage()
    
    # définit la taille de la fenetre pour qu'elle occupe tout l'écran --> sous Windows 10 et ultérieur elle passe même en plein écran mais pas sous Linux et MacOS
    fenetrePygame = pygame.display.set_mode(
        (tailleEcran[affichagePersonalise][0], tailleEcran[affichagePersonalise][1]), pygame.DOUBLEBUF)
    game = Game(infoObject)
    game.genererMatrice()
    
    
    # mise a l'echelle du perso les argument sont la surface qui est modifier et la taille
    # valeur de x qui place perso au milieu de l'ecran sur l'axe horizontale
    Imselection = pygame.image.load("data/tuiles/selection.png").convert_alpha()
    Imselection = pygame.transform.scale(Imselection, (150,150))
    buttonHome = pygame.image.load("data/menu/buttonHome.png").convert_alpha()
    buttonHome = pygame.transform.scale(buttonHome, (70, 70))
    tick_ressource=0
    move_ticker=0

    tuile=False

    joueur = Player(game,"joueur_1")
    inventaire=Inventaire(0,0, [])
    mob = Mob(game, "monstre")
    for i in range(-1, 2):
        for j in range(-1, 2):
            game.deleteFog(joueur.posX+i, joueur.posY+j)
    game.genererImg()
    itemForge = Item(game, "forge", 150)
    itemMoulin = Item(game, "moulin", 10)

    for deplacement in range(1675-infoObject.current_w):
        for i in range(len(game.map)):
            for j in range(len(game.map[0])):
                game.map[i][j].decalerX(-4)
        joueur.rect.x-=4 
        moveX-=4
    
    for deplacement in range(1070-infoObject.current_h):
        for i in range(len(game.map)):
            for j in range(len(game.map[0])):
                game.map[i][j].decalerY(-4)
        joueur.rect.y-=4
        moveY-=4
                            
    while continuer == True:
        # initialisation de la vitesse de raffraichissement (fps)
        modification=False
        cliqueItem = False
        modification, tuileTemp = KEY_move(game, joueur)
        for event in pygame.event.get():
            if event.type == QUIT:
                continuer = False
                
                
            

        
            if event.type == pygame.MOUSEBUTTONDOWN:  # si clic souris
                
                for item in inventaire.listeItem: 
                    if colisionItem(item, pygame.mouse.get_pos()) and tuile!=False:
                        if item.nom == "scierie":
                            joueur.construireScierie(tuile)    
                            joueur.changerImageScierie(tuile)
                            
                            modification=True
                            cliqueItem=True
                            

                if mouse[0] <= 75 and mouse[1] <= 75:  # detection si clic sur menu pricipal
                    continuer = False
                    main_menu.load =False
                    
                if not cliqueItem:
                    tuile = majSelection(game, pygame.mouse.get_pos())
                else :
                    tuile=False
                
                
        if continuer == True:  # récupère la position de la souris mais uniquement si la fenetre pygame est ouverte
            mouse = pygame.mouse.get_pos()
            deplacement_cam(mouse, game, joueur)
            
           
            #### Deplacement des mobs

            #if randint(0,10)==0:
            #    mob.randmove()
        
            if move_ticker>0:
                move_ticker-=1

            # efface l'image pour pouvoir actualiser le jeu
            fenetrePygame.fill(BLACK)

            #affichage de la map
            
            #Rafraîchissement de l'écran
            
            #affichage selection
            if tick_ressource==0:
                tick_ressource=180
                joueur.ajouterRessources()
            else:
                tick_ressource-=1

            if modification:
                game.genererImg()
                
                
            
            fenetrePygame.blit(game.mapImg, (moveX, moveY))
            fenetrePygame.blit(buttonHome, (10, 10))
            if tuile!=False:
                
                fenetrePygame.blit(Imselection, (tuile.getRectX(), tuile.getRectY()))    
            #affichage personnage
            
            
            
            fenetrePygame.blit(joueur.skin, (joueur.rect.x, joueur.rect.y))
            #fenetrePygame.blit(imDebug, joueur.getFeet())
            if game.map[mob.posY][mob.posX].isExplored:
                fenetrePygame.blit(mob.skin, (game.map[mob.posY][mob.posX].rect.x, game.map[mob.posY][mob.posX].rect.y-10))
            if joueur.bateau:
                fenetrePygame.blit(joueur.skinBateau, (joueur.rect.x, joueur.rect.y+70))
                
            if tuile!=False:
                liste = selectionDispoItem(game, tuile)
                inventaire = Inventaire(tuile.getRectX()-85, tuile.getRectY()-25, liste)
                inventaire.blitInventaire(fenetrePygame)

                
            
            for i in range(len(joueur.ressourcesIMG)):
                fenetrePygame.blit(joueur.ressourcesIMG[i], (infoObject.current_w-190-(190*i), 25))
                fenetrePygame.blit(joueur.RessourcesTEXT[i], (infoObject.current_w-120-(190*i), 3/100*infoObject.current_h))
                if joueur.RessourcesInfoModified[i] != False:
                    timeComtpeur +=1
                    if timeComtpeur <=60 :
                        fenetrePygame.blit(joueur.RessourcesInfoModified[i],(infoObject.current_w-95-(190*i),90))
                    else :
                        timeComtpeur = 0
                        joueur.resetRessourcesModified()


            pygame.display.flip()
        
        else:
            print("Fermeture du jeu & Lancement du menu principal")
            #main_menu.Main_Menu()
            pygame.display.quit()
            pygame.quit()  # ferme pygame et le jeu
            fenetrePygame=""
            return
        clock.tick(60)
            
            
def affichage():
        for i in range(len(tailleEcran)):
            if tailleEcran[i][0] == infoObject.current_w and tailleEcran[i][1] == infoObject.current_h:
                return i
        return 2
    
def KEY_move(game, joueur):
    modification=False
    tuile=False
    keys=pygame.key.get_pressed()
    
    if keys[K_RIGHT] :
        if joueur.deplacementAutorise("droite") and joueur.getWater() -10 >=0 :
            #joueur.goRight()
            #joueur.nombreDecalageRestantX=1
            joueur.rect.x+=joueur.velocity
            tuile = majSelectionJoueur(game, joueur.getFeet())
            joueur.posX, joueur.posY = tuile.posX, tuile.posY
            joueur.majBateau()
            for i in range(-1,2):
                for j in range(-1, 2):
                    if game.deleteFog(joueur.posX+i, joueur.posY+j): ##MODIFICATION
                        modification=True

                
                
    if keys[K_LEFT]:
            if joueur.deplacementAutorise("gauche") and joueur.getWater() -10 >=0:
                #joueur.goLeft()
                joueur.majBateau()
                joueur.rect.x-=joueur.velocity
                tuile = majSelectionJoueur(game, joueur.getFeet())
                joueur.posX, joueur.posY = tuile.posX, tuile.posY
                for i in range(-1,2):
                    for j in range(-1, 2):
                        if game.deleteFog(joueur.posX+i, joueur.posY+j): ##MODIFICATION
                            modification=True
    

    if keys[K_UP]:
            if joueur.deplacementAutorise("haut") and joueur.getWater() -10 >=0:
                #joueur.goUp()
                joueur.majBateau()
                joueur.rect.y-=joueur.velocity
                tuile = majSelectionJoueur(game, joueur.getFeet())
                joueur.posX, joueur.posY = tuile.posX, tuile.posY
                for i in range(-1,2):
                    for j in range(-1, 2):
                        if game.deleteFog(joueur.posX+i, joueur.posY+j): ##MODIFICATION
                            modification=True

    if keys[K_DOWN]:
            if joueur.deplacementAutorise("bas"):
                #joueur.goDown()
                joueur.rect.y+=joueur.velocity
                tuile = majSelectionJoueur(game, joueur.getFeet())
                joueur.posX, joueur.posY = tuile.posX, tuile.posY
                joueur.majBateau()
                for i in range(-1,2):
                    for j in range(-1, 2):
                        if game.deleteFog(joueur.posX+i, joueur.posY+j): ##MODIFICATION
                            modification=True
                
        
    if keys[K_b]:
        joueur.bateau=True
    if keys[K_v]:
        joueur.bateau = False
        
    return modification, tuile


def deplacement_cam(mouse, game, joueur): #gestion du déplacement de la caméra 
    deplacementCamBas(mouse, game, joueur)
    deplacementCamDroite(mouse, game, joueur)
    deplacementCamGauche(mouse, game, joueur)
    deplacementCamHaut(mouse, game, joueur)
    
    

    

    
        
        
    

def deplacementCamBas(mouse, game, joueur):
    global moveY, moveX
    x=infoObject.current_h-mouse[1]
    if x < 200 :  # Si souris en bas
        
        for i in range(len(game.map)):
            for j in range(len(game.map[0])):
                game.map[i][j].decalerY(f(x))
        joueur.rect.y+=f(x)
        moveY+=f(x)
    print(f(x))

        
def deplacementCamHaut(mouse, game, joueur):
    global moveY, moveX
    x = mouse[1]
    if x < 200 : #Si souris en haut
        for i in range(len(game.map)):
            for j in range(len(game.map[0])):
                game.map[i][j].decalerY(-f(x))
        joueur.rect.y+=-f(x)
        moveY+=-f(x)
        
def deplacementCamGauche(mouse, game, joueur):
    global moveY, moveX
    x= mouse[0]
    y = -f(x)
    if x < 200:  # Si souris à gauche
        for i in range(len(game.map)):
            for j in range(len(game.map[0])):
                game.map[i][j].decalerX(y)
        joueur.rect.x+=y
        moveX+=y
        
def deplacementCamDroite(mouse, game, joueur):
    global moveY, moveX
    x = infoObject.current_w-mouse[0]
    y=f(x)
    print("x=",x)
    if x < 200:  # Si souris à droite
        for i in range(len(game.map)):
            for j in range(len(game.map[0])):
                game.map[i][j].decalerX(y)
        joueur.rect.x+=y
        moveX+=y

def f(x):  #fonction vitesse deplacement cam
    y  = round(x*0.04-10)
    if y>20:
        return 15
    return y