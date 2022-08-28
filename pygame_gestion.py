import math
from random import randint
import pygame
from pygame.locals import *
from inventaire import Inventaire
from generation import *
from mob import Mob
import main_menu
from selection import colisionItem, majSelection, majSelectionJoueur, selectionDispoItem
from game import Game
#from game import background_pil
from coffre import Coffre
from findPos import *
fenetrePygame = ""
infoObject = 0

global moveY, moveX, suiviePerso


def pygameInit():  # fonction servant à l'initialisation pygame
    
    global infoObject, modification, joueur,timeComtpeur, annimIncendie, delayIncendie,nombreAnnimationIncendie, annimTremblementListe
    global fenetrePygame, moveX, moveY, last, suiviePerso
     #if Options.music == True:
    
    moveY=0
    moveX=0
    last = 0
    annimIncendieListe=[]
    annimTremblementListe=[]
    annimIncendie=0
    suiviePerso=140 #baisser la valeur pour un suivi plus rapide, 130 = suivi parfait
    nombreAnnimationIncendie=3

    # initialise la taille de l'écran (largeur, hauteur) en pixel
    modification = False
    delayIncendie=500
    timeComtpeur=0
    #music = pygame.mixer.music.load("data/Music/level0.mp3")
    # pygame.mixer.music.play(10)
    print("Génération de la map")
    imDebug = pygame.image.load("data/tuiles/debug.png")
    imDebug = pygame.transform.scale(imDebug, (2,2))
    BLACK = (0, 0, 0)
    continuer = True  # répeter à l'infini la fenetre pygame jusqu'a que continuer = false
    fenetrePygame = pygame.init()  # Initialisation de la bibliothèque Pygame
    pygame.mixer.init()

    clock = pygame.time.Clock()
    pygame.key.set_repeat(1, 30)

    infoObject = pygame.display.Info()  # récupère la taille de l'écran
    fenetrePygame = pygame.display.set_mode((infoObject.current_w, infoObject.current_h))
    
    game = Game(infoObject, fenetrePygame)
    
    # mise a l'echelle du perso les argument sont la surface qui est modifie et la taille
    # valeur de x qui place perso au milieu de l'ecran sur l'axe horizontale
    Imselection = pygame.image.load("data/tuiles/selection.png").convert_alpha()
    buttonHome = pygame.image.load("data/menu/buttonHome.png").convert_alpha()
    buttonHome = pygame.transform.scale(buttonHome, (70, 70))
    bookicon = pygame.image.load("data/menu/book.png").convert_alpha()
    bookicon = pygame.transform.scale(bookicon,(50,50))
    pauseicon = pygame.image.load("data/menu/pause.png").convert_alpha()
    pauseicon = pygame.transform.scale(pauseicon,(45,45))

    librairieIMG = pygame.image.load("data/personnages/infoBulle/librairie.png").convert_alpha()
    health = pygame.image.load("data/menu/health.png").convert_alpha()
    health = pygame.transform.scale(health, (50, 50))
    feuille = pygame.image.load("data/menu/feuille.png").convert_alpha()
    feuille = pygame.transform.scale(feuille, (50, 50))

    for i in range(1,10):
        im = pygame.image.load("data/cata/tremblement/tremblement"+str(i)+".png").convert_alpha()
        annimTremblementListe.append(pygame.transform.scale(im, (im.get_width()*1.5, im.get_height()*1.5)))
    for i in range(1,10):
        annimIncendieListe.append(pygame.image.load("data/cata/feu/flamme"+str(i)+".png").convert_alpha())

    tick_ressource=0
    tirageCoffre = 0 #compte le nombre de tirage de coffre rate, 1 tirage toute les 10 secondes
    move_ticker=0
    tuile=False
    librairie=False
    tickBatiment=1000

    inventaire=Inventaire(0,0, [])

    for i in range(-1, 2):
        for j in range(-1, 2):
            game.deleteFog(game.joueur.posX+i, game.joueur.posY+j)
    #game.genererImg()

    centrerJoueur(game)
    
    
    #game.groupMob.add(Mob(game,"golem_des_forets", 100, 2, tuile=game.map[4][4], score=150))
    #game.groupMob.add(Mob(game, "oursin", 150, 3, pique=True, tuile=game.map[1][2], score = 100))
    #game.groupMob.add(Mob(game,"oursin", 100, 2, tuile=game.map[1][1]))
    #game.groupMob.add(Mob(game,"mage", 100, 2, tuile=game.map[1][3]))
    #game.groupMob.add(Mob(game, "kraken", 50, 1, aquatique=True))
    #game.groupMob.add(Mob(game, "dragon", 100, 2,game.map[1][1], aerien=True))
    #game.groupMob.add(Mob(game, "mage", 50, 1, game.map[1][1]))
    #the_path = [[game.groupMob.sprites()[0].posY, game.groupMob.sprites()[0].posX]]
    #fleche= Projectile(game, "fleche", 10, 0,0, game.joueur)
    #game.groupProjectile.add(fleche)
    game.tempsMort+=pygame.time.get_ticks()
    fps = 0 #compte le nombre de fps
    tailleEcran = pygame.display.Info().current_w, pygame.display.Info().current_h
    diagonalEcran = math.sqrt(tailleEcran[0]**2 + tailleEcran[1]**2)
    taillePolice = round(3/100*diagonalEcran)
    while continuer == True:
        scoreText = get_font(taillePolice).render(str(game.joueur.score), True, "Black")
        scoreRect = scoreText.get_rect(center=(tailleEcran[0]*9.5/10, tailleEcran[1]*1.2/10))
        if fps>=60:
            fps =0
        else:
            fps+=1
        game.augmenterMob()
        game.son.jouerMusique()
        modification=False
        cliqueItem = False
        
        modification = KEY_move(game, game.joueur, fenetrePygame)
        listeColide = game.checkCollision(game.joueur, game.groupMob)
        
        for mob in game.groupMob:#Gestion des pieux
            
            if mob.name=="oursin":
                if game.avoirTuileJoueur(mob).trou:
                    game.joueur.changerImageBatiment(game.avoirTuileJoueur(mob), "trou_bouche")
                    pygame.mixer.Sound.play(game.son.trou)
                    modification=True
                    game.avoirTuileJoueur(mob).aEteModifie=True
                    game.avoirTuileJoueur(mob).trou=False
                    game.joueur.score+=mob.score
                    mob.kill()
                    
                    
            
            tuileMob=majSelectionJoueur(game, pos=(mob.getFeet()))
            
            if not mob.pique and not mob.aerien and tuileMob.pieux:
            #if game.map[mob.posY][mob.posX].pieux==True:
                mob.takeDamage(0.1)
                if not mob.slow:
                    mob.slow =True


            elif tuileMob.sableMouvant and not mob.aerien:
                mob.takeDamage(0.3)
                if game.tempsJeu() - game.son.dernierSable >2000:
                    pygame.mixer.Sound.play(game.son.sableMouvantPassage, maxtime=2000)
                    game.son.dernierSable = game.tempsJeu()
                if not mob.slow:
                    mob.slow =True
                    
                    mob.velocity=mob.velocity/3
                    if mob.velocity<1:
                        mob.velocity=1
                        
            elif tuileMob.ventilo and not mob.aerien:
                mob.takeDamage(0.5)
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
                 mob.velocity =mob.maxVelocity
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
                if mouse[0] <= pauseicon.get_width()+76 and mouse[0]>80 and mouse[1] <= 20+pauseicon.get_height():  # detection si clic sur pause
                    tempsPasse = pause(pauseicon)
                    game.tempsMort+=tempsPasse
                if mouse[0] <= 75  and mouse[1] <= 75:  # detection si clic sur menu pricipal
                    continuer = False
                    game.son.stop()
                    
                if mouse[0] <= bookicon.get_width() and mouse[1] <= bookicon.get_height()+80 and mouse[1] >= 80:  # detection si clic sur librairie
                    if librairie ==True : 
                        librairie = False 
                    else : 
                        librairie = True 
                else :
                    librairie = False
                if not cliqueItem:
                    tuile = majSelection(game, pygame.mouse.get_pos(), game.joueur)
                else :
                    if tuile:
                        tuile.estSelect=False
                    tuile=False
            
                
        if continuer == True:  # récupère la position de la souris mais uniquement si la fenetre pygame est ouverte
            
            deplacement_cam(mouse, game)
            
           
            #### Deplacement des mobs
            now = game.tempsJeu()
            for mob in game.groupMob:
                
                if now-mob.last>=mob.cooldown and mob.fini and not (game.map[game.joueur.posY][game.joueur.posX].caseBloquante() and not mob.aquatique and not mob.aerien) and not (not game.map[game.joueur.posY][game.joueur.posX].caseBloquante() and mob.aquatique):
                    mob.the_path = findPos(game, game.joueur.posX, game.joueur.posY, mob.posX, mob.posY, aqua=mob.aquatique, aerien=mob.aerien)
                    
                    mob.last = now
                    mob.majCoolDown()
                if not mob.slow :
                    mob.fini = mob.allerVersTuile(mob.the_path[0][1], mob.the_path[0][0])
                else :
                    if now%2==0 :
                        mob.fini = mob.allerVersTuile(mob.the_path[0][1], mob.the_path[0][0])
                        
                if mob.fini and len(mob.the_path)>1:
                    mob.the_path = mob.the_path[1:]

            for tour in game.groupDefense:
                tour.attack()
            for projo in game.groupProjectile:
                projo.moveProjectile()

            if move_ticker>0:
                move_ticker-=1

            # efface l'image pour pouvoir actualiser le jeu
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
                if game.groupMob.__len__()<9:
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
            for y in range(25):
                for x in range(25):
                    if game.map[y][x].isExplored:
                        fenetrePygame.blit(game.map[y][x].image, (moveX+game.map[y][x].Xoriginal, moveY+game.map[y][x].Yoriginal))
                        if game.map[y][x].annimation:
                            game.map[y][x].changeAnnim()
                            
                    if game.map[y][x].annimationFog>0 and game.map[y][x].isExplored:
                        
                        fenetrePygame.blit(game.map[y][x].imageFog, (moveX+game.map[y][x].Xoriginal, moveY+game.map[y][x].Yoriginal))
                        game.map[y][x].annimationFog-=8
                        game.map[y][x].imageFog.set_alpha(game.map[y][x].annimationFog)
                    else :
                        fenetrePygame.blit(game.map[y][x].imageFog, (moveX+game.map[y][x].Xoriginal, moveY+game.map[y][x].Yoriginal))
                        
                    if game.map[y][x].ville:
                        alerteVille = True
                        tuileVille = game.map[y][x]
            
            

            for coffre in game.groupCoffre:
                if coffre.tuile.posX == game.joueur.posX and coffre.tuile.posY == game.joueur.posY:
                    game.joueur.setRessource(coffre.wood, coffre.stone, coffre.food, coffre.water)
                    pygame.mixer.Sound.play(game.son.coffreOuverture)
                    coffre.kill()
                if coffre.tuile.isExplored :
                    fenetrePygame.blit(coffre.image, (coffre.rect.x+moveX, coffre.rect.y+moveY))
                    fenetrePygame.blit(coffre.imEtoile, (coffre.etoileRect.x+moveX, coffre.etoileRect.y+moveY))  
                    fenetrePygame.blit(coffre.imEtoile2, (coffre.etoileRect2.x+moveX, coffre.etoileRect2.y+moveY))  
                    fenetrePygame.blit(coffre.imEtoile3, (coffre.etoileRect3.x+moveX, coffre.etoileRect3.y+moveY))  
                    if fps%3==0:
                        coffre.etoileAnnim()
            #fenetrePygame.blit(game.map[game.joueur.posY][game.joueur.posX].image, (0,0))
            #fenetrePygame.blit(game.mapImg, (moveX, moveY))
            #fenetrePygame.blit(game.mapImgSuperpose, (moveX, moveY))
            fenetrePygame.blit(buttonHome, (10, 10))
            fenetrePygame.blit(bookicon, (0,80))
            fenetrePygame.blit(pauseicon, (76,20))

            if tuile :
                if not (abs(tuile.posX-game.joueur.posX)<2 and abs(tuile.posY-game.joueur.posY)<2):
                    tuile.estSelect=False
                    tuile=False
            if tuile :
                fenetrePygame.blit(Imselection, (tuile.getRectX(), tuile.getRectY()))
                
                if tuile.tour:      
                    #pygame.draw.circle(fenetrePygame, (155,155,155), (tuile.tour.rect.x+30, tuile.tour.rect.y), tuile.tour.range, width=3, )
                    pass
            #affichage personnage
            
            if not game.joueur.bateau:

                fenetrePygame.blit(game.joueur.skin, (game.joueur.rect.x, game.joueur.rect.y))
            for mob in game.groupMob:
                if game.map[mob.posY][mob.posX].isExplored :
                    fenetrePygame.blit(mob.skin, (mob.rect.x, mob.rect.y))
                fenetrePygame.blit(imDebug, mob.getFeet())

            if game.joueur.bateau:
                fenetrePygame.blit(game.joueur.skinBateau, (game.joueur.rect.x-15, game.joueur.rect.y+30))
                
            for mob in game.groupMob:
                if game.map[mob.posY][mob.posX].isExplored:
                    mob.update_health_bar()
            if tuile :
                liste = selectionDispoItem(game, tuile, game.joueur)
                inventaire = Inventaire(tuile.getRectX()-85, tuile.getRectY()-25, liste)
                inventaire.blitInventaire(fenetrePygame)
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
                else:
                    entreImage=500
                    fenetrePygame.blit(annimTremblementListe[annimIncendie], (annimTremblementListe[-1].rect.x+50, annimTremblementListe[-1].rect.y-annimTremblementListe[annimIncendie].get_height()+100))
                game.incendie=False
                if game.tempsJeu()-delayIncendie>entreImage:
                    annimIncendie+=1

                    
                    delayIncendie=game.tempsJeu()
                    if annimIncendie==9:
                        if nombreAnnimationIncendie>0:
                            annimIncendie=1
                            nombreAnnimationIncendie-=1
                        else:
                            game.joueur.detruireBatimentRessource(annimIncendieListe[-1])
                            annimIncendieListe.pop(len(annimIncendieListe)-1)
                            annimTremblementListe.pop(len(annimTremblementListe)-1)
                            nombreAnnimationIncendie=3
                            annimIncendie=0

            
            
            #if game.joueur.estMort:
            #    fenetrePygame.blit(pygame.image.load("data/menu/gameover.png").convert_alpha(), (200,200))
            if librairie ==True :
                    fenetrePygame.blit(librairieIMG,(infoObject.current_w-librairieIMG.get_width()-(infoObject.current_w-librairieIMG.get_width())/2,200))
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
            game.joueur.update_ecolo_bar()
            fenetrePygame.blit(health, (120,15))
            fenetrePygame.blit(feuille, (10,368))
            fenetrePygame.blit(scoreText, scoreRect)
            if tickBatiment<60:
                fenetrePygame.blit(game.imageErreurRessource, (infoObject.current_w-game.imageErreurRessource.get_width()-(infoObject.current_w-game.imageErreurRessource.get_width())/2,infoObject.current_h - 200))
                tickBatiment+=1

                
            if librairie ==True : 
                i =0
                for mob in game.groupMob : 
                    i+=1
                    fenetrePygame.blit(mob.infoBulle,(50*i,150))
            if game.joueur.estMort:
                mort(game)
            if game.joueur.ville:
                victoire(game)
            pygame.display.flip()
        
        else:
            print("Fermeture du jeu & Lancement du menu principal")
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
    
    
    
    if keys[K_d] or keys[K_RIGHT]:
        if joueur.deplacementAutorise("droite") :
            deplacementCamDroite((infoObject.current_w - suiviePerso,0), game)
            joueur.goRight()
            tuile = majSelectionJoueur(game, joueur.getFeet())
            joueur.setPos(tuile)
            #joueur.majBateau()
            for i in range(-1,2):
                for j in range(-1, 2):
                    if game.deleteFog(joueur.posX+i, joueur.posY+j): ##MODIFICATION
                        modification=True

                
                
    if keys[K_q]or keys[K_LEFT]:
            if joueur.deplacementAutorise("gauche"):
                #joueur.majBateau()
                deplacementCamGauche((suiviePerso, 0), game)
                joueur.goLeft()
                tuile = majSelectionJoueur(game, joueur.getFeet())
                joueur.setPos(tuile)
                for i in range(-1,2):
                    for j in range(-1, 2):
                        if game.deleteFog(joueur.posX+i, joueur.posY+j): ##MODIFICATION
                            modification=True
    

    if keys[K_z] or keys[K_UP]:
            if joueur.deplacementAutorise("haut"):
                #joueur.majBateau()
                deplacementCamHaut((0,suiviePerso), game)
                joueur.goUp(haut)
                tuile = majSelectionJoueur(game, joueur.getFeet())
                joueur.setPos(tuile)
                for i in range(-1,2):
                    for j in range(-1, 2):
                        if game.deleteFog(joueur.posX+i, joueur.posY+j): ##MODIFICATION
                            modification=True

    if keys[K_s]or keys[K_DOWN]:
            if joueur.deplacementAutorise("bas"):
                deplacementCamBas((0, infoObject.current_h-suiviePerso), game)
                joueur.goDown(bas)
                tuile = majSelectionJoueur(game, joueur.getFeet())
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
    
    return modification, tuile


def deplacement_cam(mouse, game): #gestion du déplacement de la caméra 
    deplacementCamBas(mouse, game)
    deplacementCamDroite(mouse, game)
    deplacementCamGauche(mouse, game)
    deplacementCamHaut(mouse, game)
    
def centrerJoueur(game):
    while game.joueur.rect.x < infoObject.current_w//2-10:
        deplacementCamGauche((199,0), game)

    while game.joueur.rect.x > infoObject.current_w//2+10:
        deplacementCamDroite((infoObject.current_w-199,0), game)


    while game.joueur.rect.y > infoObject.current_h//2-10:
        deplacementCamBas((0,infoObject.current_h-199), game)

    while game.joueur.rect.y < infoObject.current_h//2+10:
        deplacementCamHaut((0,199), game)



def deplacementCamBas(mouse, game):
    global moveY, moveX
    x=infoObject.current_h-mouse[1]
    y=f(x)
    if x < 200 :  # Si souris en bas
        
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
        
def deplacementCamHaut(mouse, game):
    global moveY, moveX
    x = mouse[1]
    y = -f(x)
    if x < 200 : #Si souris en haut
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
        
def deplacementCamGauche(mouse, game):
    global moveY, moveX
    x= mouse[0]
    y = -f(x)
    if x < 200:  # Si souris à gauche
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
        
def deplacementCamDroite(mouse, game):
    global moveY, moveX
    x = infoObject.current_w-mouse[0]
    y=f(x)

    if x < 200:  # Si souris à droite
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

def pause(pauseicon):
    pause=True
    debutPause = pygame.time.get_ticks()
    while(pause):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse=pygame.mouse.get_pos()
                if mouse[0] <= 76+pauseicon.get_width() and mouse[0]>76 and mouse[1] <= 20 + pauseicon.get_height():
                    pause=False
                    return pygame.time.get_ticks()-debutPause
        
def mort(game):
    fenetrePygame.blit(game.images.mort, (0,0))
    
def victoire(game):
    
    fenetrePygame.blit(game.images.victoire, (0,0))
    
def get_font(size):
    return pygame.font.Font("data/menu/font.ttf", size)

