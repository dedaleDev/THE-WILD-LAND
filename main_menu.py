from tkinter import *
from turtle import st
from PIL import Image, ImageTk
import tkinter.font as font
import pygame
import options
import sys


fenetre = ""  # On crée une fenêtre, racine de l'interface Tk
startGame =False
load =True

def musicPlayerMainTheme():
    if options.music == True:
        pygame.mixer.init()
        mainTheme = pygame.mixer.music.load("data/Music/MainTheme.mp3")
        pygame.mixer.music.play(10)
    return

def option ():
    fenetre.destroy()
    options.Menu_Options()
def Quitter():
    global startGame, load
    startGame=False
    load = False
    fenetre.destroy()
    sys.exit()
    return
    # fenetre.destroy()
    # écran


def LaunchGame():
    global startGame
    startGame =True
    fenetre.destroy()


def tailleEcran(redimensionner=1, fenetre="", pleinEcran=False):
    # Cette fonction permet de redimmentioner une fenêtre TKINTER.
    #  Par défaut elle modifie  directement l'écran il faut lui dire que le paramétre redimensionner =0 pour quelle ne le fasse pas.
    # Il est OBLIGATOIRE de lui spécifier une fenetre  TKINTER à redimentionner.
    screenScale = str(fenetre.winfo_screenwidth())
    screenScale += "x"
    screenScale += str(fenetre.winfo_screenheight())
    print("taille d'écran détécté", screenScale)
    if redimensionner == 1:
        fenetre.geometry(screenScale)
        return(screenScale)
    else:
        return(screenScale)


def Main_Menu():
    global fenetre, startGame
    startGame = False
    # masque la fenêtre durant le chargement
    fenetre = Tk()
    fenetre.title("Mini-Jeu")  # titre
    # taille de l’interface utilisateur par défaut

    # lancement de l'audio
    # musicPlayerMainTheme()

    fenetre.configure(background="black")
    f = font.Font(size=80)
    tailleEcranUser = tailleEcran(fenetre=fenetre)  # redimentionne l'écran
    # sépare taille ecran dans un p-uplet
    tailleEcranUser = tailleEcranUser.split("x")
    print(tailleEcranUser)
    largeurE = tailleEcranUser[0]  # récupére taille largeur ecran
    hauteurE = tailleEcranUser[1]  # récupére taille hauteur ecran
    largeurE = int(largeurE)  # convertit en int
    hauteurE = int(hauteurE)  # convertit en int

    if options.modeHD == True:
        fenetre.geometry("1920x1280")
        largeurE = 1920  # convertit en int
        hauteurE = 1080  # convertit en int

    #fenetre.iconphoto(False, PhotoImage(file="data/logo/icon_Polgarok.png"))

    # importation image arrière plan
    imageBG = Image.open("data/menu/main_menu_background.png")
    # redimentionne la taille de l'image en fonction de la taille de l'écran
    resize_imageBG = imageBG.resize((largeurE, hauteurE))
    imgBG = ImageTk.PhotoImage(resize_imageBG)  # convertit PIL en tkinter
    # créer un label  pour afficher l'image
    arrireplanLabel = Label(fenetre, image=imgBG)
    arrireplanLabel.pack()
    # affiche l'image.
    arrireplanLabel.place(x=0, y=0)

    # button jouer :
    #imageButtonJouer = Image.open("data/Menu/button_Jouer.png")
    #imageButtonJouer = ImageTk.PhotoImage(imageButtonJouer)
    #image = imageButtonJouer
    buttonJouer = Button(fenetre, command=LaunchGame,
                         text="JOUER", relief=FLAT)
    buttonJouer['font'] = f
    buttonJouer.pack
    buttonJouer.place(anchor="nw", relx=0.02, rely=0.05)

    # button Options :
    #imageButtonOptions = Image.open("data/Menu/button_Options.png")
    #imageButtonOptions = ImageTk.PhotoImage(imageButtonOptions)
    buttonOptions = Button(
        fenetre, command=option,  text="OPTIONS", relief=FLAT)
    buttonOptions['font'] = f
    buttonOptions.pack()
    buttonOptions.place(anchor="nw", relx=0.02, rely=0.18)

    # button QUITTER :
    #imageButtonQuitter = Image.open("data/Menu/button_Quitter.png")
    #imageButtonQuitter = ImageTk.PhotoImage(imageButtonQuitter)
    buttonQuitter = Button(
        fenetre, command=Quitter, text="QUITTER", relief=FLAT)
    buttonQuitter['font'] = f
    buttonQuitter.pack()
    buttonQuitter.place(anchor="nw", relx=0.02, rely=0.32)

    # button reprendre  ce button se  charge si une ancienne sauvegarde à été déctécté dans Save.py. et il cache le button jouer

    # redimentionne la taille de l'image en fonction de la taille de l'écran
    resize_imageBG = imageBG.resize((largeurE, hauteurE))
    fenetre.mainloop()  # raffraichisement de la fenetre tkinter
