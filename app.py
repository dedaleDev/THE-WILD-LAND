import re
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from mechanize import Browser
from numpy import var
import sv_ttk
import ast
import multiprocessing
import re
import sys
from urllib.parse import urlparse
from tkinter import messagebox
import webbrowser
import web_scanner
from infoBulle import infoBulle
import pyperclip
from tkinter import messagebox
import utils
import login
#variables globales
url = ""
treeLink = ""
treeVuln = ""
treeError = ""
root = ""
webScanner=None
logged = False
new_win = None
isScanning = False
statut = ""
statutVuln = ""
inputURL = ""
mqueue_crawl = multiprocessing.Queue()
mqueue_check_vuln = multiprocessing.Queue()
simplify = True
avancedScan = True
lienFoundLabel = ""

#filtres
filtrerScan_window=None
errors_window=None
filters  =[["XSS",True],["SQL",True],["SESSION",True],["LFI/RFI",True]]#nom/etat
settings_window=None

#code source : 
codeSource = None
codeSourceText = ""
varBrowser="Firefox"
settingsFirstStart = True

#vitesse
speedScanTEXT=""
speedScanVar=4
firstAlertSpeedScan = True

trashPhoto=""

#login : 
username_entry=""
password_entry=""
url_login_entry=""

def start():
    #cette fonction permet de lancer le scan
    print("starting scan")

def software():
    global root,url, treeLink, treeVuln, statut,inputURL,treeVuln,statutVuln,lienFoundLabel,avancedScan, simplify
    print("starting software")
    #cette fonction initialise le logiciel et permet le lancement des fonctions de security tools

    root = tk.Tk()# Création de la fenêtre principale
    sv_ttk.set_theme("dark")
    root.geometry('1240x720')
    root.title('Security Scan')
    imgIcon= Image.open('data/icon.png')
    imgIcon = ImageTk.PhotoImage(imgIcon)
    root.wm_iconphoto(False, imgIcon)
    #creation des variables : 
    url = tk.StringVar()
    
    simplify = tk.BooleanVar(value=True)
    avancedScan = tk.BooleanVar(value=False)
    # Création de widgets
    startScan = ttk.Button(root, text="start scan", style="Accent.TButton",command=btn_scan_click)#creation du bouton sde démarrage du scan
    infoBulle(startScan, "Démarre la recherche de lien. ATTENTION : optenez d'abord l'autorisations de l'administrateur du site avant de scanner celui-ci.")
    stopScan = ttk.Button(root, text="stop scan", style="Accent.TButton",command=btn_stop_click)#creation du bouton sde démarrage du scan

    logoScanIMG = Image.open('data/logo.png')
    logoScanIMG = ImageTk.PhotoImage(logoScanIMG)
    logoScan=tk.Label(root, image=logoScanIMG)

    inputURL = ttk.Entry(root, width=50,textvariable=url)#creation de la zone de saisie de l'URL
    infoBulle(inputURL, '''URL au format http(s)://[...]''')

    lienFoundLabel=ttk.Label(root, text="Lien(s) trouvé(s) :")
    vulnFoundLabel=ttk.Label(root, text="Vulnérabilité(s) trouvé(s) :")
    statut=ttk.Label(root, text="Scan non démarré")
    statutVuln=ttk.Label(root, text="Scan de vulnérabilité non démarré")

    warningLabel = ttk.Label(root,text="ATTENTION : DEMANDEZ L'AUTORISATION DE L'ADMINISTRATEUR DU SITE AVANT DE LE SCANNER" )

    errors_button = ttk.Button(root, text="Errors", command=show_errors)

    #affichage des liens dans un tableau (arbre) :
    scrollbarLink = ttk.Scrollbar()
    scrollbarLink.pack(side="right", fill="y")
    treeLink = ttk.Treeview(height=11,selectmode="extended",show=("tree"),yscrollcommand=scrollbarLink.set,)
    infoBulle(inputURL, "Clic droit pour rechercher des vulnérabilitées sur le(s) lien(s) sélectionné(s).")
    scrollbarLink.config(command=treeLink.yview)
    treeLink.column("#0", anchor="w", width=140)

    tree_link = []
    if tree_link != []:
        for item in tree_link:
            parent, iid, text, values = item
            treeLink.insert(parent=parent, index="end", iid=iid, text=text, values=values)
        treeLink.selection_set(1)

    treeLink.bind('<Button-3>', lambda e: popup1(e,1))
    treeLink.bind('<Button-2>', lambda e: popup1(e,1))
    #treeLink.bind('<Key-Control_L>a', sc.select_all)

    #affichage des vulnérabilitées  dans un tableau (arbre) :
    scrollbarVuln = ttk.Scrollbar()
    scrollbarVuln.pack(side="right", fill="y")
    treeVuln = ttk.Treeview(height=11,selectmode="browse",show=("tree",),yscrollcommand=scrollbarVuln.set)
    scrollbarVuln.config(command=treeVuln.yview)
    treeVuln.column("#0", anchor="w", width=140)

    tree_Vuln = []
    if tree_Vuln != []:
        for item in tree_Vuln:
            parent, iid, text, values = item
            treeVuln.insert(parent=parent, index="end", iid=iid, text=text, values=values)
        treeLink.selection_set(1)

    #settings : 
    # Création de l'image
    imageSettingsButton = Image.open("data/settings.png")
    imageSettingsButton2 = ImageTk.PhotoImage(imageSettingsButton)
    settings_button = ttk.Button(root, image=imageSettingsButton2, command=show_settings)
    
    imageSettingsButton = Image.open('data/settings.png')
    imageSettingsButton = ImageTk.PhotoImage(imageSettingsButton)
    settings_button=ttk.Button(root, image=imageSettingsButton, command=show_settings)

    # Placement des widgets en utilisant place
    startScan.place(x=840, y=20, width=150, height=50)
    stopScan.place(x=1000, y=20, width=150, height=50)
    inputURL.place(x=180, y=20, width=650, height=50)
    logoScan.place(x=20, y=-20)
    settings_button.place(x=1165, y=23)

    lienFoundLabel.place(x=85, y=115)
    vulnFoundLabel.place(x=85, y=515)

    errors_button.place(x=1115, y=685)

    statut.place(x=860, y=70)
    statutVuln.place(x=900, y=515)

    warningLabel.place(x=300,y=695)

    treeLink.place(relx=0.071, rely=0.20, relheight=0.5, relwidth=0.853)
    scrollbarLink.place(relx=0.924, rely=0.20, relheight=0.5, relwidth=0.026)
    treeVuln.place(relx=0.071, rely=0.75, relheight=0.2, relwidth=0.853)
    scrollbarVuln.place(relx=0.924, rely=0.75, relheight=0.2, relwidth=0.026)

    root.protocol("WM_DELETE_WINDOW", quit)
    loadSave()
    root.mainloop()#boucle principale de Tkinter
import json

def quit():
    print("Quitting...")
    # Enregistrement des paramètres lors de la fermeture du logiciel :
    global root, url, varBrowser, speedScanVar
    data = {
        "url": url.get() if url.get() else "",
        "browser": varBrowser.get() if varBrowser.get() else "Firefox",
        "filters": getFilters(True),
        "speed": speedScanVar if isinstance(speedScanVar, int) else speedScanVar.get(),
    }
    with open("caches/save.json", "w+") as fichier:
        json.dump(data, fichier)
    root.destroy()
    root = None
    return

def loadSave():
    # Initialisation des variables globales :
    global url, varBrowser, filters, speedScanVar
    valueBrowser = varBrowser
    varBrowser = tk.StringVar(value=str(varBrowser))
    varBrowser.set(valueBrowser)
    # Chargement des paramètres sauvegardés :
    try:
        with open("caches/save.json", "r") as fichier:
            try :
                data = json.load(fichier)
            except :
                data =None
                pass
            if not data or data == None:
                return
            url.set(data["url"])
            varBrowser.set(data["browser"])
            for i, filter in enumerate(data["filters"]):
                if i >= len(filters):
                    break
                filters[i][1] = utils.convertToBool(filter[1])
            speedScanVar = int(data["speed"]) if isinstance(data["speed"], int) else tk.IntVar(value=data["speed"])
            print("Restauration du point de sauvegarde", url.get(), varBrowser.get(), filters)
    except Exception as e:
        print("Erreur lors de la lecture du fichier de sauvegarde :", e)
    return


def renit():
    global root
    settings_window.attributes("-topmost", False)
    validation =messagebox.askokcancel("Attention : ","La rénitialisation rétablira les réglages par défaut de Security Scan. Cette action est irréversible ! Voulez-vous vraiment continuer ?")
    settings_window.attributes("-topmost", True)
    if validation :
        with open("caches/save.txt","w+") as fichier: 
            fichier.seek(0)
            fichier.truncate()
        on_closingError()
        on_closingSettings()
        root.destroy()
    return
    

def btn_scan_click():
    global root, isScanning,webScanner,logged,statut,inputURL,simplify,avancedScan,treeError, varBrowser

    target = url.get()
    #suppression d'eventuel espace en début et fin d'url : 
    target =target.replace(" ", "")
    regex = re.compile(
        r'^(?:http|ftp)s?://'  # http(s):// ou  ftp(s)
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domaine...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...ou ip
        r'(?::\d+)?'  # port optionnel
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

    if not re.match(regex, target):
        inputURL.state(["invalid"])
        messagebox.showerror("Erreur d'URL", "L'URL saisie n'est pas valide !")
        return

    if not target.endswith("/") and not target.endswith(".php") and not target.endswith(".html"):
        target = target + "/"

    if webScanner is None:  # si l'objet webScanner n'existe pas encore, on l'instancie ici
        webScanner = web_scanner.WebScanner(target,avancedScan=avancedScan,browser=varBrowser.get())

    elif urlparse(webScanner.url).netloc not in target:  # si on change de domaine, créé un nouveau scanner
        webScanner.stopped = True
        webScanner = web_scanner.WebScanner(target,avancedScan=avancedScan,browser=varBrowser.get())

    elif logged:  # si une session de login existe, on s'assure d'avoir bien l'URL à tester et non celle du login
        webScanner.url = target

    if isScanning:
        rep = messagebox.askquestion("Scan en cours", "Un scan est déjà en cours, souhaitez-vous l'arrêter ?")
        if rep == "yes":
            webScanner.stopped = True
            statut['text'] = "Scan arrêté."
            isScanning = False
            sys.stdout.flush()
            return

    webScanner.stopped = False
    webScanner.link_list=[]
    for child in treeLink.get_children():
        treeLink.delete(child)
        
    lienFoundLabel['text'] = "Liens trouvés : " + str(len(webScanner.getLinkList())+1)
    statut['text'] = "Scan en cours..."
    inputURL.state(["!invalid"])
    webScanner.crawl(mqueue_crawl,simplify=simplify.get())
    isScanning = True
    root.after(1000,process_queue_crawl)

first=True
x=0
def process_queue_crawl():
    global isScanning, webScanner, root,mqueue_crawl,mqueue_check_vuln,treeLink,lienFoundLabel,first,x

    if first :
        x=0
    try:
        msg = mqueue_crawl.get(0)#recupere le premier lien de la queue
        while msg != "END":  # récupère des lien d'arrière-plan jusqu'au lien de fin
            treeLink.insert("",x,text=msg, values=msg)#parent, index, id, text, values
            root.update()
            x+=1
            msg = mqueue_crawl.get(0)#recupere le prochain lien de la queue
        if msg == "END":
            statut["text"] = "Scan terminé !"
            first = True
            isScanning = False
            webScanner.stopped = True
            lienFoundLabel['text'] = "Liens trouvés : " + str(len(webScanner.getLinkList()))
    except Exception as e:  # passe les exceptions sous silence (notamment la queue vide)
        root.after(1000,process_queue_crawl)#relance la fonction après 500ms



def btn_stop_click():
    # Arrête le scan
    global webScanner, isScanning, root, statut, lienFoundLabel
    if webScanner is not None:
        webScanner.stopped = True
        statut['text'] = "Scan arrêté."
        lienFoundLabel['text'] = "Liens trouvés : " + str(len(webScanner.getLinkList()))
    isScanning = False
    


def process_queue_check_vuln():
    global isScanning, webScanner, treeVuln, root,statutVuln, avancedScan
    try:
        x=0
        msg = mqueue_check_vuln.get(0)
        while msg != "END":
            treeVuln.insert("",x,text=msg, values=msg)#parent, index, id, text, values
            root.update()
            msg = mqueue_check_vuln.get(0)#recupere le prochain lien de la queue
            x+=1
            if x>=len(webScanner.analyseLink):
                print("all links have been browsed stop scanning")
                mqueue_check_vuln.put("END")
        if msg == "END":
            statutVuln["text"] = "Vérification de vulnérabilités terminée"
            isScanning = False
            
            webScanner.stopped = True
    except Exception as e:
        root.after(process_queue_check_vuln)#relance la fonction après 1 seconde de délai
        
def btn_check_vuln():
    global root, webScanner,statutVuln,treeLink,treeVuln,treeError,codeSource, filters
    webScanner.error =[]
    selectedItem = treeLink.selection()
    selectedLinks = []
    try: 
        for i in range(len(filters)):
            filters[i][1]=filters[i][0].get()
    except:
        pass
    for item in selectedItem:
        selectedLinks.append(treeLink.item(item)['text'])
    statutVuln['text'] = "Recherche de vulnérabilités en cours..."
    webScanner.check_vuln(link_list=selectedLinks)
    statutVuln['text'] = "Recherche de vulnérabilités terminé !"

def updateTreeVuln():
    global treeVuln
    i=len(treeVuln.get_children())
    for vuln in webScanner.vulnFound:
        if vuln and vuln != "-values":
            treeVuln.insert(parent="", index=i, iid=i, text=vuln, values=vuln)
            i+=1


def updateStatut(scanStatut):
    global statut, isScanning, statutVuln
    statutVuln['text'] =str(scanStatut)
    root.update()

def copyLink():
    global treeLink
    selectedItem = treeLink.selection()
    selectedLinks = ""
    for item in selectedItem:
        selectedLinks+=" "+ str(treeLink.item(item)['text'])
    pyperclip.copy(str(selectedLinks))
    print("Copied link : "+selectedLinks)

def copyError():
    global treeError
    selectedItem = treeError.selection()
    selectedErrors = ""
    for item in selectedItem:
        selectedErrors+=" "+ str(treeError.item(item)['text'])
    pyperclip.copy(str(selectedErrors))
    print("Error copied : "+selectedErrors)

def btn_help_click():
    webbrowser.open("https://github.com/DedaleStudio/SecurityScan")

def popup1(event, *args, **kwargs):
    Popupmenu = tk.Menu(root, tearoff=0)
    Popupmenu.configure(activebackground="black")
    Popupmenu.add_command(
            command=btn_check_vuln,
            label="Chercher les vulnérabilités")
    Popupmenu.add_command(
            command=copyLink,
            label="Copier")
    Popupmenu.post(event.x_root, event.y_root)
    
def popup2(event, *args, **kwargs):
    Popupmenu = tk.Menu(root, tearoff=0)
    Popupmenu.configure(activebackground="black")
    Popupmenu.add_command(
            command=copyError,
            label="Copier")
    Popupmenu.post(event.x_root, event.y_root)

def show_errors():
    global webScanner,treeError,errors_window, trashPhoto
    if errors_window :
        errors_window.lift()
    else :
        errors_window = tk.Toplevel()
        errors_window.title("Erreurs")
        errors_window.geometry("500x300")
        imgIcon= Image.open('data/icon.png')
        imgIcon = ImageTk.PhotoImage(imgIcon)
        errors_window.wm_iconphoto(False, imgIcon)

        trashIMG = Image.open('data/trash.png')
        trashPhoto = ImageTk.PhotoImage(trashIMG)
        trashButton=ttk.Button(errors_window, image=trashPhoto, command=deleteError)
        #affichage des erreur  dans un arbre :
        treeError = ttk.Treeview(errors_window,height=10,selectmode="browse",show=("tree",))
        treeError.column("#0", anchor="w", width=160)
        if webScanner !=None:
            if webScanner.error !=[]:
                tree_Error = webScanner.error
            else : 
                tree_Error = ["Hum, tout va bien..."]
        else :
            tree_Error = ["Hum, tout va bien..."]
        if tree_Error != []:
            if len(tree_Error) > 10:
                while len(tree_Error) > 10:
                    tree_Error.pop(0)
            if len(tree_Error) >=2 and "Hum, tout va bien..." in tree_Error:
                tree_Error.pop(0)
            x=1
            for error in tree_Error:
                treeError.insert(parent="", index=x, iid=x, text=error)
                x+=1
                treeError.selection_set(1)
        treeError.place(relx=0.037, rely=0.10, relheight=0.855, relwidth=0.93)
        trashButton.place(relx=0, rely=0)

        treeError.bind('<Button-2>', lambda e: popup2(e,1))
        errors_window.protocol("WM_DELETE_WINDOW", on_closingError)

def deleteError():
    #delete la premiere erreur de l'abre error: 
    global treeError,webScanner
    treeError.delete(treeError.get_children()[0])
    if treeError.get_children() == ():
        treeError.insert(parent="", index=1, iid=1, text="Hum, tout va bien...")


def on_closingError():
    #Fermetures des fenetres
    global errors_window
    if errors_window != None:
        errors_window.destroy()
        errors_window = None

def on_closingSettings():

    global settings_window,codeSourceText,codeSource,varBrowser
    settings_window.grab_release()
    if settings_window != "":
        text = codeSource.get("1.0", tk.END)
        codeSourceText = str(text)
        settings_window.destroy()
        settings_window = None


#SETTINGS : 

def show_settings():
    global settings_window,settingsFirstStart,simplify,avancedScan,codeSource,codeSourceText,varBrowser,filters,speedScanTEXT,speedScanVar
    if settings_window :
        settings_window.lift()
    else :
        settings_window = tk.Toplevel()
        settings_window.title("Paramètres")
        settings_window.geometry("1240x720")
        imgIcon= Image.open('data/icon.png')
        imgIcon = ImageTk.PhotoImage(imgIcon)
        settings_window.attributes("-topmost", True)

        #creation des widgets
        crawlerTEXT=ttk.Label(settings_window,text="Crawler :")
        simplifyCrawl = ttk.Checkbutton(settings_window, text="Analyser uniquement les liens utiles", variable=simplify, command=updateSimplifyScan)

        scanTEXT=ttk.Label(settings_window,text="Analyse :")
        avancedScanButton = ttk.Checkbutton(settings_window, text="Analyse avancé (long)", variable=avancedScan, command=updateAvancedScan)
        
        browserSetingsTEXT = ttk.Label(settings_window,text="Navigateur :")
        browser= ["Firefox","Chrome","Safari","Edge"]
        BrowserRadioButton=[]
        for i in range(len(browser)):
            BrowserRadioButton.append(ttk.Radiobutton(settings_window, variable=varBrowser, text=browser[i], value=browser[i],command=restart_alert))
            

        sourceCodeTEXT=ttk.Label(settings_window,text="Source code :")
        infoBulle(sourceCodeTEXT, '''Il arrive rarement qu'en raison de certains modules anti-robot, le code source de certains sites puisse ne pas être correctement récupéré, il est donc possible de le copier ici pour l'analyser manuellement. Le code source doit être au format HTML.''')
        text_frame = ttk.Frame(settings_window, borderwidth=2, relief="groove")
        codeSource = tk.Text(text_frame, wrap="word")
        if codeSourceText != "":
            print("codeSourceText : ",codeSourceText)
            codeSource.insert("1.0", codeSourceText)
        
        #filters :
        filtersCheckButton=[]
        for i in range(len(filters)):
            if settingsFirstStart:
                value = filters[i][1]
                filters[i][1] = tk.BooleanVar(value=value)
                filters[i][1].set(value)
            filtersCheckButton.append(ttk.Checkbutton(settings_window, text=filters[i][0], variable=filters[i][1], command=getFilters))
        
        #renit : 
        buttonRenit = ttk.Button(settings_window,text="Rénitialisation",command=renit)
        # vitesse de scan :
        if type(speedScanVar) == int:
            speedScanVar = tk.IntVar(value=speedScanVar)
        speedScan = ttk.Scale(settings_window, from_=1, to=30, orient=tk.HORIZONTAL,variable=speedScanVar, command=updateSpeedScan)
        speedScanTEXT = ttk.Label(settings_window,text="Vitesse : "+str(speedScanVar.get()))
        infoBulle(speedScanTEXT, '''Augmentez le nombre de lien testé simultanément = plus de vitesse. Attention consomme plus de ressources.''')
        
        #Login:
        loginTEXT = ttk.Label(settings_window,text="Connection :")
        setCookiesSession = ttk.Button(settings_window, text="Cookies", command=login.showCookiesSettings)
        infoBulle(speedScanTEXT, '''Deffinissez un cookies de session afin d'avoir accès à certains espaces réservé au membre connecté de votre site web.''')
        #placement des widgets
        crawlerTEXT.place(x=20,y=20)
        simplifyCrawl.place(x=40, y=40)

        scanTEXT.place(x=20,y=120)
        avancedScanButton.place(x=40, y=140)

        sourceCodeTEXT.place(x=800,y=20)
        text_frame.place(x=800, y=60, width=400, height=600)
        codeSource.pack(expand=True, fill="both")

        speedScanTEXT.place(x=40,y=300)
        speedScan.place(x=120,y=300)

        
        for i in range (len(browser)):
            BrowserRadioButton[i].place(x=350,y=50+(i*30))
        browserSetingsTEXT.place(x=325,y=20)
        for i in range (len(filters)):
            filtersCheckButton[i].place(x=40,y=170+(i*30))
        
        buttonRenit.place(x=10,y=680)
        loginTEXT.place(x=325, y=180)
        setCookiesSession.place(x=350, y=210)


        settings_window.wm_iconphoto(False, imgIcon)
        settingsFirstStart = False
        settings_window.protocol("WM_DELETE_WINDOW", on_closingSettings)

def getFilters(returned=False):
    global filters
    try : 
        newliste = []
        for i in range(len(filters)):
            newliste.append([filters[i][0],filters[i][1].get()])
        if returned:
            return newliste
        else:
            print ("updating filter : ",newliste)
    except:
        return filters

def updateSimplifyScan():
    global simplify
    if simplify.get():
        simplify.set(True)
    else:
        simplify.set(False)

def updateAvancedScan():
    #alerter l'utilisateur que l'analyse avancé est longue
    messagebox.showinfo("Attention : ", "L'analyse avancée est longue et n'est recommandée que si vous avez besoin d'une forte précision de scan. L'analyse avancée n'est pas disponible pour l'ensemble des vulnérabilités (voir readme). Un scan normal sera effectué dans ces cas-là.")
    global avancedScan
    if avancedScan.get():
        avancedScan.set(True)
    else:
        avancedScan.set(False)

def getCodeSource():
    global codeSource
    if codeSource != None and codeSource != "":
        try : 
            codeSource= codeSource.get()
            return codeSource
        except : 
            return ""
    else:
        return ""

def restart_alert():
    global settings_window
    settings_window.attributes("-topmost", False)
    messagebox.showinfo("Un redémarrage est nécessaire : ","Pour appliquer les modifications Security Scan va à présent s'eteindre, nous vous invitons à le redémarrer par la suite.")
    on_closingError()
    on_closingSettings()
    quit()

def getSpeedScan():
    #permets de récupérer la vitesse de scan de vulnérailité
    global speedScanVar
    if type(speedScanVar) != int:
        return speedScanVar.get()
    else:
        return speedScanVar

def updateSpeedScan(event):
    global speedScanVar, speedScanTEXT,firstAlertSpeedScan, settings_window
    speedScanTEXT.config(text="Vitesse :"+str(speedScanVar.get()))
    if firstAlertSpeedScan:
        if speedScanVar.get() >= 10:
            settings_window.attributes("-topmost", False)
            firstAlertSpeedScan = False
            messagebox.showwarning("Attention : ", "Au delà de 10, la vitesse de scan bien que plus élevé peut causer des problèmes de performance très élevée voir extrême. Nous vous conseillons de ne pas dépasser 10 sauf si votre matériel vous le permet. Vous risquez aussi d'être bloqué car vous enverrez trop de requête simultanée. Enfin, il est possible en fonction du type de scan que l'augmentation de la vitesse de scan ne soit pas significative ou n'implique pas de gain de vitesse.")
            settings_window.attributes("-topmost", True)
    

