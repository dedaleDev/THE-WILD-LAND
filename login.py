import json
import os
import app  
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
    
cookiesRoot = None
tableau =None
class Tableau(tk.Frame):
    def __init__(self,parent):
        super().__init__(parent)
        self.tableau=ttk.Treeview(self,columns=("Valeur","Domain"))
        self.tableau.heading("#0",text="Nom")
        self.tableau.heading("Valeur",text="Valeur")
        self.tableau.heading("Domain",text="Domain")


        self.tableau.pack(side="left",fill="both",expand=True)

        self.entree_nom = ttk.Entry(self)
        self.entree_valeur = ttk.Entry(self)
        self.entree_domain = ttk.Entry(self)
        self.entree_nom.insert(0, "Nom")
        self.entree_valeur.insert(0, "Valeur")
        self.entree_domain.insert(0, "Domaine")

        self.entree_nom.pack(side="top",fill="x")
        self.entree_valeur.pack(side="top",fill="x")
        self.entree_domain.pack(side="top",fill="x")

        self.addButton = ttk.Button(self,text="Ajouter", command=self.add)
        self.addButton.pack(side="top")

        self.clearButton = ttk.Button(self,text="Effacer", command=self.clear)
        self.clearButton.pack(side="top")
        self.load_cookies()

    def add(self):
        nom = self.entree_nom.get()
        valeur = self.entree_valeur.get()
        domain = self.entree_domain.get()

        self.tableau.insert('','end',text=nom,values=(valeur,domain))

        #effacer entree :
        self.entree_nom.delete(0,'end')
        self.entree_valeur.delete(0,'end')
        self.entree_domain.delete(0,'end')

    def getValue(self):
        values = []
        for item in self.tableau.get_children():
            nom = self.tableau.item(item,'text')
            valeur =  self.tableau.item(item,'values')[0]
            domain =  self.tableau.item(item,'values')[1]
            values.append([nom,valeur,domain])
        return values

    def clear(self):
        self.tableau.delete(*self.tableau.get_children())
        

    def load_cookies(self):
        cookies_path = "caches/cookies.json"
        try :
            if os.path.exists(cookies_path):
                with open(cookies_path, "r") as f:
                    if f != "":
                        cookies = json.load(f)
                        for cookie in cookies:
                            nom = cookie[0]
                            valeur = cookie[1]
                            domain = cookie[2]
                            self.tableau.insert("", "end", text=nom, values=(valeur, domain))
        except Exception as e:
            pass


def showCookiesSettings():
    global cookiesRoot,tableau
    if cookiesRoot != None:
        return
    #creation d'un fenetre permettant de définir un cookies de session :
    app.settings_window.attributes("-topmost", False)
    cookiesRoot = tk.Toplevel()
    cookiesRoot.title("Paramètres des cookies de session")
    cookiesRoot.geometry("1000x600")
    imgIcon= Image.open('data/icon.png')
    imgIcon = ImageTk.PhotoImage(imgIcon)
    cookiesRoot.attributes("-topmost", True)
    labelExplication =ttk.Label(cookiesRoot,text="Veuillez entrez vos cookies de sessions ici :")

    #creation du tableau : 
    tableau=Tableau(cookiesRoot)

    tableau.pack(side='top',fill="both",expand=True)
    labelExplication.place(x=20,y=10)
    cookiesRoot.wm_iconphoto(False, imgIcon)
    cookiesRoot.protocol("WM_DELETE_WINDOW", on_closingCookiesSetting)
    
def on_closingCookiesSetting():
    global cookiesRoot,tableau
    cookiesRoot.attributes("-topmost", False)
    app.settings_window.attributes("-topmost", True)
    # enregistrement des données dans le fichier cookies.json
    cookies_path = "caches/cookies.json"
    cookies = tableau.getValue()
    if os.path.exists("caches"):
        with open(cookies_path, "w") as f:
            json.dump(cookies, f)
    else:
        os.mkdir("caches")
        with open(cookies_path, "w") as f:
            json.dump(cookies, f)
    cookiesRoot.destroy()
    cookiesRoot = None
    return

def loginDriver(driver, url):
    #connexion au site web si besoin pour le scanner
    driver.get(url)
    return  driver



