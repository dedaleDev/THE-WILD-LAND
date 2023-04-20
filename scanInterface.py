import re
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
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
speed = 1000
scaleSpeed = ""
speedLabel = ""
lienFoundLabel = ""

filtrerScan_window=None
errors_window=None
filters  =[["SQL",1],["XSS",1],["Session",1],["LFI/RFI",1]]#nom/etat
settings_window=None
def start():
    #cette fonction permet de lancer le scan
    print("starting scan")

def software():
    global root,url, treeLink, treeVuln, statut,inputURL,treeVuln,statutVuln,speed,scaleSpeed,speedLabel,lienFoundLabel,avancedScan, simplify
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
    avancedScan = tk.BooleanVar(value=True)
    avancedScan =False
    # Création de widgets
    startScan = ttk.Button(root, text="start scan", style="Accent.TButton",command=btn_scan_click)#creation du bouton sde démarrage du scan
    infoBulle(startScan, "Démarre la recherche de lien. ATTENTION : optenez d'abord l'autorisations de l'administrateur du site avant de scanner celui-ci.")
    stopScan = ttk.Button(root, text="stop scan", style="Accent.TButton",command=btn_stop_click)#creation du bouton sde démarrage du scan

    scanAvanceButton = ttk.Checkbutton(root, text="scan avancé (long)", style="Accent.TCheckbutton",variable=avancedScan,command=updateAvancedScan)#creation du bouton sde démarrage du scan
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

    scaleSpeed = ttk.Scale(root,from_=2000, to=1, value="1000",orient="horizontal",command=updateSpeed)
    infoBulle(scaleSpeed, "attente entre les requêtes")
    speedLabel = tk.Label(root, text="délai d'attente (1s) :")

    errors_button = ttk.Button(root, text="Errors", command=show_errors)
    filter_button = ttk.Button(root, text="Filter", command=set_filter)

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
    scanAvanceButton.place(x=260, y=510)

    lienFoundLabel.place(x=85, y=115)
    vulnFoundLabel.place(x=85, y=515)

    errors_button.place(x=1170, y=685)
    filter_button.place(x=1100, y=685)

    statut.place(x=860, y=70)
    statutVuln.place(x=900, y=515)

    warningLabel.place(x=300,y=695)

    treeLink.place(relx=0.071, rely=0.20, relheight=0.5, relwidth=0.853)
    scrollbarLink.place(relx=0.924, rely=0.20, relheight=0.5, relwidth=0.026)
    treeVuln.place(relx=0.071, rely=0.75, relheight=0.2, relwidth=0.853)
    scrollbarVuln.place(relx=0.924, rely=0.75, relheight=0.2, relwidth=0.026)

    scaleSpeed.place(x=992, y=105, width=150, height=50)
    speedLabel.place(x=800, y=102, width=150, height=50)

    root.mainloop()#boucle principale de Tkinter




def btn_scan_click():
    global root, isScanning,webScanner,logged,statut,inputURL,simplify,speed,avancedScan,treeError

    target = url.get()
    
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
        webScanner = web_scanner.WebScanner(target,avancedScan=avancedScan)

    elif urlparse(webScanner.url).netloc not in target:  # si on change de domaine, créé un nouveau scanner
        webScanner.stopped = True
        webScanner = web_scanner.WebScanner(target,avancedScan=avancedScan)

    elif logged:  # si une session de login existe, on s'assure d'avoir bien l'URL à tester et non celle du login
        webScanner.url = target

    if isScanning:
        rep = messagebox.askquestion("Scan en cours", "Un scan est déjà en cours, souhaitez-vous l'arrêter ?")
        if rep == "yes":
            webScanner.stopped = True
            statut['text'] = "Scan arrêté."
            isscanning = False
            sys.stdout.flush()
            return

    webScanner.stopped = False
    webScanner.link_list=[]
    for child in treeLink.get_children():
        treeLink.delete(child)
        
    lienFoundLabel['text'] = "Liens trouvés : " + str(len(webScanner.getLinkList()))
    statut['text'] = "Scan en cours..."
    inputURL.state(["!invalid"])
    webScanner.crawl(mqueue_crawl,simplify=simplify.get())
    isScanning = True
    root.after(speed, process_queue_crawl)

first=True
x=0
def process_queue_crawl():
    global isScanning, webScanner, root,mqueue_crawl,mqueue_check_vuln,treeLink,speed,lienFoundLabel,first,x

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
        root.after(speed, process_queue_crawl)#relance la fonction après 500ms




def updateAvancedScan():
    global avancedScan,webScanner
    if avancedScan:
        avancedScan=False
        if webScanner is not None:
            webScanner.avancedScan=False
        return
    avancedScan=True
    if webScanner is not None:
            webScanner.avancedScan=True


def btn_stop_click():
    # Arrête le scan
    global webScanner, isScanning, root, statut, lienFoundLabel
    if webScanner is not None:
        webScanner.stopped = True
        statut['text'] = "Scan arrêté."
        lienFoundLabel['text'] = "Liens trouvés : " + str(len(webScanner.getLinkList()))
    isScanning = False
    


def process_queue_check_vuln():
    global isScanning, webScanner, treeVuln, root,statutVuln, speed, avancedScan
    try:
        x=0
        print("process scan vuln x = "+x)
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
        root.after(speed, process_queue_check_vuln)#relance la fonction après 1 seconde de délai


def updateSpeed(event):
    global speed, scaleSpeed,speedLabel
    speed = int(scaleSpeed.get())
    speedLabel['text'] = "délai d'attente : "+ str(speed) + "ms"



def login_callback():
    global webScanner, new_win, logged
    login_info = new_win.nametowidget("entry_login").get()
    login_url = new_win.nametowidget("entry_url").get()
    if webScanner is None:
        webScanner = web_scanner.WebScanner(login_url)

    if webScanner.get_login_session(ast.literal_eval(login_info), login_url) is not None:
        messagebox.showinfo("Login réussi !", "Le scanner est connecté.")
        logged = True
        new_win.destroy()
    else:
        messagebox.showerror("Login non réussi !", "Erreur de connexion, vérifiez les informations.")
        logged = False


def fill_login_info():
    global new_win
    new_win = tk.Toplevel(root)  # créé une nouvelle fenêtre à la volée
    new_win.geometry("500x200")

    lbl = tk.Label(new_win, text="Données de login (ex: {\"username\":\"admin\",\"password\":...})")
    lbl.pack()
    ety = tk.Entry(new_win, name="entry_login", width=50)
    ety.insert(0, '{"username": "admin", "password": "password", "Login":"Login"}')
    ety.pack()
    lbl2 = tk.Label(new_win, text="URL de login")
    lbl2.pack()
    ety2 = tk.Entry(new_win, name="entry_url", width=50)
    ety2.pack()
    btn = tk.Button(new_win, text="OK", width=25, command=login_callback)
    btn.pack()


    new_win.mainloop()
    sys.stdout.flush()


def btn_check_vuln():
    global root, webScanner,statutVuln,treeLink,treeVuln,speed,treeError
    selectedItem = treeLink.selection()
    selectedLinks = []
    for item in selectedItem:
        selectedLinks.append(treeLink.item(item)['text'])
    statutVuln['text'] = "Recherche de vulnérabilités en cours..."
    webScanner.check_vuln(link_list=selectedLinks)
    statutVuln['text'] = "Recherche de vulnérabilités terminé !"
    i=0

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
    global webScanner,treeError,errors_window
    if errors_window :
        errors_window.lift()
    else :
        errors_window = tk.Toplevel()
        errors_window.title("Erreurs")
        errors_window.geometry("500x300")
        imgIcon= Image.open('data/icon.png')
        imgIcon = ImageTk.PhotoImage(imgIcon)
        errors_window.wm_iconphoto(False, imgIcon)

        #affichage des erreur  dans un arbre :
        treeError = ttk.Treeview(errors_window,height=10,selectmode="browse",show=("tree",))
        treeError.column("#0", anchor="w", width=160)
        if webScanner !=None:
            tree_Error = webScanner.error
        else :
            tree_Error = ["Hum, il n'y a rien ici pour le moment et c'est tant mieux..."]
        if tree_Error != []:
            if len(tree_Error) > 10:
                while len(tree_Error) > 10:
                    tree_Error.pop(0)
            if len(tree_Error) >=2 and "Hum, il n'y a rien ici pour le moment et c'est tant mieux..." in tree_Error:
                tree_Error.pop(0)
            x=1
            for error in tree_Error:
                treeError.insert(parent="", index=x, iid=x, text=error)
                x+=1
                treeError.selection_set(1)
        treeError.place(relx=0.037, rely=0.10, relheight=0.855, relwidth=0.93)

        treeError.bind('<Button-2>', lambda e: popup2(e,1))
        errors_window.protocol("WM_DELETE_WINDOW", on_closingError)


def set_filter():
    global webScanner, filters, filtrerScan_window
    if filtrerScan_window:
        filtrerScan_window.lift()
    else:
        filtrerScan_window = tk.Toplevel()
        filtrerScan_window.title("Filtrer")
        filtrerScan_window.geometry("500x300")
        imgIcon= Image.open('data/icon.png')
        imgIcon = ImageTk.PhotoImage(imgIcon)
        filtrerScan_window.wm_iconphoto(False, imgIcon)
        for i, filter in enumerate(filters):
            value = tk.BooleanVar(value=filter[1])
            check = ttk.Checkbutton(filtrerScan_window, text=filter[0], variable=value)
            check.pack()
            def callback(*args):
                filters[i][1] = value.get()
            value.trace("w", callback)
        filtrerScan_window.protocol("WM_DELETE_WINDOW", on_closingFilter)

#Fermetures des fenetres
def on_closingFilter():
    global filtrerScan_window
    filtrerScan_window.destroy()
    filtrerScan_window = None
def on_closingError():
    global errors_window
    errors_window.destroy()
    errors_window = None
def on_closingSettings():
    global settings_window
    settings_window.destroy()
    settings_window = None



def getFilter():
    global filters
    return filters


def show_settings():
    global settings_window,simplify
    print("settings : ", "scan réduit : ",simplify.get())
    if settings_window :
        settings_window.lift()
    else :
        settings_window = tk.Toplevel()
        settings_window.title("Paramètres")
        settings_window.geometry("1240x720")
        imgIcon= Image.open('data/icon.png')
        imgIcon = ImageTk.PhotoImage(imgIcon)

        #creation des widgets
        logoScan=ttk.Label(settings_window,text="Crawler :")
        simplifyScan = ttk.Checkbutton(settings_window, text="recherche restreinte", variable=simplify, command=updateSimplifyScan)

        #placement des widgets
        logoScan.place(x=20,y=20)
        simplifyScan.place(x=40, y=40)

        settings_window.wm_iconphoto(False, imgIcon)
        settings_window.protocol("WM_DELETE_WINDOW", on_closingSettings)

def updateSimplifyScan():
    global simplify
    if simplify.get():
        simplify.set(True)
    else:
        simplify.set(False)