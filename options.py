from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import tkinter.font as font
import main_menu
import pygame
fenetreOptions = ""

checkVar1 = 1
checkVar2 = 0
music = True
modeHD = False


def init():
    global fenetreOptions, checkVar1, music
    fenetreOptions = Tk()
    screenScale = str(fenetreOptions.winfo_screenwidth())
    screenScale += "x"
    screenScale += str(fenetreOptions.winfo_screenheight())
    fenetreOptions.geometry(screenScale)
    # if music == True:
    # pygame.mixer.init()
    #mainTheme = pygame.mixer.music.load("data/Music/Options.mp3")
    # pygame.mixer.music.play(10)
    #checkVar1 = IntVar()
    return


def ok():
    # quand clique sur ok alors enregistrement et fermeture du menu
    global fenetreOptions, music
    fenetreOptions.destroy()
    fenetreOptions=""
    print("fermeture du menu option et enregistrement des modifications")
    main_menu.Main_Menu()
    return


def Renit():
    # fonction gérant le bouton rénitialisation
    global fenetreOptions
    print("suppresion des sauvegardes ?")
    if messagebox.askokcancel("ATTENTION : ", "En poursuivant l'entièreté de vos sauvegardes seront effacées. Cette action est irréversible. Voulez-vous vraiment continuer ? ") == True:
        print("Ok, suppresion des sauvegardes")
        fenetreOptions.destroy()
        main_menu.Main_Menu()
    else:
        print("Canceled")


def StopMusic():
    global checkVar1, music
    print(checkVar1)
    if checkVar1.get() == 0:
        pygame.mixer.init()
        #mainTheme = pygame.mixer.music.load("data/Music/Options.mp3")
        pygame.mixer.music.play(10)
        print("activation des musiques")
        music = True
    elif checkVar1.get() == 1:
        pygame.mixer.music.stop()
        print("stop musique")
        music = False
    return


def forceHD():
    # cette fonction permet de forcer le passage au mode HD (1920x1080) pour les écrans ayant une résolution trop élevé  2K, 4K.
    global modeHD
    modeHD = True
    print("Mode HD activate")
    return


def Menu_Options():
    global isActive, fenetreOptions, checkVar1, checkVar2
    init()
    fenetreOptions.update_idletasks()
    fenetreOptions.title("Options")  # titre
    #fenetre.attributes('-fullscreen', True)
    f= font.Font(size=50)

    #fenetreOptions.iconphoto(False, PhotoImage(file="data/logo/icon_Polgarok.png"))
    imageBGOptions = Image.open("data/menu/main_options_background.png")
    # redimentionne la taille de l'image en fonction de la taille de l'écran
    resize_imageBGOptions = imageBGOptions.resize(
        (fenetreOptions.winfo_screenwidth(), fenetreOptions.winfo_screenheight()))
    imgBGOptions = ImageTk.PhotoImage(
        resize_imageBGOptions)  # convertit PIL en tkinter
    # créer un label  pour afficher l'image
    arrireplanLabel = Label(fenetreOptions, image=imgBGOptions)
    arrireplanLabel.pack()
    arrireplanLabel.place(x=0, y=0)

    resetSave = Button(fenetreOptions, command=Renit, text= "Rénitialiser les sauvegardes")
    resetSave['font']=f
    resetSave.pack
    resetSave.place(anchor="nw", relx=0.02, rely=0.10)

    okButton = Button(fenetreOptions, command=ok, text= "Ok" )
    okButton['font'] = f
    okButton.pack
    okButton.place(anchor="nw", relx=0.02, rely=0.25)

    checkButtonMusic = Checkbutton(fenetreOptions, text="Musique", variable=checkVar1,
                                   onvalue=0, offvalue=1, justify=LEFT, width=25, command=StopMusic)
    checkButtonMusic.pack
    checkButtonMusic.place(anchor="nw", relx=0.02, rely=0.52)

    checkButtonHD = Checkbutton(fenetreOptions, text="Forçage du mode HD", variable=checkVar2,
                                onvalue=1, offvalue=0, justify=LEFT, width=25, command=forceHD)
    checkButtonHD.pack
    checkButtonHD.place(anchor="nw", relx=0.02, rely=0.55)

    fenetreOptions.columnconfigure(0, weight=1)
    fenetreOptions.mainloop()  # raffraichisement de la fenetre tkinter
