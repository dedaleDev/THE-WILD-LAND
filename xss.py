import os
import app  
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import json
from datetime import datetime, timedelta

import gevent
from gevent import monkey
monkey.patch_all()
class XSS_Scanner():
    def __init__(self, page, source_code = None) -> None:
        self.payloads = ["<img src=x onerror=eval(atob('YWxlcnQoMSk='))>","<img src=x onerror=eval(String.fromCharCode(97,108,101,114,116,40,49,41))>",
                "<script>alert(1)</script>","<svg onload=alert('1')>","<img src=x onerror=alert('1') style='display:none'>", 
                "<a data-alert='1' onclick=eval(atob('YWxlcnQoJ2RhdGEtYWxlcnQnKQ=='))>XSS1234</a>",
                "<div><script>alert(String.fromCharCode(66, 82, 79, 87, 78))</script></div>","<iframe srcdoc='<script>alert(`1`)</script>'></iframe>"]
        self.threadsEnCours = False
        self.page =page
        self.source_code = source_code
        self.threads = []
        self.vulnFound=None
        self.vitesse = app.getSpeedScan()
        self.startScan()

    def getVulnFound(self):
        return self.vulnFound

    def startScan(self):
        #GESTION DES THREADS :
        #calcul du nombre de payload à scan par thread :
        try :
            if self.vitesse == 1:
                sous_liste = [self.payloads]
            else:
                taille_sous_liste = len(self.payloads) // self.vitesse
                reste = len(self.payloads) % self.vitesse
                sous_liste = []
                debut = 0
                for i in range(self.vitesse):
                    fin = debut + taille_sous_liste
                    if i < reste:
                        fin += 1 
                    sous_liste.append(self.payloads[debut:fin])
                    debut = fin
        except:
            print("Error cuttting payloads")
        #suppression des groupes vide :    
        groupesPayload=[]
        for groupe in sous_liste:
            if not(groupe == [] or groupe == None or groupe == "" or groupe == [ ]):
                groupesPayload.append(groupe)

        x=1
        for i in groupesPayload:
            #print("groupe de payload n°: ",x,":",i, "parmi :",len(self.payloads),"payloads /n")
            x+=1
        self.threadsEnCours = True
        try:
            threads = [gevent.spawn(self.check_xss_form, self.page, self.source_code, groupesPayload[i]) for i in range(self.vitesse)]
            gevent.joinall(threads)
        except Exception as e:
            print("Critical Error Multi Threading !!! " ,str(e), "Erreur in xss.py at ligne : ",str(sys.exc_info()[-1].tb_lineno))
        print("ending xss scan")


    def check_xss_form(self,page=None, source_code=None, payloads=[]):
        #analyse des failles xss des formulaire
        driver = self.getDriver()
        if driver == None :
            app.webScanner.error.append("Le driver du navigateur n'existe pas. Echec de l'analyse XSS. Veuillez vérifiez vos paramètres et ou configurations logicielles.")
            return 
        for payload in payloads:  
            print("try : ", payload)
            if self.threadsEnCours :
                driver.get(page)
                WebDriverWait(driver, 10).until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
                if source_code != None and source_code != "":#test si code source
                    driver.execute_script("document.documentElement.innerHTML ="+str(source_code))
                # remplir les champs du formulaire
                try : 
                    fields = driver.find_elements(By.XPATH, "//input | //textarea")
                except: 
                    app.webScanner.error.append("La recherche XSS à échoué car le formulaire n'a pas de champs ou ceci ne sont pas reconnu"+ "Erreur in xss.py at ligne : "+str(sys.exc_info()[-1].tb_lineno))
                    return
                for field in fields:
                    try : 
                        if field.is_displayed():
                            field.send_keys(str(payload))
                    except :
                        app.webScanner.error.append("La recherche XSS à échoué car le formulaire ne peux pas être rempli"+"Erreur in xss.py at ligne : "+ str(sys.exc_info()[-1].tb_lineno))
                # soumettre le formulaire
                try :
                    submit_button = driver.find_element(By.XPATH, "//input[@type='submit']")
                    submit_button.click()
                except :
                    app.webScanner.error.append("La recherche XSS à échoué car le formulaire n'a pas de bouton submit"+"Erreur in xss.py at ligne : "+str(sys.exc_info()[-1].tb_lineno))
                    driver.quit()
                    return
                # récupérer le contenu de l'alerte
                alert_text="No alert"
                if self.threadsEnCours == False :
                    print("XSS scan arreté car l'un des theads a trouvé une vulnérabilité")
                    driver.quit()
                    return
                try : 
                    alert=WebDriverWait(driver, 1).until(EC.alert_is_present())
                    alert_text = alert.text
                    alert.accept()
                except :
                    print("echec du payload : ",payload)
                if "1" in str(alert_text) or "BROWN" in str(alert_text) :
                    print("XSS detected with : ",  payload)
                    self.threadsEnCours = False
                    self.vulnFound="FAILLE XSS DETECTE DANS LE FORMULAIRE DE LA PAGE : " + str(page) + "avec :"+payload+ "\n"
                    driver.quit()
                    return
            else :
                driver.quit()
                return

    def getDriver(self):
        #revoie le driver correspondant au navigateur selectionné
        driver=None
        try : 
            if app.varBrowser.get()=="Firefox":
                options = webdriver.FirefoxOptions()
                #options.add_argument('-headless')
                driver =  webdriver.Firefox(options=options)
            elif app.varBrowser.get()=="Chrome" :
                if sys.platform.startswith('win'):
                    driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')
                elif sys.platform.startswith('linux'):
                    driver = webdriver.Chrome('/usr/bin/google-chrome')
                elif sys.platform.startswith('darwin'):
                    driver = webdriver.Chrome('/Applications/Google Chrome.app/Contents/MacOS/Google Chrome')
            elif app.varBrowser.get()=="Safari" :
                driver = webdriver.Safari()
            elif app.varBrowser.get()=="Edge" :
                if sys.platform.startswith('win'):
                    driver = webdriver.Edge('C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe')
                elif sys.platform.startswith('linux'):
                    driver = webdriver.Edge('/usr/bin/msedge')
                elif sys.platform.startswith('darwin'):
                    driver = webdriver.Edge('/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge')
            #chargement page vide :

            cookies_path = "caches/cookies.json"
            if driver != None:
                if os.path.exists(cookies_path):
                    with open(cookies_path, "r") as f:
                        if f != "":
                            cookies = json.load(f)
                            for cookie in cookies:
                                nom = cookie[0]
                                valeur = cookie[1]
                                domain = cookie[2]
                                cookie ={
                                        'name':str(nom),
                                        'value': str(valeur),
                                        'domain': str(domain),
                                        'path': '/',
                                        'expiry': int((datetime.utcnow() + timedelta(days=30)).timestamp()),
                                        'httpOnly': True,
                                        'secure': False,
                                        'sameSite': 'Lax',
                                        'partitionKey':'default',
                                        'priority': 'Medium'
                                        }
                                print(cookie)
                                
                                try : 
                                    if "https" in domain :
                                        driver.get(domain)
                                    else : 
                                        #nettoyage du domaine: 
                                        if domain[0]=="." or domain[0]=="/":
                                            domain=domain[1:]
                                        driver.get("https://"+str(domain))
                                    #driver.add_cookie(cookie)
                                except Exception as e:
                                    app.webScanner.error.append("Le navigateur n'est pas parvenu à ajouter un cookie veuillez verifier que le nom de domain est correct","Rapport de Crash : ",str(e))
            return driver
        except Exception as e:
                app.webScanner.error.append("Un problème liè au navigateur est survenu. Veuillez verifier dans les réglages que votre selection est la bonne. Navigateur selectioné actuellement :"+ app.varBrowser.get()+ "Rapport de Crash : "+ str(e))
                return 
        
    


    