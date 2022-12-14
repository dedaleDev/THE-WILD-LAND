import os
from tkinter import *
import tkinter.font as tkFont
from tkinter import filedialog
import shutil
from PIL import ImageTk, Image  
import os
import math

def supprimerEspace(chaine:str):
    chaineSansEspace=""
    for char in chaine:
        if char!=" ":
            chaineSansEspace+=char
    return chaineSansEspace

class Biome:
    #classe qui permet de créer un biome et de lui ajouter des variations
    def __init__(self, name:str, variations=[], probabilitée=5,first=0):
        #ATTENTION LE PARAMETRE first NE JAMAIS ETRE INITIALISE QU'UNE SEULE FOIS 
        self.name = supprimerEspace(name)
        self.variations = [1]
        self.selected = False
        self.selectedV=1
        self.imVariations =[False]
        self.probabilitée =probabilitée
        if first == 1:
            self.selected =True

    def addVariation(self, variation):
        self.variations.append(variation)
        self.imVariations.append(False)

    def setImageVariation(self,variation:int, statut:bool):
        self.imVariations[variation] = statut

    def probability(self, value):
        self.probabilitée = value
    def getName(self):
        return self.name
    def getVariations(self):
        #return variations, variation actuelle, liste des variations disposant d'une image
        return self.variations, self.selectedV,self.imVariations
    def getSelected(self):
        return self.selected

#créer fenetre tkinter :
infoObject = [1920,1080]
tailleE =[]
fenetre=""
filename=""
listboxB =""
listboxV =""
selectV =""
biomes = [Biome("biome 1",first=1)]
NameNewBiome =""
varB =""
varV =""
selectV =""
selectB=""
tuile =""






def importTuile():
    global biomes
    print("importation...")
    file =str(filedialog.askopenfilename(initialdir = "/",title = " Sélectionner le fichier ",filetypes = (("Image files","*.png"),("all files","*.*"))))
    path= os.path.dirname(__file__)
    path+="/data/tuiles/tuilesUsers"
    shutil.copy(file, path)
    trouve =False
    for i in range (len(biomes)):
        if biomes[i].getSelected()==True:
            trouve = True
            selectedV2 = str(biomes[i].getVariations()[1])
            selectedB2 = str(biomes[i].getName())
            biomes[i].setImageVariation(biomes[i].getVariations()[1]-1, True)
    if trouve == False : 
        print("erreur : aucun biome selectionné")
        return False
    file2= path+"/"+supprimerEspace(selectedB2+"_"+selectedV2+".png")
    os.rename(path+"/"+file.split("/")[-1],file2)
    loadTuile(file2)

def loadTuile(file2:str):
    global tuile, apercu,load #global load = obligatoire complétement farfelu
    tailleIMG = [int(tailleE[0]*0.4),int(tailleE[1]*0.35)]
    if os.path.isfile(file2):
        apercu =Image.open(file2)
        apercu = apercu.resize((int(tailleIMG[0]*0.7), int(tailleIMG[1]*0.8)), Image.Resampling.LANCZOS)
        load = ImageTk.PhotoImage(apercu)
        tuile.config(image =load)

def getPathofTuile(selectedB:str, selectedV:str):
    path= os.path.dirname(__file__)
    path+="/data/tuiles/tuilesUsers"
    path+="/"+supprimerEspace(selectedB+"_"+selectedV)+".png"
    return loadTuile(file2=path)


def showSelectedBiome(biomes):
    selectedB= str((listboxB.get(ACTIVE)))

    for i in range (len(biomes)):
        if biomes[i].getName() == selectedB:
            biomes[i].selected = True
            selectB.config(text =selectedB)
            path = getPathofTuile(str(selectedB), str(biomes[i].getVariations()[1]))
            selectV.config(text =1)
            biomes[i].selectedV = 1
        else :
            biomes[i].selected = False
    

def showSelectedVariation(biomes):
    global varV
    selectedV= int(listboxV.get(ACTIVE))
    trouve = False
    for i in range (len(biomes)):
        if biomes[i].getSelected() == True:
            #print("name",biomes[i].getName(),"actuel :",biomes[i].getSelected(),"selectionné :",selectedV, "liste : ",biomes[i].getVariations()[0])
            variations = biomes[i].getVariations()[0] 
            if selectedV in variations:
                selectV.config(text =selectedV)
                biomes[i].selectedV = selectedV
                varV.set(biomes[i].getVariations()[0])
                if biomes[i].getVariations()[2][selectedV-1] == False:
                    path = loadTuile('data/menu/editorTuile/tuile.png')
                    return 
                else : 
                    getPathofTuile(str(biomes[i].getName()),str(selectedV))
                    return 
    print("error, critical problem unknow  in showSelectedVariation ")
    return False

def newBiome():#creation d'une nouvelles biomes 
    global biomes, NameNewBiome, varB
    res = str(NameNewBiome.get())
    if res =="" or res in biomes:
        print("erreur : nom de biome vide ou déjà crée")
        return
    else : 
        print("creation d'une nouvelle biome  :", res)
        biomes.append(Biome(res))
        biomesWritable=[]
        for biome in biomes:
            biomesWritable.append(biome.getName())
        varB.set(biomesWritable)

def newVariation():#creation d'une nouvelle variation
    global biomes
    print("creation d'une nouvelle variation...")
    for biome in biomes:
        if biome.getSelected() == True:
            res = int(biome.getVariations()[0][-1])+1
            biome.addVariation(res)
            varV.set(biome.getVariations()[0])
            return True
    print("ERREUR inconnu lors de la création d'une nouvelle variation")
    return False
    


def leftclick(event):#permet la selection des biomes et des variations via un simple click souris
    showSelectedBiome(biomes)
    showSelectedVariation(biomes)

def key_press(event):#prermet d'utiliser les fleches du clavier pour naviguer dans les listbox
    if event.keysym=="Up" or event.keysym=="Down":
        showSelectedBiome(biomes)
        showSelectedVariation(biomes)

def TuileEditor(infoObject):
    #menu tuile editor starting 
    #créer fenetre tkinter :
    global tuile,fenetre,tailleE, listboxB, listboxV,NameNewBiome,biomes,varB, varV,selectB,selectV
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
    
    varB =Variable(value=biomes[0].getName())

    listboxB = Listbox(fenetre,listvariable=varB,height=3, width=int(tailleE[0]*0.012),selectmode=BROWSE,background="white",foreground="black")
    listboxB.place(x=tailleE[0]*0.82,y=tailleE[1]*0.255)

    scrollbar = Scrollbar(fenetre,orient=VERTICAL,command=listboxB.yview)
    listboxB['yscrollcommand'] = scrollbar.set


    selectB = Label(fenetre, text=str(listboxB.get(ANCHOR)), foreground="white", background = "black",font=helv24)
    selectB.place(x=tailleE[0]*0.73,y=tailleE[1]*0.28)

    #new biome :
    textEntry = Entry(fenetre,textvariable=NameNewBiome,background="grey", width=15).place(x=tailleE[0]*0.7,y=tailleE[1]*0.32)
    addBiome = Button(fenetre, text="Nouvelle Biome", command=newBiome).place(x=tailleE[0]*0.82,y=tailleE[1]*0.32)

    #variations : 
    variations = ['1']
    
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
