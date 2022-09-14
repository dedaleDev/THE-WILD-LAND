import math
from random import randint
import pygame
from pygame.locals import *
from inventaire import Inventaire
from generation import *
from loot import Loot
from mob import Mob
import main_menu
from selection import colisionItem, majSelection, majSelectionJoueur, majSelectionMob, selectionDispoItem
from game import Game
#from game import background_pil
from coffre import Coffre
from button import Button
from findPos import *
fenetrePygame = ""
infoObject = 0

global moveY, moveX, suiviePerso


def pygameInit(mapChoisie,pointSpawn):  # fonction servant à l'initialisation pygame
    
    global infoObject, modification, joueur,timeComtpeur, annimIncendie, delayIncendie,nombreAnnimationIncendie, annimTremblementListe
    global fenetrePygame, moveX, moveY, last, suiviePerso
    moveY=0
    moveX=0
    last = 0
    annimIncendieListe=[]
    annimTremblementListe=[]
    annimIncendie=0
    suiviePerso=140 #baisser la valeur pour un suivi plus rapide, 130 = suivi parfait
    nombreAnnimationIncendie=3
    nombreAnnimationTremblement=3

    # initialise la taille de l'écran (largeur, hauteur) en pixel
    modification = False
    delayIncendie=500
    timeComtpeur=0
    imDebug = pygame.image.load("data/tuiles/debug.png").convert_alpha()
    imDebug2 = pygame.transform.scale(imDebug, (20,20))
    imDebug = pygame.transform.scale(imDebug, (2,2))
    BLACK = (0, 0, 0)
    pygame.mixer.init()
    continuer = True  # répeter à l'infini la fenetre pygame jusqu'a que continuer = false
    fenetrePygame = pygame.init()  # Initialisation de la bibliothèque Pygame


    clock = pygame.time.Clock()
    pygame.key.set_repeat(1, 30)

    infoObject = pygame.display.Info()  # récupère la taille de l'écran
    fenetrePygame = pygame.display.set_mode((infoObject.current_w, infoObject.current_h))
    fenetrePygame.fill("black")
    im = pygame.image.load("data/menu/chargement.png")
    chargement = pygame.transform.scale(im, (infoObject.current_w, infoObject.current_h))
    fenetrePygame.blit(chargement, (0,0))
    pygame.display.flip()
    game = Game(infoObject, fenetrePygame, mapChoisie, pointSpawn)
    
    # mise a l'echelle du perso les argument sont la surface qui est modifie et la taille
    # valeur de x qui place perso au milieu de l'ecran sur l'axe horizontale
    Imselection = pygame.image.load("data/tuiles/selection.png").convert_alpha()
    buttonHome = pygame.image.load("data/menu/buttonHome.png").convert_alpha()
    buttonHome = pygame.transform.scale(buttonHome, (70, 70))
    bookicon = pygame.image.load("data/menu/book.png").convert_alpha()
    bookicon = pygame.transform.scale(bookicon,(50,50))
    pauseicon = pygame.image.load("data/menu/pause.png").convert_alpha()
    pauseicon = pygame.transform.scale(pauseicon,(45,45))

    
    infobulleIncendie = pygame.image.load("data/cata/infoBulle/info_incendie.png").convert_alpha()
    infoMortAnnimal = pygame.image.load("data/cata/infoBulle/infoMort.png").convert_alpha()

    infobulletremb = pygame.image.load("data/cata/infoBulle/info_tremblementDeTerre.png").convert_alpha()
    
    health = pygame.image.load("data/menu/health.png").convert_alpha()
    health = pygame.transform.scale(health, (50, 50))
    feuille = pygame.image.load("data/menu/feuille.png").convert_alpha()
    feuille = pygame.transform.scale(feuille, (50, 50))

    for i in range(1,10):
        im = pygame.image.load("data/cata/tremblement/tremblement"+str(i)+".png").convert_alpha()
        annimTremblementListe.append(pygame.transform.scale(im, (im.get_width()*1.5, im.get_height()*1.5)))
    for i in range(1,10):
        annimIncendieListe.append(pygame.image.load("data/cata/feu/flamme_"+str(i)+".png").convert_alpha())

    tick_ressource=0
    tirageCoffre = 0 #compte le nombre de tirage de coffre rate, 1 tirage toute les 10 secondes
    move_ticker=0
    tuile=False
    tickBatiment=1000

    inventaire=Inventaire(0,0, [])

    for i in range(-1, 2):
        for j in range(-1, 2):
            game.deleteFog(game.joueur.posX+i, game.joueur.posY+j)

    centrerJoueur(game)
    game.spawnAnnimal(5)
    
    #game.groupCoffre.add(Coffre(game, game.map[10][10], 100,100,100,100))
    #game.groupMob.add(Mob(game,"oiseau", 100, 2, tuile=game.map[4][4], score=150, aerien=True, annimal=True, attaque=0))
    #game.groupMob.add(Mob(game,"chameau", 100, 1, tuile=game.map[3][3], score=0, desertique=True, annimal=True, attaque=0))
    #game.groupMob.add(Mob(game,"oiseau", 100, 2, tuile=game.map[4][4], score=150, aerien=True, annimal=True, attaque=0))
    #game.groupMob.add(Mob(game,"oiseau", 100, 2, tuile=game.map[4][4], score=150, aerien=True, annimal=True, attaque=0))
    #game.groupMob.add(Mob(game,"oiseau", 100, 2, tuile=game.map[4][4], score=150, aerien=True, annimal=True, attaque=0))
    #game.groupMob.add(Mob(game,"oursin", 100, 1, tuile=game.map[4][4], score=150))
    game.groupMob.add(Mob(game,"golem_des_forets", 100, 2, tuile=game.map[4][4], score=150))
    #game.groupMob.add(Mob(game,"golem_des_forets", 100, 2, tuile=game.map[4][4], score=150))

    #game.groupMob.add(Mob(game,"oursin", 100, 2, tuile=game.map[4][4], score=150))
    #game.groupMob.add(Mob(game, "oursin", 150, 3, pique=True, tuile=game.map[1][2], score = 100))
    listefps=[]
    game.tempsMort+=pygame.time.get_ticks()
    fps = 0 #compte le nombre de fps
    tailleEcran = pygame.display.Info().current_w, pygame.display.Info().current_h
    diagonalEcran = math.sqrt(tailleEcran[0]**2 + tailleEcran[1]**2)
    taillePolice = round(3/100*diagonalEcran)
    police = get_font(taillePolice)
    while continuer == True:
        game.joueur.blit=False
        
        scoreText = police.render(str(game.joueur.score), True, "Black")
        scoreRect = scoreText.get_rect(center=(tailleEcran[0]*9.5/10, tailleEcran[1]*9.7/10))
        
        if fps>=60:
            fps =0
            listefps.append(clock.get_fps())
        else:
            fps+=1
        
        game.augmenterMob()
        game.son.jouerMusique2()
        
        modification=False
        cliqueItem = False

        modification = KEY_move(game, game.joueur, fenetrePygame)

        
        listeColide = game.checkCollision(game.joueur, game.groupMob)
        
        
        
        
        
        
        gestionMob(game, fps)
            
        
        keys=pygame.key.get_pressed()
        if keys[K_ESCAPE] and pygame.time.get_ticks() - game.lastPause > 250:
            tempsPasse = pause(fenetrePygame)
            game.lastPause = pygame.time.get_ticks()
            game.tempsMort+=tempsPasse
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == QUIT:
                continuer = False

            
            
            if event.type == pygame.MOUSEBUTTONDOWN:  # si clic souris
                
                for item in inventaire.listeItem: 
                    if colisionItem(item, pygame.mouse.get_pos()) and tuile: #on a une tuile de selectionné
                        batimentConstruit = game.joueur.construireBatiment(tuile, item)
                        modification=True
                        cliqueItem=True
                        if not batimentConstruit:
                            tickBatiment=0
                if not cliqueItem:
                    tuile = majSelection(game, pygame.mouse.get_pos(), game.joueur)
                else :
                    if tuile:
                        tuile.estSelect=False
                    tuile=False
        
       
        
        
        if continuer == True: 
            
            deplacement_cam(mouse, game, True)
            
           
            #### Deplacement des mobs
            
            
            
            
            
            
            for tour in game.groupDefense:
                tour.attack()
            for projo in game.groupProjectile:
                projo.moveProjectile()

            if move_ticker>0:
                move_ticker-=1
            
            fenetrePygame.fill(BLACK)
            
            ####CATASTROPHE
            
                
            modification=True
            #affichage selection
            if tick_ressource==0:
                tick_ressource=600
                game.joueur.ajouterRessources()
                
                chanceCoffre = random.randint(0,100)
                if chanceCoffre < tirageCoffre :
                    game.joueur.genererCoffre()
                    tirageCoffre=0
                else :
                    tirageCoffre+=7
                if game.groupMob.__len__()-game.nbAnnimaux<9:
                    game.spawMob()
                    
                
                tuileCata = game.majCata()
                if game.incendie and tuileCata:
                    annimIncendieListe.append(tuileCata)
                    annimTremblementListe.append(tuileCata)
                    choixIncendie = random.randint(0,1)
                    if choixIncendie:
                        pygame.mixer.Sound.play(game.son.incendie, maxtime=4000)
                    else:
                        #pygame.mixer.Sound.play(game.son.tremblement)
                        pass
            else:
                tick_ressource-=1
            
            if modification:
                pass
                #game.genererImg()
            alerteVille=False #une ville est presente sur la map
            game.moveX, game.moveY = moveX, moveY
            listeMontagne=[]
            for y in range(game.taille_matriceY):
                for x in range(game.taille_matriceX):
                    if game.map[y][x].isExplored:
                        if (moveX+game.map[y][x].Xoriginal < infoObject.current_w and moveY+game.map[y][x].Yoriginal<infoObject.current_h) or True: #si la tuile est dans l'ecran
                            if game.map[y][x].type==2 or game.map[y][x].type==7:
                                listeMontagne.append(game.map[y][x])
                            else:
                                fenetrePygame.blit(game.map[y][x].image, (moveX+game.map[y][x].Xoriginal, moveY+game.map[y][x].Yoriginal))
                        if game.map[y][x].annimation:
                            game.map[y][x].changeAnnim()
                    if game.map[y][x].traceMob:
                        fenetrePygame.blit(Imselection, (game.map[y][x].getRectX(), game.map[y][x].getRectY()))
                    if game.map[y][x].annimationFog>0 and game.map[y][x].isExplored:
                        
                        fenetrePygame.blit(game.map[y][x].imageFog, (moveX+game.map[y][x].Xoriginal, moveY+game.map[y][x].Yoriginal))
                        game.map[y][x].annimationFog-=8
                        game.map[y][x].imageFog.set_alpha(game.map[y][x].annimationFog)
                        
                    elif not game.map[y][x].isExplored:
                        fenetrePygame.blit(game.map[y][x].imageFog, (moveX+game.map[y][x].Xoriginal, moveY+game.map[y][x].Yoriginal))
                        
                    if game.map[y][x].ville:
                        alerteVille = True
                        tuileVille = game.map[y][x]
                        
            
            
            
            for coffre in game.groupCoffre:
                if coffre.tuile.posX == game.joueur.posX and coffre.tuile.posY == game.joueur.posY:
                    if coffre.clock==coffre.clockMax:
                        coffre.indice+=1
                        coffre.clock=0
                        if coffre.indice==len(game.images.coffre)-1:
                            game.joueur.setRessource(coffre.wood, coffre.stone, coffre.food, coffre.water)
                            pygame.mixer.Sound.play(game.son.coffreOuverture)
                            game.groupLoot.add(Loot(coffre.wood, coffre.stone, coffre.water, coffre.food, coffre.rect.x+20, coffre.rect.y-30, game))
                            
                            coffre.kill()
                    else:
                        coffre.clock+=1

                else:
                    coffre.indice=0

                if coffre.tuile.isExplored :
                    fenetrePygame.blit(coffre.image[coffre.indice], (coffre.rect.x+moveX, coffre.rect.y+moveY))
                    fenetrePygame.blit(coffre.imEtoile, (coffre.etoileRect.x+moveX, coffre.etoileRect.y+moveY))  
                    fenetrePygame.blit(coffre.imEtoile2, (coffre.etoileRect2.x+moveX, coffre.etoileRect2.y+moveY))  
                    fenetrePygame.blit(coffre.imEtoile3, (coffre.etoileRect3.x+moveX, coffre.etoileRect3.y+moveY))  
                    if fps%3==0:
                        coffre.etoileAnnim()



            

            if tuile :
                if not (abs(tuile.posX-game.joueur.posX)<2 and abs(tuile.posY-game.joueur.posY)<2):
                    tuile.estSelect=False
                    tuile=False
            
            #affichage personnage
            
            
            listeOrdre = []
            #debut = time.time()
            for mob in game.groupMob:
                if game.map[mob.posY][mob.posX].isExplored :
                    #fenetrePygame.blit(mob.skin, (mob.rect.x, mob.rect.y))
                    listeOrdre.append((mob.skin, mob.rect.x, mob.rect.y, mob.rect.center[1]))
                    pass
                
            


            for mob in game.groupMob:
                if game.map[mob.posY][mob.posX].isExplored:
                    if not mob.annimal:
                        mob.update_health_bar()

            ####PASSAGE DES MONTAGNES
            if tuile :
                fenetrePygame.blit(Imselection, (tuile.getRectX(), tuile.getRectY()))
                if tuile.tour:      
                    #pygame.draw.circle(fenetrePygame, (155,155,155), (tuile.tour.rect.x+30, tuile.tour.rect.y), tuile.tour.range, width=3, )
                    pass
            decalageYcentre = -100
            for tuile2 in listeMontagne:
                if tuile2.type==2 :
                    center = tuile2.centerOriginal
                    if tuile2.mortier:
                        listeOrdre.append((tuile2.image, moveX+tuile2.Xoriginal, moveY+tuile2.Yoriginal-85, center[1]+moveY-92-decalageYcentre))
                    #fenetrePygame.blit(tuile2.image, (moveX+tuile2.Xoriginal, moveY+tuile2.Yoriginal-112))
                    else:
                        
                        listeOrdre.append((tuile2.image, moveX+tuile2.Xoriginal, moveY+tuile2.Yoriginal-112, moveY+center[1]-112-decalageYcentre))
                else :
                    center = tuile2.centerOriginal
                    
                    #fenetrePygame.blit(tuile2.image, (moveX+tuile2.Xoriginal, moveY+tuile2.Yoriginal-80))
                    
                    listeOrdre.append((tuile2.image, moveX+tuile2.Xoriginal, moveY+tuile2.Yoriginal-92, center[1]+moveY-92-decalageYcentre))
            
            if not game.joueur.bateau:
                fenetrePygame.blit(game.joueur.skin, (game.joueur.rect.x, game.joueur.rect.y))
                center = game.joueur.rect.center
                listeOrdre.append((game.joueur.skin, game.joueur.rect.x, game.joueur.rect.y, center[1]))

            elif game.joueur.bateau:
                #fenetrePygame.blit(game.joueur.skinBateau, (game.joueur.rect.x-15, game.joueur.rect.y+30))
                center = game.joueur.rect.center
                
                listeOrdre.append((game.joueur.skinBateau, game.joueur.rect.x-15, game.joueur.rect.y+30, center[1]+30))
            listeOrdre.sort(key=lambda x: x[3])
            for image, posX, posY, center in listeOrdre:
                fenetrePygame.blit(image, (posX, posY))
            for loot in game.groupLoot:
                loot.update(fenetrePygame, moveX,moveY)
            
            
            if tuile :
                liste = selectionDispoItem(game, tuile, game.joueur)
                inventaire = Inventaire(tuile.getRectX()-50, tuile.getRectY()-25, liste)
                inventaire.blitInventaire(fenetrePygame, game.joueur)
                for item in inventaire.listeItem:
                        if colisionItem(item, pygame.mouse.get_pos()):##INFO BULLE##
                            inventaire.blitInfoBulle(fenetrePygame, item)
            for projectile in game.groupProjectile:              
                fenetrePygame.blit(projectile.img, (projectile.rect.x, projectile.rect.y))


            for collision in listeColide:
                fenetrePygame.blit(game.imCollision,(random.randint(game.joueur.rect.x-20, game.joueur.rect.x+20), random.randint(game.joueur.rect.y, game.joueur.rect.y+120)))
                
            if alerteVille:
                fenetrePygame.blit(game.images.ville, (tuileVille.rect.x+30, tuileVille.rect.y-260))
            
            if (annimIncendie or  game.incendie) and type(annimIncendieListe[-1])==Tuile :
                if choixIncendie:
                    entreImage=100
                    fenetrePygame.blit(annimIncendieListe[annimIncendie], (annimIncendieListe[-1].rect.x+50, annimIncendieListe[-1].rect.y-annimIncendieListe[annimIncendie].get_height()+100))
                    fenetrePygame.blit(infobulleIncendie, (tailleEcran[0]- 400, tailleEcran[1] - 700))
                else:
                    entreImage=100
                    fenetrePygame.blit(annimTremblementListe[annimIncendie], (annimTremblementListe[-1].rect.x+50, annimTremblementListe[-1].rect.y-annimTremblementListe[annimIncendie].get_height()+100))
                    fenetrePygame.blit(infobulletremb, (tailleEcran[0]- 400, tailleEcran[1] - 700))
                game.incendie=False
                if game.tempsJeu()-delayIncendie>entreImage:
                    annimIncendie+=1
                    delayIncendie=game.tempsJeu()
                    if annimIncendie==9 :
                        if nombreAnnimationIncendie>0:
                            annimIncendie=1
                            nombreAnnimationIncendie-=1
                        elif nombreAnnimationTremblement>0:
                            annimIncendie=1
                            nombreAnnimationTremblement-=1
                        else:
                            game.joueur.detruireBatimentRessource(annimIncendieListe[-1])
                            annimIncendieListe.pop(len(annimIncendieListe)-1)
                            annimTremblementListe.pop(len(annimTremblementListe)-1)
                            nombreAnnimationIncendie=3
                            
                            annimIncendie=0
            
            for i in range(len(game.joueur.ressourcesIMG)):
                fenetrePygame.blit(game.joueur.ressourcesIMG[i], (infoObject.current_w-190-(190*i), 25))
                fenetrePygame.blit(game.joueur.RessourcesTEXT[i], (infoObject.current_w-120-(190*i), 3/100*infoObject.current_h))
                if game.joueur.RessourcesInfoModified[i] != False:
                    timeComtpeur +=1
                    if timeComtpeur <=60 :
                        fenetrePygame.blit(game.joueur.RessourcesInfoModified[i],(infoObject.current_w-95-(190*i),90))
                    else :
                        timeComtpeur = 0
                        game.joueur.resetRessourcesModified()
            game.joueur.update_health_bar()
            
            if game.joueur.imageArmure:
                fenetrePygame.blit(game.joueur.imageArmure, (22,80))
            for mob in game.groupMob:
                fenetrePygame.blit(imDebug, mob.getFeet())
            game.joueur.update_ecolo_bar()
            fenetrePygame.blit(health, (20,15))
            fenetrePygame.blit(feuille, (10,368))
            fenetrePygame.blit(scoreText, scoreRect)
            if tickBatiment<60:
                fenetrePygame.blit(game.imageErreurRessource, (infoObject.current_w-game.imageErreurRessource.get_width()-(infoObject.current_w-game.imageErreurRessource.get_width())/2,infoObject.current_h - 200))
                tickBatiment+=1
            if game.infoMortAnnimal>0:
                print("mort")
                fenetrePygame.blit(infoMortAnnimal, (tailleEcran[0]- 400, tailleEcran[1] - 700))
                game.infoMortAnnimal-=1
            
            for pos in game.listeDebug:
                fenetrePygame.blit(imDebug2, pos)

            if game.joueur.estMort:
                mort(game)
            if game.joueur.ville:
                victoire(game)
            
            pygame.display.flip()
            
        else:
            print("Fermeture du jeu")
            moyenneFps=0
            if listefps:
                for elem in listefps :
                    
                    moyenneFps += elem
                moyenneFps = moyenneFps/len(listefps)
                print("moyenne des fps sur la session acutelle :", moyenneFps )
                listefps.sort()
                print("fps min 1% et max 1% :", listefps[1//100*len(listefps)], listefps[99//100*len(listefps)-1] )
                print("mesure sur "+str(len(listefps))+" fps")
            main_menu.main_menu()
            pygame.display.quit()
            pygame.quit()  # ferme pygame et le jeu
            fenetrePygame=""
            return
        
        clock.tick(60)


def KEY_move(game,joueur,fenetre):
    modification=False
    tuile=False
    haut=True
    bas=True

    keys=pygame.key.get_pressed()
    #gestion diagonale
    if (keys[K_d] or keys[K_RIGHT]) and (keys[K_z] or keys[K_UP]): #diag haut droite
        haut=False
    elif (keys[K_d] or keys[K_RIGHT]) and (keys[K_s]or keys[K_DOWN]): #diag bas droite
        bas=False
    elif (keys[K_q]or keys[K_LEFT]) and (keys[K_s]or keys[K_DOWN]): #diag bas gauche
        bas=False
    elif (keys[K_q]or keys[K_LEFT]) and (keys[K_z] or keys[K_UP]): #diag haut gauche
        haut=False
    
    
    bug=False
    if keys[K_d] or keys[K_RIGHT]:
        if bug:=joueur.deplacementAutorise("droite") :
            
            deplacementCamDroite((infoObject.current_w - suiviePerso,0), game, True)
            joueur.goRight()
            tuile = majSelectionJoueur(game)
            if tuile!=None:
                    joueur.setPos(tuile)
            #joueur.majBateau()
            
            for i in range(-1,2):
                for j in range(-1, 2):
                    if game.deleteFog(joueur.posX+i, joueur.posY+j): ##MODIFICATION
                        modification=True
            
                
                
    if keys[K_q]or keys[K_LEFT]:
            if bug:=joueur.deplacementAutorise("gauche"):
                #joueur.majBateau()
                deplacementCamGauche((suiviePerso, 0), game, True)
                joueur.goLeft()
                tuile = majSelectionJoueur(game)
                if tuile!=None:
                    joueur.setPos(tuile)
                for i in range(-1,2):
                    for j in range(-1, 2):
                        if game.deleteFog(joueur.posX+i, joueur.posY+j): ##MODIFICATION
                            modification=True
    

    if keys[K_z] or keys[K_UP]:
            if bug:=joueur.deplacementAutorise("haut"):
                #joueur.majBateau()
                deplacementCamHaut((0,suiviePerso), game, True)
                joueur.goUp(haut)
                tuile = majSelectionJoueur(game)
                if tuile!=None:
                    joueur.setPos(tuile)
                for i in range(-1,2):
                    for j in range(-1, 2):
                        if game.deleteFog(joueur.posX+i, joueur.posY+j): ##MODIFICATION
                            modification=True

    if keys[K_s]or keys[K_DOWN]:
            if bug:=joueur.deplacementAutorise("bas"):
                deplacementCamBas((0, infoObject.current_h-suiviePerso), game, True)
                joueur.goDown(bas)
                tuile = majSelectionJoueur(game)
                if tuile!=None:
                    joueur.setPos(tuile)
                #joueur.majBateau()
                for i in range(-1,2):
                    for j in range(-1, 2):
                        if game.deleteFog(joueur.posX+i, joueur.posY+j): ##MODIFICATION
                            modification=True
                
        
    if keys[K_b]:
        if game.map[joueur.posY][joueur.posX].port:
            joueur.bateau=True
    if keys[K_v]:
        if game.map[joueur.posY][joueur.posX].port:
            joueur.bateau = False
    if bug==None:
        print("bug")
        tuile = majSelectionJoueur(game)
        if tuile!=None:
            print(tuile.posY, tuile.posX, "bug resolu")
            joueur.setPos(tuile)
    return modification, tuile


def deplacement_cam(mouse, game, bloquage=False): #gestion du déplacement de la caméra 
    deplacementCamBas(mouse, game, bloquage)
    deplacementCamDroite(mouse, game, bloquage)
    deplacementCamGauche(mouse, game, bloquage)
    deplacementCamHaut(mouse, game, bloquage)
    
def centrerJoueur(game):
    while game.joueur.rect.x < infoObject.current_w//2-10:
        deplacementCamGauche((199,0), game, False)

    while game.joueur.rect.x > infoObject.current_w//2+10:
        deplacementCamDroite((infoObject.current_w-199,0), game, False)


    while game.joueur.rect.y > infoObject.current_h//2-10:
        deplacementCamBas((0,infoObject.current_h-199), game, False)

    while game.joueur.rect.y < infoObject.current_h//2+10:
        deplacementCamHaut((0,199), game, False)



def deplacementCamBas(mouse, game, bloquage):
    global moveY, moveX
    x=infoObject.current_h-mouse[1]
    y=f(x)
    if x < 200 :  # Si souris en bas
        if not bloquage or (game.map[-1][0].Yoriginal+moveY>infoObject.current_h-250):
            for i in range(len(game.map)):
                for j in range(len(game.map[0])):
                    game.map[i][j].decalerY(y)
            game.joueur.rect.y+=y
            moveY+=y
            for mob in game.groupMob:
                mob.rect.y+=y
            for projo in game.groupProjectile:
                projo.rect.y+=y
            for defense in game.groupDefense:
                defense.rect.y+=y
            
def deplacementCamHaut(mouse, game, bloquage):
    global moveY, moveX
    x = mouse[1]
    y = -f(x)
    if x < 200 : #Si souris en haut
        if not bloquage or (game.map[0][-1].rect.y+moveY<100):
            for i in range(len(game.map)):
                for j in range(len(game.map[0])):
                    game.map[i][j].decalerY(y)
            game.joueur.rect.y+=y
            moveY+=y
            for mob in game.groupMob:
                mob.rect.y+=y
            for projo in game.groupProjectile:
                projo.rect.y+=y
            for defense in game.groupDefense:
                defense.rect.y+=y
        
def deplacementCamGauche(mouse, game, bloquage):
    global moveY, moveX
    x= mouse[0]
    y = -f(x)
    if x < 200:  # Si souris à gauche
        if not bloquage or (game.map[0][0].rect.x+moveX<100):
            for i in range(len(game.map)):
                for j in range(len(game.map[0])):
                    game.map[i][j].decalerX(y)
            game.joueur.rect.x+=y
            for mob in game.groupMob:
                mob.rect.x+=y
            moveX+=y
            for projo in game.groupProjectile:
                projo.rect.x+=y
            for defense in game.groupDefense:
                defense.rect.x+=y
        
def deplacementCamDroite(mouse, game, bloquage):
    global moveY, moveX
    x = infoObject.current_w-mouse[0]
    y=f(x)


    if x < 200:  # Si souris à droite
        if not bloquage or (game.map[-1][-1].Xoriginal+moveX>infoObject.current_w-400):
            for i in range(len(game.map)):
                for j in range(len(game.map[0])):
                    game.map[i][j].decalerX(y)
            game.joueur.rect.x+=y
            moveX+=y
            for mob in game.groupMob:
                mob.rect.x+=y
            for projo in game.groupProjectile:
                projo.rect.x+=y
            for defense in game.groupDefense:
                defense.rect.x+=y

def f(x):  #fonction vitesse deplacement cam
    y  = round(x*0.04-10)
    if y>20:
        return 15
    return y

def pause(fenetre):
    global infoObject
    tailleEcran = infoObject.current_w, infoObject.current_h 
    diagonalEcran = math.sqrt(tailleEcran[0]**2 + tailleEcran[1]**2)
    pause=True
    scaleButton = 1/3 * tailleEcran[0], 1/9*tailleEcran[1]
    debutPause = pygame.time.get_ticks()
    clock = pygame.time.Clock()
    font = pygame.font.Font("data/menu/font.ttf", round(3/100*diagonalEcran))
    imBouton = pygame.transform.scale(pygame.image.load("data/menu/backButton.png").convert_alpha(), scaleButton)
    menu = Button(imBouton, (tailleEcran[0]*1/2, tailleEcran[1]*1/3+40/100*tailleEcran[1]), "menu", font, "white", "#999999")
    reprendre = Button(imBouton, (tailleEcran[0]*1/2, tailleEcran[1]*1/3), "reprendre", font, "white", "#999999")
    documentation = Button(imBouton, (tailleEcran[0]*1/2, tailleEcran[1]*1/3+20/100*tailleEcran[1]), "documentation", font, "white", "#999999")
    fermer = Button(imBouton, (tailleEcran[0]*1/2, tailleEcran[1]*1/3+55/100*tailleEcran[1]), "fermer", font, "white", "#999999")
    pause = Button(None, (tailleEcran[0]*1/2, tailleEcran[1]*1/3-20/100*tailleEcran[1]), "pause", font, "black", "#999999")
    librairie = False
    
    while(pause):
        mouse = pygame.mouse.get_pos()
        keys=pygame.key.get_pressed()
        librairieIMG = pygame.image.load("data/personnages/infoBulle/librairie.png").convert_alpha()
        
        if keys[K_ESCAPE] and pygame.time.get_ticks()-debutPause>250:
            pause=False
            return pygame.time.get_ticks()-debutPause
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN :
                if reprendre.checkForInput(mouse):
                    pause=False
                    return pygame.time.get_ticks()-debutPause
                if documentation.checkForInput(mouse):
                    librairie = not librairie
                if menu.checkForInput(mouse):
                    main_menu.main_menu()
                if librairie and fermer.checkForInput(mouse):
                    librairie=False
        fenetre.fill("white")
        if librairie:
            fenetrePygame.blit(librairieIMG,(infoObject.current_w-librairieIMG.get_width()-(infoObject.current_w-librairieIMG.get_width())/2,200))
            fermer.changeColor(mouse)
            fermer.update(fenetre)
        else:
            
            reprendre.changeColor(mouse)
            reprendre.update(fenetre)
            documentation.changeColor(pygame.mouse.get_pos())
            documentation.update(fenetre)
            menu.changeColor(pygame.mouse.get_pos())
            menu.update(fenetre)
        pause.update(fenetre)
        pygame.display.flip()
        pygame.event.pump()
        clock.tick(60)

def mort(game):
    fenetrePygame.blit(game.images.mort, (0,0))
    
def victoire(game):
    
    fenetrePygame.blit(game.images.victoire, (0,0))
    
def get_font(size):
    return pygame.font.Font("data/menu/font.ttf", size)

def surEcran(entite, moveX, moveY, infoObject):
    return entite.rect.x>=0 and entite.rect.x<=infoObject.current_w and entite.rect.y>=0 and entite.rect.y<=infoObject.current_h


def gestionMob(game, fps):
    now = game.tempsJeu()
    for mob in game.groupMob:
        majSelectionMob(game, mob)
        if mob.name=="oursin":
            if game.avoirTuileJoueur(mob).trou:
                game.joueur.changerImageBatiment(game.avoirTuileJoueur(mob), "trou_bouche")
                pygame.mixer.Sound.play(game.son.trou)
                modification=True
                game.avoirTuileJoueur(mob).aEteModifie=True
                game.avoirTuileJoueur(mob).trou=False
                game.joueur.score+=mob.score
                game.joueur.setRessource(mob.recompenseWood, mob.recompenseStone, mob.recompenseFood, mob.recompenseWater)
                game.groupLoot.add(Loot(mob.recompenseWood, mob.recompenseStone, mob.recompenseWater, mob.recompenseFood, mob.rect.x+20-moveX, mob.rect.y-30-moveY, game))
                mob.kill()
        
        
        if not mob.pique and not mob.aerien and mob.tuileMob.pieux:
            mob.takeDamage(0.1, moveX, moveY)
            if not mob.slow:
                mob.slow =True


        elif mob.tuileMob.sableMouvant and not mob.aerien :
            mob.takeDamage(0.3, moveX, moveY)
            if game.tempsJeu() - game.son.dernierSable >2000:
                pygame.mixer.Sound.play(game.son.sableMouvantPassage, maxtime=2000)
                game.son.dernierSable = game.tempsJeu()
            if not mob.slow:
                mob.slow =True
                
                mob.velocity=mob.velocity/3
                if mob.velocity<1:
                    mob.velocity=1
                    
        elif mob.tuileMob.ventilo and not mob.aerien:
            mob.takeDamage(0.5, moveX, moveY)
            if game.tempsJeu() - game.son.dernierVentilo >2000:
                pygame.mixer.Sound.play(game.son.ventilo, maxtime=2000)
                game.son.dernierVentilo = game.tempsJeu()

            if not mob.slow:
                mob.slow =True
                
                mob.velocity=mob.velocity/3
                if mob.velocity<1:
                    mob.velocity=1
                    
        elif mob.slow:
            mob.slow =False
            mob.velocity = mob.maxVelocity
        
        if mob.annimal and now-mob.last>=mob.cooldown:
            for i in range(game.taille_matriceY):
                for j in range(game.taille_matriceX):
                    game.map[i][j].traceMob=False
            destX, destY  = mob.destAnnimal()

            mob.the_path=[(destY, destX)]
            #mob.the_path= findPos(game, destX, destY, mob.posX, mob.posY, aqua=mob.aquatique, aerien=mob.aerien, desertique=mob.desertique)
            mob.last = now
            
        elif now-mob.last>=mob.cooldown and mob.fini and not (game.map[game.joueur.posY][game.joueur.posX].caseBloquante() and not mob.aquatique and not mob.aerien) and not (not game.map[game.joueur.posY][game.joueur.posX].caseBloquante() and mob.aquatique):
            mob.the_path = findPos(game, game.joueur.posX, game.joueur.posY, mob.posX, mob.posY, aqua=mob.aquatique, aerien=mob.aerien)
            mob.last = now
            if False:
                traceMob(game, mob.the_path)
            

        if not mob.slow :
            
            mob.fini = mob.allerVersTuile(mob.the_path[0][1], mob.the_path[0][0])
        else :
            if fps%2==0 :
                mob.fini = mob.allerVersTuile(mob.the_path[0][1], mob.the_path[0][0])
                
        if mob.fini and len(mob.the_path)>1:
            mob.the_path = mob.the_path[1:]
            
            
def traceMob(game, the_path):
    for y in range(game.taille_matriceY):
        for x in range(game.taille_matriceX):
            game.map[y][x].traceMob=False
    for posY, posX in the_path:
            game.map[posY][posX].traceMob=True
            
def blitJoueur(fenetrePygame, game):
    if not game.joueur.blit:
        if not game.joueur.bateau:
            fenetrePygame.blit(game.joueur.skin, (game.joueur.rect.x, game.joueur.rect.y))
            game.joueur.blit=True
        elif game.joueur.bateau:
            fenetrePygame.blit(game.joueur.skinBateau, (game.joueur.rect.x-15, game.joueur.rect.y+30))
            game.joueur.blit=True