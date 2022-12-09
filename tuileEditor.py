import os
from tkinter import *
import tkinter.font as tkFont
from tkinter import filedialog
import shutil
from PIL import ImageTk, Image  
import os
import math
#créer fenetre tkinter :
infoObject = [1280,720]
tailleE =[]
tuile =""
fenetre=""
filename=""
listboxB =""
selectB=""
listboxV =""
selectV =""
selectedB,selectedV = "",""
biomes=["1 "] #liste des biomes
variations =["1 "] #liste des variations
NameNewBiome =""
varB =""
varV =""

def supprimerEspace(chaine:str):
    chaineSansEspace=""
    for char in chaine:
        if char!=" ":
            chaineSansEspace+=char
    return chaineSansEspace

def importTuile():
    global tuile, fenetre,filename,tailleE,apercu, load,selectedB,selectedV
    print("début de l'importation")
    file =str(filedialog.askopenfilename(initialdir = "/",title = " Sélectionner le fichier ",filetypes = (("Image files","*.png"),("all files","*.*"))))
    print("déplacement du fichier...")
    path= os.path.dirname(__file__)
    path+="/data/tuiles/tuilesUsers"
    shutil.copy(file, path)
    
    print("renomage du fichier...")
    file2= path+"/"+supprimerEspace(selectedB+"_"+selectedV)+".png"
    os.rename(path+"/"+file.split("/")[-1],file2)
    print("fichier renomé en : ",file2)
    loadTuile(file2)

def getPathofTuile():
    global selectedB,selectedV
    path= os.path.dirname(__file__)
    path+="/data/tuiles/tuilesUsers"
    path+="/"+supprimerEspace(selectedB+"_"+selectedV)+".png"
    return loadTuile(file2=path)

def loadTuile(file2:str):
    global tuile,tailleE,apercu, load
    if os.path.isfile(file2):
        print("fichier trouvé, chargement de l'aperçu...")
        apercu = Image.open(file2)
        apercu = apercu.resize((tailleE[0]//10, tailleE[0]//10), Image.Resampling.LANCZOS)
        load =  ImageTk.PhotoImage(apercu)
        tuile.config(image =load)

def showSelectedBiome():
    global listboxB, selectB,selectedB
    selected = listboxB.get(ACTIVE)
    selectedB= str(listboxB.get(ACTIVE))
    print(selectedB)
    selectB.config(text =selected)
    

def showSelectedVariation():
    global listboxV, selectV,selectedV
    selected = listboxV.get(ACTIVE)
    selectedV= str(listboxV.get(ACTIVE))
    print(selectedV)
    selectV.config(text =selected)
    getPathofTuile()

def newBiome():#creation des nouvelles biomes 
    res = str(NameNewBiome.get())
    if res =="" or res in biomes:
        print("erreur : nom de biome vide ou déjà crée")
        return
    else : 
        print("creation d'une nouvelle biome en cours :", res)
        biomes.append(res)
        varB.set(biomes)
        print("fin du traitement")

def newVariation():#creation des nouvelles variations 
    res = str(int(variations[-1])+1)
    print("creation d'une nouvelle biome en cours :", res)
    variations.append(res)
    varV.set(variations)
    print("fin du traitement")


def leftclick(event):
    showSelectedBiome()
    showSelectedVariation()

def key_press(event):
    if event.keysym=="Up" or event.keysym=="Down":
        print("touche touche fleche haut ou bas presse")
        showSelectedBiome()
        showSelectedVariation()

def TuileEditor(infoObject):
    #menu tuile editor starting 
    #créer fenetre tkinter :
    global tuile,fenetre,tailleE, selectB, listboxB, selectV, listboxV,NameNewBiome,biomes,variations,varB, varV
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

    fenetre.call("source", "ttkthemes/azure.tcl")
    fenetre.tk.call("set_theme", "light")
    
    #initialisation des variables spéciales :
    NameNewBiome = StringVar()
    selectB =StringVar()
    selectV =StringVar()

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
    settingsIMG = settingsIMG.resize((int(tailleIMG[0]*0.8), int(tailleIMG[1]*2.4)), Image.Resampling.LANCZOS)
    loadSettingsIMG =  ImageTk.PhotoImage(settingsIMG)


    buttonImportIMG = Image.open('data/menu/editorTuile/import.png')
    buttonImportIMG = buttonImportIMG.resize((int(tailleIMG[0]*0.55), int(tailleIMG[1]*0.25)), Image.Resampling.LANCZOS)
    loadButtonImportIMG =  ImageTk.PhotoImage(buttonImportIMG)





    #widgets
    title = Label(fenetre, text="ÉDITEUR DE TUILE :", foreground="white", background = "black",font=helv32).place(x=tailleE[0]/2.4,y=tailleE[1]*0.02)
    modeEmploi = Label(fenetre, image = loadModeEmploiIMG,background="black").place(x=tailleE[0]*0.02,y=tailleE[1]*0.55)
    tuile = Label(fenetre, image = loadTuileIMG, background="black")
    tuile.place(x=tailleE[0]*0.09,y=tailleE[1]*0.2)
    settings = Label(fenetre, image = loadSettingsIMG, background="black").place(x=tailleE[0]*0.67,y=tailleE[1]*0.1)
    buttonImport = Button(fenetre,image=loadButtonImportIMG,borderwidth=0,relief='flat',highlightthickness = 0, bd = 0, command=importTuile).place(x=tailleE[0]*0.71,y=tailleE[1]*0.73)


    #BIOMES :
    
    varB =Variable(value=biomes)

    listboxB = Listbox(fenetre,listvariable=varB,height=3, width=int(tailleE[0]*0.012),selectmode=BROWSE,background="white",foreground="black")
    listboxB.place(x=tailleE[0]*0.82,y=tailleE[1]*0.255)

    scrollbar = Scrollbar(fenetre,orient=VERTICAL,command=listboxB.yview)
    listboxB['yscrollcommand'] = scrollbar.set


    selectB = Label(fenetre, text=str(listboxB.get(ANCHOR)), foreground="white", background = "black",font=helv24)
    selectB.place(x=tailleE[0]*0.73,y=tailleE[1]*0.28)

    #new biome :
    textEntry = Entry(fenetre,textvariable=NameNewBiome,background="grey", width=15).place(x=tailleE[0]*0.7,y=tailleE[1]*0.32)
    addBiome = Button(fenetre, text="Nouvelle Biome", command=newBiome).place(x=tailleE[0]*0.82,y=tailleE[1]*0.32)

    print(listboxB.get(ACTIVE))
    #variations : 
    variations = ['1 ',"2","3"]
    
    varV =Variable(value=variations)

    listboxV = Listbox(fenetre,listvariable=varV,height=3,selectmode=BROWSE,background="white",foreground="black")
    listboxV.place(x=tailleE[0]*0.82,y=tailleE[1]*0.47)

    scrollbar = Scrollbar(fenetre,orient=VERTICAL,command=listboxV.yview)
    listboxV['yscrollcommand'] = scrollbar.set

    selectV = Label(fenetre, text=str(listboxV.get(ANCHOR)), foreground="white", background = "black",font=helv24)
    selectV.place(x=tailleE[0]*0.73,y=tailleE[1]*0.51)
    addVariation = Button(fenetre, text="Nouvelle variation", command=newVariation).place(x=tailleE[0]*0.82,y=tailleE[1]*0.575)
    fenetre.bind("<Button-1>", leftclick)
    fenetre.bind("<Up>", key_press)
    fenetre.bind("<Down>", key_press)
    fenetre.mainloop()


    return

TuileEditor(infoObject)
