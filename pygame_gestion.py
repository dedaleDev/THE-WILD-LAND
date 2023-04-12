import math
import operator
import pygame
from pygame.locals import *
from boss import Boss
from inventaire import Inventaire
from generation import *
from loot import Loot
import main_menu
from mob import Mob
from selection import colisionItem, majSelection, majSelectionJoueur, majSelectionMob, selectionDispoItem
from game import Game
#from game import background_pil
from button import Button
import tuto
from findPos import *
fenetrePygame = ""


global moveY, moveX, suiviePerso 


def pygameInit(mapChoisie,pointSpawn):  # fonction servant à l'initialisation pygame
    
    global infoObject, modification, joueur,timeComtpeur, annimIncendie, delayIncendie,nombreAnnimationIncendie, annimTremblementListe
    global fenetrePygame, moveX, moveY, last, suiviePerso
    listeBoss=[]
    moveY=0
    moveX=0
    last = 0
    annimIncendieListe=[]
    annimTremblementListe=[]
    nombreAnnimationIncendie=3
    annimIncendie=0
    suiviePerso=136
    nombreAnnimationTremblement=3


    # initialise la taille de l'écran (largeur, hauteur) en pixel
    modification = False
    delayIncendie=500
    timeComtpeur=0
    imDebug = pygame.image.load("data/tuiles/debug.png").convert_alpha()
    imDebug2 = pygame.transform.scale(imDebug, (60,60))
    imDebug = pygame.transform.scale(imDebug, (2,2))
    
    
    
    
    
    BLACK = (0, 0, 0)
    pygame.mixer.init()
    continuer = 1
    fenetrePygame = pygame.init()  # Initialisation de la bibliothèque Pygame


    clock = pygame.time.Clock()
    pygame.key.set_repeat(1, 30)
    reelEcran = pygame.display.Info()
    
    infoObject =  (int(aideCSV.valCorrespondante("largeurEcran")), int(aideCSV.valCorrespondante("hauteurEcran"))) # récupère la taille de l'écran
    tailleEcran = infoObject[0], infoObject[1]
    diagonalEcran = math.sqrt(tailleEcran[0]**2 + tailleEcran[1]**2)
    statImg = pygame.image.load("data/menu/stat.png").convert_alpha()
    statImg = pygame.transform.scale(statImg, (statImg.get_width()*diagonalEcran*0.00035, statImg.get_height()*diagonalEcran*0.00035))

    
    
    opti = int(aideCSV.valCorrespondante("optimisation"))
    
    if not opti:
        #flags = pygame.FULLSCREEN | pygame.DOUBLEBUF | pygame.SCALED | pygame.HWSURFACE
        fenetrePygame = pygame.display.set_mode((infoObject[0], infoObject[1]))
        
    elif opti == 1 :
        flags = pygame.FULLSCREEN | pygame.DOUBLEBUF | pygame.SCALED | pygame.HWSURFACE
        fenetrePygame = pygame.display.set_mode((infoObject[0], infoObject[1]),flags)
    elif opti == 2:
        flags = pygame.FULLSCREEN | pygame.DOUBLEBUF | pygame.SCALED | pygame.HWSURFACE
        fenetrePygame = pygame.display.set_mode((infoObject[0], infoObject[1]),flags)

    fenetrePygame.fill("black")
    im = pygame.image.load("data/menu/chargement.png")
    chargement = pygame.transform.scale(im, (infoObject[0], infoObject[1]))
    chargement.set_alpha(0)
    while chargement.get_alpha()<150:
        chargement.set_alpha(chargement.get_alpha()+5)
        fenetrePygame.blit(chargement, (0,0))
        pygame.display.flip()
        clock.tick(60)
    game = Game(infoObject, fenetrePygame, mapChoisie, pointSpawn)
    game.listeTuto=tuto.createTuto(game)#creation des tutoriels
    # mise a l'echelle du perso les argument sont la surface qui est modifie et la taille
    # valeur de x qui place perso au milieu de l'ecran sur l'axe horizontale
    Imselection = pygame.image.load("data/tuiles/selection.png").convert_alpha()
    buttonHome = pygame.image.load("data/menu/buttonHome.png").convert_alpha()
    buttonHome = pygame.transform.scale(buttonHome, (70, 70))
    bookicon = pygame.image.load("data/menu/book.png").convert_alpha()
    bookicon = pygame.transform.scale(bookicon,(50,50))
    pauseicon = pygame.image.load("data/menu/pause.png").convert_alpha()
    pauseicon = pygame.transform.scale(pauseicon,(45,45))
    indiceBackArene=0
    indiceBackMonde=0

    infobulleIncendie = pygame.image.load("data/cata/infoBulle/info_incendie.png").convert_alpha()
    infoMortAnnimal = pygame.image.load("data/cata/infoBulle/infoMort.png").convert_alpha()

    infobulletremb = pygame.image.load("data/cata/infoBulle/info_tremblementDeTerre.png").convert_alpha()
    
    health = pygame.image.load("data/menu/health.png").convert_alpha()
    health = pygame.transform.scale(health, (50, 50))
    feuille = pygame.image.load("data/menu/feuille.png").convert_alpha()
    feuille = pygame.transform.scale(feuille, (50, 50))
    scoreBar = pygame.image.load("data/menu/score.png").convert_alpha()
    scoreBar = pygame.transform.scale(scoreBar, (scoreBar.get_width()*0.25,scoreBar.get_height()*0.25))
    pygame.event.set_allowed([QUIT, KEYDOWN, KEYUP, MOUSEBUTTONDOWN, MOUSEBUTTONUP])
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

    inventaire=Inventaire(0,0, [], game)

    for i in range(-1, 2):
        for j in range(-1, 2):
            game.deleteFog(game.joueur.posX+i, game.joueur.posY+j)

    centrerJoueur(game)
    game.spawnAnnimal(5)


    #game.groupMob.add(Mob(game,"oursin", 200, 2, tuile=game.map[4][4], score=150))

    #game.groupMob.add(Mob(game,"dragon", 100, 2, tuile=game.map[4][4], score=150))
    #game.groupCoffre.add(Coffre(game, game.map[10][10], 100,100,100,100))
    #game.groupMob.add(Mob(game,"oiseau", 100, 2, tuile=game.map[4][4], score=150, aerien=True, annimal=True, attaque=0))
    #game.groupMob.add(Mob(game,"chameau", 100, 1, tuile=game.map[3][3], score=0, desertique=True, annimal=True, attaque=0))
    #game.groupMob.add(Mob(game,"oiseau", 100, 2, tuile=game.map[4][4], score=150, aerien=True, annimal=True, attaque=0))
    #game.groupMob.add(Mob(game,"oiseau", 100, 2, tuile=game.map[4][4], score=150, aerien=True, annimal=True, attaque=0))
    #game.groupMob.add(Mob(game,"oiseau", 100, 2, tuile=game.map[4][4], score=150, aerien=True, annimal=True, attaque=0))
    #game.groupMob.add(Mob(game,"oursin", 100, 1, tuile=game.map[4][4], score=150))
    
    #game.groupMob.add(Mob(game,"mage", 100, 2, tuile=game.map[4][4], score=150))
    #game.groupMob.add(Mob(game,"kraken", 100, 2, tuile=game.map[4][4], score=150, aquatique=True))
    
    
    #game.groupMob.add(Mob(game,"oursin", 100, 2, tuile=game.map[4][4], score=150))
    #game.groupMob.add(Mob(game, "oursin", 150, 3, pique=True, tuile=game.map[1][2], score = 100))
    listefps=[]
    game.tempsMort+=pygame.time.get_ticks()
    fps = 0 #compte le nombre de fps
    tailleEcran = pygame.display.Info().current_w, pygame.display.Info().current_h
    diagonalEcran = math.sqrt(tailleEcran[0]**2 + tailleEcran[1]**2)
    taillePolice = round(3/100*diagonalEcran)
    police = get_font(taillePolice)
    smallTaillePolice = round(1.5/100*diagonalEcran)
    smallPolice = get_font(smallTaillePolice)
    verySmallTaillePolice = round(1.1/100*diagonalEcran)
    verySmallPolice = get_font(verySmallTaillePolice)
    indiceFleche=0
    badSelec=-1
    print(game.modeFacile)
    print(game.modeDifficile)
    while continuer:
        
        listeBlitHealthBarDessus=[]
        debut = pygame.time.get_ticks()
        game.joueur.blit=False
        
        scoreText = smallPolice.render(str(game.joueur.score), True, "Black")
        scoreRect = scoreText.get_rect(center=(tailleEcran[0]*9.3/10, tailleEcran[1]*9.55/10))
        
        if fps>=60:
            fps =0
            listefps.append(clock.get_fps())
        else:
            fps+=1
        
        
        game.son.jouerMusique2()
        
        modification=False
        cliqueItem = False

        modification = KEY_move(game, game.joueur, fenetrePygame)

        
        listeColide = game.checkCollision(game.joueur, game.groupMob)
        


        if not game.boss:
            gestionMob(game, fps)
        if game.theBoss and game.theBoss.health>0:
            game.theBoss.moveBoss()
            game.theBoss.lunchProjectile()
        
        keys=pygame.key.get_pressed()
        if keys[K_ESCAPE] and pygame.time.get_ticks() - game.lastPause > 250:
            tempsPasse = pause(fenetrePygame, game)
            game.lastPause = pygame.time.get_ticks()
            game.tempsMort+=tempsPasse
        if keys[K_SPACE]:
            centrerJoueur(game)

        if game.joueur.getTuile().ville or (keys[K_r] and keys[K_e] and keys[K_l]):
            game.boss=True
            game.map=game.mapBoss
            for i in range(7):
                for j in range(7):
                    game.map[i][j].rect.x = game.mapWorld[i][j].rect.x
                    game.map[i][j].rect.y = game.mapWorld[i][j].rect.y
            
            
            game.map[0][0].annimation=game.images.arene
            game.map[0][0].clockAnnimMax=3
            game.map[0][0].clockAnnim=0
            game.map[0][0].arene=True
            tuilePos = game.map[1][1]
            game.joueur.setPos(tuilePos)
            game.joueur.rect.x, game.joueur.rect.y=tuilePos.rect.x,tuilePos.rect.y
            centrerJoueur(game)
            game.taille_matriceX=len(game.map)
            game.taille_matriceY=len(game.map[0])
            game.theBoss = Boss(game, 100)
            
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == QUIT:
                continuer = 0

            
            
            if event.type == pygame.MOUSEBUTTONDOWN :  # si clic souris
                for tutoT in game.listeTuto:
                    tutoT.CheckClic(pygame.mouse.get_pos())
                    
                for item in inventaire.listeItem: 
                    if colisionItem(item, pygame.mouse.get_pos()) and tuile: #on a une tuile de selectionné
                        batimentConstruit = game.joueur.construireBatiment(tuile, item)
                        modification=True
                        cliqueItem=True
                        if not batimentConstruit:
                            tickBatiment=0
                
                if not cliqueItem:
                    tuile, cliEnDehors = majSelection(game, pygame.mouse.get_pos(), game.joueur, infoDehors=True)
                    if cliEnDehors:
                        if badSelec==-1:
                            badSelec=0
                    

                    
                
                else :
                    if tuile:
                        tuile.estSelect=False
                    tuile=False
                    
                if tuile and tuile.build:
                    tuile.estSelect=False
                    tuile=False
                if tuile:
                    for build in game.groupBuild:
                        rectBuild = pygame.Rect(build.rect.x+10, build.rect.y-80-30,220,240)
                        if rectBuild.collidepoint(pygame.mouse.get_pos()):
                            tuile.estSelect=False
                            tuile=False
                            break
                    
                for build in game.groupBuild:
                    if build.checkClick():
                        if tuile:
                            tuile.estSelect=False
                        tuile=False

       
        
        
            
        if continuer: 
            
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
            
            if fps==0 :
                if game.groupMob.__len__()-game.nbAnnimaux<9:
                    game.spawMob()
                    game.majMob()
            
                
            
            modification=True
            #affichage selection
            if tick_ressource==0:
                tick_ressource=600
                game.joueur.ajouterRessources()
                
                for batiment in game.listeCaseBatiment:
                    bonus=0
                    if batiment in game.groupTuileBoost:
                        bonus=3
                    
                    if batiment.type==2 and batiment.mine:
                        game.groupLoot.add(Loot(0, 4+bonus, 0, 0, batiment.Xoriginal+70, batiment.Yoriginal+50, game))
                        game.joueur.setStone(bonus)
                    if batiment.type==4 and batiment.scierie:
                        game.groupLoot.add(Loot(5+bonus, 0, 0, 0, batiment.Xoriginal+70, batiment.Yoriginal+50, game))
                        game.joueur.setWood(bonus)
                    if batiment.type==3 and batiment.moulin:
                        game.groupLoot.add(Loot(0, 0, 3+bonus, 0, batiment.Xoriginal+70, batiment.Yoriginal+50, game))
                        game.joueur.setWater(bonus)
                    if batiment.type==1:
                        if batiment.elevage:
                            game.groupLoot.add(Loot(0, 0, 0, 4+bonus, batiment.Xoriginal+70, batiment.Yoriginal+50, game))
                            game.joueur.setFood(bonus)
                        if batiment.champs:
                            game.groupLoot.add(Loot(0, 0, 0, 1+bonus, batiment.Xoriginal+70, batiment.Yoriginal+50, game))
                            game.joueur.setFood(bonus)
                            
                chanceCoffre = random.randint(0,100)
                if chanceCoffre < tirageCoffre :
                    if not game.boss:
                        game.joueur.genererCoffre()
                    tirageCoffre=0
                else :
                    tirageCoffre+=5
                
                
                if not random.randint(0,((round(game.joueur.MaxEcolo-game.joueur.indiceEcolo))%10)):
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
            

            alerteVille=False #une ville est presente sur la map
            game.moveX, game.moveY = moveX, moveY
            listeMontagne=[]
            if game.boss:
                fenetrePygame.blit(game.backgroundArene[indiceBackArene], (0,0))
                if fps%2==0:
                    indiceBackArene+=1
                if indiceBackArene>=len(game.backgroundArene):
                    indiceBackArene=0
            else:
                fenetrePygame.blit(game.backgroundMonde[indiceBackMonde], (0,0))
                if fps%4==0:
                    indiceBackMonde+=1
                if indiceBackMonde>=len(game.backgroundMonde):
                    indiceBackMonde=0
            for y in range(game.taille_matriceY):
                for x in range(game.taille_matriceX):
                    tuileBlit = game.map[y][x]
                    if tuileBlit.isExplored:
                        if (tuileBlit.type==4 or tuileBlit.type==10) and not game.boss: #affichage des annim sans socle
                            
                            listeMontagne.append(tuileBlit)
                        if (tuileBlit.type==2 or tuileBlit.type==7) and not game.boss:
                            listeMontagne.append(tuileBlit)
                            
                            
                            if x==0 or y==game.taille_matriceY-1:
                                fenetrePygame.blit(game.images.backVolcan, (tuileBlit.rect.x, tuileBlit.rect.y+70))
                        else:
                            #affichage des tuiles
                            #fenetrePygame.blit(tuileBlit.image, (moveX+tuileBlit.Xoriginal, moveY+tuileBlit.Yoriginal))
                            if tuileBlit.arene:
                                fenetrePygame.blit(tuileBlit.image, (tuileBlit.rect.x, tuileBlit.rect.y-360-145))
                            else:
                                if not game.boss:
                                    
                                    fenetrePygame.blit(tuileBlit.image, tuileBlit.rect)
                            
                            if tuileBlit.surAnnimListe:
                                fenetrePygame.blit(tuileBlit.surAnnimListe[tuileBlit.indicesurAnnim], tuileBlit.rect)
                            if tuileBlit.indiceSurbrillance>=0:
                                fenetrePygame.blit(tuileBlit.surbrillance[tuileBlit.indiceSurbrillance], tuileBlit.rect)
                            if tuileBlit.statue and tuileBlit.type!=4 and tuileBlit.type!=10:
                                fenetrePygame.blit(game.images.statue(tuileBlit.type), tuileBlit.rect)
                        if tuileBlit.type!=4 and tuileBlit.type!=10:
                            tuileBlit.changeAnnim()
                        else:
                            tuileBlit.changeAnnim(annim=False)
                    if tuileBlit.traceMob:
                        fenetrePygame.blit(Imselection, (tuileBlit.getRectX(), tuileBlit.getRectY()))
                
                    if tuileBlit.annimationFog>0 and tuileBlit.isExplored:
                        
                        fenetrePygame.blit(tuileBlit.imageFog, (moveX+tuileBlit.Xoriginal, moveY+tuileBlit.Yoriginal))
                        tuileBlit.annimationFog-=8
                        tuileBlit.imageFog.set_alpha(tuileBlit.annimationFog)
                    elif not tuileBlit.isExplored:
                        fenetrePygame.blit(tuileBlit.imageFog, (moveX+tuileBlit.Xoriginal, moveY+tuileBlit.Yoriginal))
                        
                    if tuileBlit.ville:
                        alerteVille = True
                        tuileVille = tuileBlit
                        
            
            
                    
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
                if not game.boss:
                    if game.map[mob.posY][mob.posX].isExplored :
                        #fenetrePygame.blit(mob.skin, (mob.rect.x, mob.rect.y))
                        if mob.name=="dragon":
                            listeOrdre.append((mob.skin, mob.rect.x, mob.rect.y, mob.rect.center[1]+500,None, None, None))
                        else:
                            listeOrdre.append((mob.skin, mob.rect.x, mob.rect.y, mob.rect.center[1],None, None, None))
                    if not mob.annimal:
                        if mob.name=="dragon":
                            listeBlitHealthBarDessus.append(mob)
                        mob.update_health_bar()
                        
            
                
    

            ####PASSAGE DES MONTAGNES
            if tuile :
                fenetrePygame.blit(Imselection, (tuile.getRectX(), tuile.getRectY()))
                if not ((tuile.posX, tuile.posY) in listeBoss):
                    listeBoss.append((tuile.posX, tuile.posY))
                if tuile.tour:
                    #pygame.draw.circle(fenetrePygame, (155,155,155), (tuile.tour.rect.x+30, tuile.tour.rect.y), tuile.tour.range, width=3, )
                    pass
            decalageYcentre = -100
            for tuile2 in listeMontagne:
                if tuile2.type==2:
                    center = tuile2.centerOriginal
                    if tuile2.mortier:
                        listeOrdre.append((tuile2.image, moveX+tuile2.Xoriginal, moveY+tuile2.Yoriginal-85, center[1]+moveY-92-decalageYcentre, None, None, tuile2.type))
                    #fenetrePygame.blit(tuile2.image, (moveX+tuile2.Xoriginal, moveY+tuile2.Yoriginal-112))
                    else:
                        listeOrdre.append((tuile2.image, moveX+tuile2.Xoriginal, moveY+tuile2.Yoriginal-112, moveY+center[1]-112-decalageYcentre, tuile2.indiceSurbrillance, tuile2.statue, tuile2.type))
                elif tuile2.type==4 or tuile2.type==10:
                    center = tuile2.centerOriginal
                    
                    listeOrdre.append((tuile2.annimation[0], moveX+tuile2.Xoriginal, moveY+tuile2.Yoriginal-75, center[1]+moveY-100-decalageYcentre, tuile2.indiceSurbrillance, tuile2.statue, tuile2.type))
                else :
                    center = tuile2.centerOriginal
                    
                    #fenetrePygame.blit(tuile2.image, (moveX+tuile2.Xoriginal, moveY+tuile2.Yoriginal-80))
                    
                    listeOrdre.append((tuile2.image, moveX+tuile2.Xoriginal, moveY+tuile2.Yoriginal-92, center[1]+moveY-92-decalageYcentre, tuile2.indiceSurbrillance, tuile2.statue, tuile2.type))
            
            if not game.joueur.bateau:
                fenetrePygame.blit(game.joueur.skin, (game.joueur.rect.x, game.joueur.rect.y))
                center = game.joueur.rect.center
                
                listeOrdre.append((game.joueur.skin, game.joueur.rect.x, game.joueur.rect.y, center[1], None, None, None))

            elif game.joueur.bateau:
                #fenetrePygame.blit(game.joueur.skinBateau, (game.joueur.rect.x-15, game.joueur.rect.y+30))
                center = game.joueur.rect.center

                listeOrdre.append((game.joueur.skinBateau, game.joueur.rect.x-15, game.joueur.rect.y+30, center[1]+30, None, None, None))
            if game.theBoss and game.theBoss.health>0:
                listeOrdre.append((game.theBoss.image, game.theBoss.rect.x-15, game.theBoss.rect.y+30, center[1]+30, None, None, None))
                listeOrdre.append((game.theBoss.imageBoule, game.theBoss.rect.x+40, game.theBoss.rect.y+110, center[1]+32, None, None, None))
                #game.theBoss.rect.x-15, game.theBoss.rect.y+30
            listeOrdre.sort(key=lambda x: x[3])
            
            for image, posX, posY, center, surbrillance, statue, typet in listeOrdre:
                fenetrePygame.blit(image, (posX, posY))
                if surbrillance!=-1 and surbrillance!=None:
                    fenetrePygame.blit(game.images.surbrillance[surbrillance], (posX, posY))
                if statue:
                    fenetrePygame.blit(game.images.statue(typet), (posX+30, posY+30))
            
            for loot in game.groupLoot:
                loot.update(fenetrePygame, moveX,moveY)
            
            
            for build in game.groupBuild:
                build.update()
                #fenetrePygame.blit(build.image, (build.rect.x-50, build.rect.y-70))
                fenetrePygame.blit(build.image, (build.rect.x-50, build.rect.y-70-80))
                if build.imageClickPassif and build.actuelClick:
                    #pygame.draw.rect(fenetrePygame, (255,255,255), build.actuelClick, 1)
                    
                    fenetrePygame.blit(build.imageClickPassif, build.actuelClick)
            for mob in listeBlitHealthBarDessus:
                mob.update_health_bar()
                
            if tuile :
                
                liste = selectionDispoItem(game, tuile, game.joueur)
                inventaire = Inventaire(tuile.getRectX()-50, tuile.getRectY()-25, liste, game)
                inventaire.blitInventaire(fenetrePygame, game.joueur)
                for item in inventaire.listeItem:
                        if colisionItem(item, pygame.mouse.get_pos()):##INFO BULLE##
                            inventaire.blitInfoBulle(fenetrePygame, item)

            for projectile in game.groupProjectile:              
                fenetrePygame.blit(projectile.img, (projectile.rect.x, projectile.rect.y))


            for collision in listeColide:
                fenetrePygame.blit(game.imCollision,(random.randint(game.joueur.rect.x-20, game.joueur.rect.x+20), random.randint(game.joueur.rect.y, game.joueur.rect.y+120)))
            
            if alerteVille:
                fenetrePygame.blit(game.images.ville, (tuileVille.rect.x, tuileVille.rect.y-100))
            
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


            #(infoObject[0]/1.7*(190*i), 25)
            if game.theBoss:
                game.theBoss.update()
                game.theBoss.drawHealthBar(fenetrePygame)
            else:
                for i in range(len(game.joueur.ressourcesIMG)):
                    fenetrePygame.blit(game.joueur.ressourcesIMG[i], (infoObject[0]/1.1-(infoObject[1]/6.3*i), 0.9/100*infoObject[1]))
                    fenetrePygame.blit(game.joueur.RessourcesTEXT[i], (infoObject[0]/1.06-(infoObject[1]/6.3*i), 1.5/100*infoObject[1]))
                    if game.joueur.RessourcesInfoModified[i] != False:
                        timeComtpeur +=1
                        if timeComtpeur <=60 :
                            fenetrePygame.blit(game.joueur.RessourcesInfoModified[i],(infoObject[0]-95-(190*i),90))
                        else :
                            timeComtpeur = 0
                            game.joueur.resetRessourcesModified()
            game.joueur.update_health_bar()
            
                
            if game.joueur.imageArmure:
                fenetrePygame.blit(game.joueur.imageArmure, (22,80))
            
            if not game.theBoss:
                game.joueur.update_ecolo_bar()
                fenetrePygame.blit(feuille, (10,368))
            fenetrePygame.blit(health, (20,15))
            
            for annimMort in game.groupMobMort:
                annimMort.update(fenetrePygame)
            
            if fps%2==0:
                indiceFleche+=1
            if indiceFleche>111:
                indiceFleche=0
            posXfleche=5
            posYfleche=359
            if not game.theBoss:
                if game.joueur.indiceEcolo>=80:
                    
                    fenetrePygame.blit(game.images.fleche[0][indiceFleche], (posXfleche,posYfleche))
                elif game.joueur.indiceEcolo>=40:
                    fenetrePygame.blit(game.images.fleche[1][indiceFleche], (posXfleche,posYfleche))
                else:
                    #game.images.changerimgCouleur(game.images.fleche[2][indiceFleche], [0,125,0])
                    fenetrePygame.blit(game.images.fleche[2][indiceFleche], (posXfleche,posYfleche))
                
                    
            fenetrePygame.blit(scoreBar, (game.infoObject[0]*0.88,game.infoObject[1]*0.92))
            fenetrePygame.blit(scoreText, scoreRect)
            if tickBatiment<60:
                fenetrePygame.blit(game.imageErreurRessource, (infoObject[0]-game.imageErreurRessource.get_width()-(infoObject[0]-game.imageErreurRessource.get_width())/2,infoObject[1] - 200))
                tickBatiment+=1
            if game.infoMortAnnimal>0:
                fenetrePygame.blit(infoMortAnnimal, (tailleEcran[0]- 400, tailleEcran[1] - 700))
                game.infoMortAnnimal-=1
            
            #for pos in game.listeDebug:
                #fenetrePygame.blit(imDebug2, pos)
            if game.win:
                victoire(game)
            if game.joueur.estMort:
                mort(game)
            #if game.joueur.ville:
                #victoire(game)
            
            
            
            if False: #### PASSER A TRUE POUR HITBOX
                for projectile in game.groupProjectile:
                    pygame.draw.rect(fenetrePygame, (255,255,255), projectile.rect, width=3)
                
                for mob in game.groupMob:
                    pygame.draw.rect(fenetrePygame, (255,255,255), mob.rect, width=3)
                for mob in game.groupJoueur:
                    pygame.draw.rect(fenetrePygame, (255,255,255), mob.rect, width=3)

            if game.stat : 
                tuto.disableTuto(game)
                game.stat =False
                fenetrePygame.blit(statImg, (infoObject[0]*0.705,infoObject[1]*0.1))
                #recup 
                productionWood, productionStone, productionWater, productionFood, recuperationEcolo, nbAnnimauxMort, ennemieDegat = stat(game)
                #render : 

                productionWood = smallPolice.render(str(productionWood), True, (0, 0, 0))
                productionWater = smallPolice.render(str(productionWater), True, (0, 0, 0))
                productionStone = smallPolice.render(str(productionStone), True, (0, 0, 0))
                productionFood = smallPolice.render(str(productionFood), True, (0, 0, 0))

                titleEco= smallPolice.render("Environnement ", True, (0, 0, 0))
                nbAnnimauxMort= verySmallPolice.render("Animaux décédés :  "+str(nbAnnimauxMort), True, (0, 0, 0))
                recuperationEcolo= verySmallPolice.render("Gain écologique :  "+str(recuperationEcolo), True, (0, 0, 0))

                titleCombat= smallPolice.render("Combats ", True, (0, 0, 0))
                ennemieDegat= verySmallPolice.render("Pire ennemi : "+str(ennemieDegat), True, (0, 0, 0))
                fps2 = smallPolice.render("FPS  "+str(int(clock.get_fps())), True, (0,0, 0))
                temps=game.tempsJeuMinute()-int(game.tempsJeuMinute())
                temps = temps/1*60
                time = smallPolice.render("Temps  "+str(int(game.tempsJeuMinute()))+":"+str(round(temps,1)), True, (0,0, 0))
                #blit : 
                fenetrePygame.blit(productionWood,(infoObject[0]*0.91, infoObject[1]*0.29))
                fenetrePygame.blit(productionWater,(infoObject[0]*0.91, infoObject[1]*0.34))
                fenetrePygame.blit(productionFood,(infoObject[0]*0.78, infoObject[1]*0.29))
                fenetrePygame.blit(productionStone,(infoObject[0]*0.78, infoObject[1]*0.34))

                fenetrePygame.blit(titleEco,(infoObject[0]*0.72, infoObject[1]*0.4))
                fenetrePygame.blit(nbAnnimauxMort,(infoObject[0]*0.74, infoObject[1]*0.44))
                fenetrePygame.blit(recuperationEcolo,(infoObject[0]*0.74, infoObject[1]*0.48))

                fenetrePygame.blit(titleCombat,(infoObject[0]*0.72, infoObject[1]*0.51))
                fenetrePygame.blit(ennemieDegat,(infoObject[0]*0.74, infoObject[1]*0.55))
                
                fenetrePygame.blit(fps2,(infoObject[0]*0.72, infoObject[1]*0.6))
                fenetrePygame.blit(time,(infoObject[0]*0.72, infoObject[1]*0.65))
                
            if badSelec>=0:
                if fps%2:
                    badSelec+=1
                for x in range(-1,2):
                    for y in range(-1,2):
                        if x!=0 or y!=0:
                            fenetrePygame.blit(game.images.annimBadSelection[badSelec], game.map[game.joueur.posY+y][game.joueur.posX+x])
                if badSelec==76:
                    badSelec=-1
                
                
                
            if game.text:
                game.displayTxt()
                
            if game.boss:
                game.theBoss.update_health_bar()
            #tuto
            if game.tempsJeu()>1000*5:
                tuto.upadateStatutTuto(game,"move")
            if game.tempsJeu()>1000*30:
                tuto.upadateStatutTuto(game,"mouse")
            if game.tempsJeu()>1000*60:
                tuto.upadateStatutTuto(game,"build")
            if game.tempsJeu()>1000*60*5:
                tuto.upadateStatutTuto(game,"esc")
            if game.tempsJeu()>1000*60*4:
                tuto.upadateStatutTuto(game,"health")
            if game.tempsJeu()>1000*60*10:
                tuto.upadateStatutTuto(game,"score")
            if game.tempsJeu()>1000*60*6:
                tuto.upadateStatutTuto(game,"statut")
            if game.tempsJeu()>1000*60*8:
                tuto.upadateStatutTuto(game,"stat")
            if game.tempsJeu()>1000*60*1.3:
                tuto.upadateStatutTuto(game,"espace")
            if not game.theBoss:
                tuto.afficherTuto(fenetrePygame,game)
            game.joueur.updateBateau()
            if game.annimDegat>=0:
                fenetrePygame.blit(game.images.annimDegat[game.annimDegat],(0, 0))
                game.annimDegat+=1
                if game.annimDegat>=len(game.images.annimDegat):
                    game.annimDegat=-1
            #if game.theBoss:
                #if game.theBoss.directionRush:
                    #pygame.draw.rect(fenetrePygame, (255,0,255), pygame.Rect(game.theBoss.directionRush.rect.x, game.theBoss.directionRush.rect.y, 100,100))
            
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
        
    else:
        
        game.joueur.lunchProjectile()
    if keys[K_i]:
        game.stat = True
    
    if (keys[K_q]or keys[K_LEFT]) or (keys[K_d] or keys[K_RIGHT]) or keys[K_z] or keys[K_UP] or keys[K_s]or keys[K_DOWN]:
        game.joueur.attendre=0
    else:
        game.joueur.attendre+=1
    bug=False
    if keys[K_d] or keys[K_RIGHT]:
        if bug:=joueur.deplacementAutorise("droite") :
            
            deplacementCamDroite((infoObject[0] - suiviePerso,0), game, True, True)
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
                deplacementCamGauche((suiviePerso, 0), game, True, True)
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
                deplacementCamHaut((0,suiviePerso), game, True, True)
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
                deplacementCamBas((0, infoObject[1]-suiviePerso), game, True, True)
                joueur.goDown(bas)
                tuile = majSelectionJoueur(game)
                if tuile!=None:
                    joueur.setPos(tuile)
                #joueur.majBateau()
                for i in range(-1,2):
                    for j in range(-1, 2):
                        if game.deleteFog(joueur.posX+i, joueur.posY+j): ##MODIFICATION
                            modification=True
                

    """if keys[K_b]:
        if game.map[joueur.posY][joueur.posX].port:
            joueur.bateau=True
    if keys[K_v]:
        if game.map[joueur.posY][joueur.posX].port:
            joueur.bateau = False"""
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
    while game.joueur.rect.x < infoObject[0]//2-10:
        deplacementCamGauche((49,0), game, False)

    while game.joueur.rect.x > infoObject[0]//2+10:
        deplacementCamDroite((infoObject[0]-49,0), game, False)


    while game.joueur.rect.y > infoObject[1]//2-10:
        deplacementCamBas((0,infoObject[1]-49), game, False)

    while game.joueur.rect.y < infoObject[1]//2+10:
        deplacementCamHaut((0,49), game, False)



def deplacementCamBas(mouse, game, bloquage, suiviePerso=False):
    global moveY, moveX
    x=infoObject[1]-mouse[1]
    y=f(x)
    if x < 50 or suiviePerso:  # Si souris en bas
        if not bloquage or (game.map[-1][0].Yoriginal+moveY>infoObject[1]-250):
            for i in range(len(game.map)):
                for j in range(len(game.map[0])):
                    game.map[i][j].decalerY(y)
            game.joueur.rect.y+=y
            if game.theBoss:
                game.theBoss.rect.y+=y
            moveY+=y
            for mob in game.groupMob:
                
                mob.rect.y+=y
            for projo in game.groupProjectile:
                projo.rect.y+=y
            for defense in game.groupDefense:
                defense.rect.y+=y
            for pos in game.listeDebug:
                pos[1]+=y
            for annimMort in game.groupMobMort:
                annimMort.posY+=y
                
def deplacementCamHaut(mouse, game, bloquage, suiviePerso=False):
    global moveY, moveX
    x = mouse[1]
    y = -f(x)
    if x < 50 or suiviePerso: #Si souris en haut
        if not bloquage or (game.map[0][-1].rect.y<100):
            for i in range(len(game.map)):
                for j in range(len(game.map[0])):
                    game.map[i][j].decalerY(y)
            game.joueur.rect.y+=y
            if game.theBoss:
                game.theBoss.rect.y+=y
            moveY+=y
            for mob in game.groupMob:
                mob.rect.y+=y
            for projo in game.groupProjectile:
                projo.rect.y+=y
            for defense in game.groupDefense:
                defense.rect.y+=y
            for pos in game.listeDebug:
                pos[1]+=y
            for annimMort in game.groupMobMort:
                annimMort.posY+=y
        
def deplacementCamGauche(mouse, game, bloquage, suiviePerso=False):
    global moveY, moveX
    x= mouse[0]
    y = -f(x)
    if x < 50 or suiviePerso:  # Si souris à gauche
        if not bloquage or (game.map[0][0].rect.x<100):
            for i in range(len(game.map)):
                for j in range(len(game.map[0])):
                    game.map[i][j].decalerX(y)
            game.joueur.rect.x+=y
            if game.theBoss:
                game.theBoss.rect.x+=y
            for mob in game.groupMob:
                mob.rect.x+=y
            moveX+=y
            for projo in game.groupProjectile:
                projo.rect.x+=y
            for defense in game.groupDefense:
                defense.rect.x+=y
            for pos in game.listeDebug:
                pos[0]+=y
            for annimMort in game.groupMobMort:
                annimMort.posX+=y
        
def deplacementCamDroite(mouse, game, bloquage, suiviePerso=False):
    global moveY, moveX
    x = infoObject[0]-mouse[0]
    y=f(x)


    if x < 50 or suiviePerso:  # Si souris à droite
        if not bloquage or (game.map[-1][-1].rect.x>infoObject[0]-400):
            for i in range(len(game.map)):
                for j in range(len(game.map[0])):
                    game.map[i][j].decalerX(y)
            game.joueur.rect.x+=y
            if game.theBoss:
                game.theBoss.rect.x+=y
            moveX+=y
            for mob in game.groupMob:
                mob.rect.x+=y
            for projo in game.groupProjectile:
                projo.rect.x+=y
            for defense in game.groupDefense:
                defense.rect.x+=y
            for pos in game.listeDebug:
                pos[0]+=y
            for annimMort in game.groupMobMort:
                annimMort.posX+=y
            
def f(x):  #fonction vitesse deplacement cam
    y  = round(x*0.04-10)
    if y>20:
        return 15
    return y


def pause(fenetre, game):
    global infoObject
    tailleEcran = infoObject[0], infoObject[1]
    diagonalEcran = math.sqrt(tailleEcran[0]**2 + tailleEcran[1]**2)
    pause=True
    scaleButton = 1/3 * tailleEcran[0], 1/9*tailleEcran[1]
    debutPause = pygame.time.get_ticks()
    clock = pygame.time.Clock()
    font = pygame.font.Font("data/menu/font.ttf", round(3/100*diagonalEcran))
    imBouton = pygame.transform.scale(pygame.image.load("data/menu/backButton.png").convert_alpha(), scaleButton)
    if game.langage == "fr":
        fermer = Button(imBouton, (tailleEcran[0]*1/2, tailleEcran[1]*1/3+55/100*tailleEcran[1]), "fermer", font, "white", "#999999")
        reprendre = Button(imBouton, (tailleEcran[0]*1/2, tailleEcran[1]*1/3), "reprendre", font, "white", "#999999")
        documentation = Button(imBouton, (tailleEcran[0]*1/2, tailleEcran[1]*1/3+20/100*tailleEcran[1]), "documentation", font, "white", "#999999")
        pause = Button(None, (tailleEcran[0]*1/2, tailleEcran[1]*1/3-20/100*tailleEcran[1]), "pause", font, "black", "#999999")
    else:
        fermer = Button(imBouton, (tailleEcran[0]*1/2, tailleEcran[1]*1/3+55/100*tailleEcran[1]), "close", font, "white", "#999999")
        reprendre = Button(imBouton, (tailleEcran[0]*1/2, tailleEcran[1]*1/3), "resume", font, "white", "#999999")
        documentation = Button(imBouton, (tailleEcran[0]*1/2, tailleEcran[1]*1/3+20/100*tailleEcran[1]), "documentation", font, "white", "#999999")
        pause = Button(None, (tailleEcran[0]*1/2, tailleEcran[1]*1/3-20/100*tailleEcran[1]), "break", font, "black", "#999999")
    librairie = False
    menu = Button(imBouton, (tailleEcran[0]*1/2, tailleEcran[1]*1/3+40/100*tailleEcran[1]), "menu", font, "white", "#999999")
    
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
            fenetrePygame.blit(librairieIMG,(infoObject[0]-librairieIMG.get_width()-(infoObject[0]-librairieIMG.get_width())/2,200))
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
    return pygame.font.Font("data/menu/Avenir.ttc", size)

def surEcran(entite, moveX, moveY, infoObject):
    return entite.rect.x>=0 and entite.rect.x<=infoObject[0] and entite.rect.y>=0 and entite.rect.y<=infoObject[1]


def gestionMob(game, fps):
    now = game.tempsJeu()
    for mob in game.groupMob:
        a=1
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
        
        elif (now-mob.last)>=mob.cooldown and mob.fini :
            recherchePossible=False
            if mob.aquatique: #les kraken
                if game.joueur.getTuile().type==3: 
                    recherchePossible=True
            elif mob.aerien:    #les dragons
                recherchePossible=True
            elif not game.joueur.getTuile().caseBloquante(): #tous les autres
                recherchePossible=True
                
            if recherchePossible:
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


def stat(game:Game): #specification du type game
    
    #multiplication par 6 pour mettre en minute
    productionWood = str(5*game.joueur.nbScierie*6)
    productionStone = str(4*game.joueur.nbMine*6)
    productionWater = str(3*game.joueur.nbMoulin*6)
    productionFood = str(4*game.joueur.nbElevage*6 + 1*game.joueur.nbChamps*6)
    recuperationEcolo = str(game.joueur.nbFrigo*0.5*6)
    nbAnnimauxMort = game.joueur.nbAnnimauxTue
    ennemieDegat = max(game.joueur.dictioDegatMob.items(), key=operator.itemgetter(1))[0]
    #game.tempsJeu() --> en mili sec /1000
    

    
    return productionWood, productionStone, productionWater, productionFood, recuperationEcolo, nbAnnimauxMort, ennemieDegat

