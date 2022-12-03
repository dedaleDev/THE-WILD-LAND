import os
from tkinter import *
import tkinter.font as tkFont
from tkinter import filedialog
import shutil
from PIL import ImageTk, Image  
import os
import math
#créer fenetre tkinter :
infoObject = [1920,1080]
tailleE =[]
tuile =""
fenetre=""
filename=""
listboxB =""
selectB=""
listboxV =""
selectV =""
global apercu, load

def importTuile():
    global tuile, fenetre,filename,tailleE,apercu, load, selectV, selectB
    print("début de l'importation")
    file =str(filedialog.askopenfilename(initialdir = "/",title = " Sélectionner le fichier ",filetypes = (("Image files","*.png"),("all files","*.*"))))
    print("déplacement du fichier...")
    path= os.path.dirname(__file__)
    path+="/data/tuiles/tuilesUsers"
    shutil.copy(file, path)
    os.rename(path+"/"+file,  str(selectB)+str(selectV)+".png")
    print("fichier renomé")
    file =  str(selectB)+str(selectV)+".png"
    file = file.split("/")
    print(path+"/"+file[-1])
    apercu = Image.open(path+"/"+file[-1])
    apercu = apercu.resize((tailleE[0]//10, tailleE[0]//10), Image.Resampling.LANCZOS)
    load =  ImageTk.PhotoImage(apercu)
    tuile.config(image =load)

def showSelectedBiome():
    global listboxB, selectB
    selected = listboxB.get(ACTIVE)
    print(selected)
    selectB.config(text =selected)

def showSelectedVariation():
    global listboxV, selectV
    selected = listboxV.get(ACTIVE)
    print(selected)
    selectV.config(text =selected)



def TuileEditor(infoObject):
    #menu tuile editor starting 
    #créer fenetre tkinter :
    global tuile,fenetre,tailleE, varB, selectB, listboxB, selectV, listboxV
    fenetre = Tk()
    fenetre.title("Tuile Editeur")
    tailleE =infoObject
    infoObject=str(infoObject[0])+"x"+str(infoObject[1])
    fenetre.geometry(infoObject)
    fenetre.resizable(width=False, height=False)
    fenetre.iconbitmap("data/logo/icon_WL.png")
    fenetre.config(background='#000000')
    diagonale = math.sqrt(tailleE[0]**2+tailleE[1]**2)
    tailleIMG =[int(tailleE[0]*0.4),int(tailleE[1]*0.35)]
    #police
    helv32 = tkFont.Font(family='Helvetica', size=int(diagonale*0.0139),weight='bold')  # big police
    helv24 = tkFont.Font(family='Helvetica', size=int(diagonale*0.010),weight='bold')  #moyenne  police
    helv14 = tkFont.Font(family='Helvetica', size=int(diagonale*0.006),weight='normal')  #petite police

    #images :    

    modeEmploiIMG = Image.open('data/menu/editorTuile/instruction.png')
    modeEmploiIMG = modeEmploiIMG.resize((int(tailleIMG[0]), int(tailleIMG[1])), Image.Resampling.LANCZOS)
    loadModeEmploiIMG =  ImageTk.PhotoImage(modeEmploiIMG)
    
    tuileIMG = Image.open('data/menu/editorTuile/tuile.png')
    tuileIMG = tuileIMG.resize((int(tailleIMG[0]*0.7), int(tailleIMG[1]*0.8)), Image.Resampling.LANCZOS)
    loadTuileIMG =  ImageTk.PhotoImage(tuileIMG)

    settingsIMG = Image.open('data/menu/editorTuile/settings.png')
    settingsIMG = settingsIMG.resize((int(tailleIMG[0]*0.6), int(tailleIMG[1]*1.9)), Image.Resampling.LANCZOS)
    loadSettingsIMG =  ImageTk.PhotoImage(settingsIMG)

    buttonImportIMG = Image.open('data/menu/editorTuile/import.png')
    buttonImportIMG = buttonImportIMG.resize((int(tailleIMG[0]*0.55), int(tailleIMG[1]*0.25)), Image.Resampling.LANCZOS)
    loadButtonImportIMG =  ImageTk.PhotoImage(buttonImportIMG)




    #widgets
    title = Label(fenetre, text="ÉDITEUR DE TUILE :", foreground="white", background = "black",font=helv32).place(x=tailleE[0]/2.4,y=tailleE[1]*0.02)
    modeEmploi = Label(fenetre, image = loadModeEmploiIMG,background="black").place(x=tailleE[0]*0.02,y=tailleE[1]*0.55)
    tuile = Label(fenetre, image = loadTuileIMG, background="black")
    tuile.place(x=tailleE[0]*0.09,y=tailleE[1]*0.2)
    settings = Label(fenetre, image = loadSettingsIMG, background="black").place(x=tailleE[0]*0.7,y=tailleE[1]*0.2)
    buttonImport = Button(fenetre,image=loadButtonImportIMG,borderwidth=0,relief='flat',highlightthickness = 0, bd = 0, command=importTuile).place(x=tailleE[0]*0.71,y=tailleE[1]*0.73)
    
    #biomes :
    langs = ['biome 1', 'biome 2','biome 3','biome 4', 'biome 5','biome 6', 'biome 7','biome 8','biome 9', 'biome 10']
    
    varB =Variable(value=langs)

    listboxB = Listbox(fenetre,listvariable=varB,height=3, width=int(tailleE[0]*0.012),selectmode=BROWSE,background="white",foreground="black")
    listboxB.place(x=tailleE[0]*0.82,y=tailleE[1]*0.32)

    scrollbar = Scrollbar(fenetre,orient=VERTICAL,command=listboxB.yview)
    listboxB['yscrollcommand'] = scrollbar.set


    selectB = Label(fenetre, text=str(listboxB.get(ANCHOR)), foreground="white", background = "black",font=helv24)
    selectB.place(x=tailleE[0]*0.73,y=tailleE[1]*0.35)
    buttonBApply = Button(fenetre,text = "Appliquer",borderwidth=0,relief='flat',highlightthickness = 0, bd = 0, command=showSelectedBiome)
    buttonBApply.place(x=tailleE[0]*0.82,y=tailleE[1]*0.395)

    addBiome = Button(fenetre,borderwidth=0,relief='flat', text="Nouvelle Biome",highlightthickness = 0, bd = 0, command=importTuile).place(x=tailleE[0]*0.87,y=tailleE[1]*0.395)

    print(listboxB.get(ACTIVE))
    #variations : 
    langs = ['variation 1 ', 'variation 2','variation 3','variation 4', 'variation 5','variation 6', 'variation 7','variation 8','variation 9', 'variation 10']
    
    variation =Variable(value=langs)

    listboxV = Listbox(fenetre,listvariable=variation,height=5,selectmode=BROWSE,background="white",foreground="black")
    listboxV.place(x=tailleE[0]*0.83,y=tailleE[1]*0.5)

    scrollbar = Scrollbar(fenetre,orient=VERTICAL,command=listboxV.yview)
    listboxV['yscrollcommand'] = scrollbar.set

    selectV = Label(fenetre, text=str(listboxV.get(ANCHOR)), foreground="white", background = "black",font=helv24)
    selectV.place(x=tailleE[0]*0.73,y=tailleE[1]*0.52)
    buttonVApply = Button(fenetre,text = "Appliquer", command=showSelectedVariation)
    buttonVApply.place(x=tailleE[0]*0.83,y=tailleE[1]*0.575)

    fenetre.mainloop()


    return

TuileEditor(infoObject)
