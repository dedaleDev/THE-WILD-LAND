#!/usr/bin/env python3
# coding:utf-8
import re
import sys
import threading
import urllib
import urllib.request
import urllib.response
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import app  
import re


#IMPORT VULN PRISE EN CHARGE :
import sql
import xss
import rfi_lfi
import session


class WebScanner:
    def __init__(self, url, proxy=None, ssl =True,avancedScan=False,browser="Firefox"):
        #initialisation du scawler web : prend en argument : l'url, un eventuel proxy, le simulateur de machine utilisateur et le patch du protocole ssl
        if not url.endswith("/") and not url.endswith(".php") and not url.endswith(".html"):#si l'url ne se termine pas normalement on ajoute un slash à la fin
            self.url = url + "/"
        else:#sinon on save l'url telle quelle
            self.url = url
        self.proxy = proxy
        
        self.session = requests.Session()#creation d'une session pour le crawler permet de maintenir les cookies sur les pages
        self.link_list = []#liste des liens
        self.analyseLink = []#liste à analyser
        self.vulnFound=[]
        self.nbLink = 0#nombre de liens total trouvé
        self.stopped = False#si le scan est stoppé 
        self.avancedScan =avancedScan
        self.error =[]
        self.scanStatus = "En attente"
        if browser == "Firefox":
            self.user_agent ="Mozilla/5.0 (X11; Linux i686; rv:110.0) Gecko/20100101 Firefox/110.0"
        elif browser == "Chrome" : 
            self.user_agent ="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
        elif browser == "Safari" :
            self.user_agent ="Mozilla/5.0 (Macintosh; Intel Mac OS X 13_2_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.3 Safari/605.1.15"
        elif browser == "Edge":
            self.user_agent ="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/110.0.1587.63"
        print("scan on : ",self.user_agent)
    def getLinkList(self):
        return self.link_list

    def print_link_list(self):
        #print tous les liens
        for link in self.link_list:
            print(link)

    def get_page_source(self, page=None):
        #Obtient le code source d'une page web
        #prend en paramètre la page recherchée, sinon utilise self.url
        #retourn le code source de la page

        if page is None: #si la page n'a pas été spécifié on prend l'url de la classe 
            page = self.url
        page = page.strip()#supprimer les espaces inutiles au debut/fin de l'url
        user_agent = {"User-agent": self.user_agent}

        try:#tente de recuperer le code source de la page si elle n'est pas accessible on print l'erreur
            if self.proxy:#si on a un proxy on l'utilise
                res = self.session.get(page, headers=user_agent, proxies=self.proxy)#on obtient le code source de la page
            else:
                res = self.session.get(page, headers=user_agent)#pareil mais sans proxy
        except Exception as e:#en cas de problème d'url on print l'erreur
            app.webScanner.error.append("[-] Erreur pour la page : " + page + " " + str(e))
            return None
        return res.text#retourne le code source de la page

    def get_page_links(self, page=None, simplify=True):
        #obtient les tous les liens disponible d'une page web (href), excluant les liens externes
        #prend en paramètre la page recherchée, sinon utilise self.url
        #return une liste contenant les liens d'une page
        #si l'option simplify est utilisé on supprimer les liens contenant certains mot reférencé comme inutile par exemple : "Facebook", "Youtube"...
        link_list = []  # la liste de liens internes à "page"
        forbidden_pattern = r"https?://.*(trustpilot|youtube|facebook|amazon|twitter|github|google|linkedin|instagram|dailymotion|vimeo|pinterest|aliexpress|leboncoin|slack|reddit|4chan).*"


        if page is None:#si aucune url n'est spécifié
            page = self.url
        source = self.get_page_source(page)#on obtient le code source de la page

        if source is not None: #si le code source est accessible
            soup = BeautifulSoup(source, "html.parser") #on extrait les balises html pour pouvoir les manipuler
            uparse = urlparse(page)#decoupage de l'url
            for link in soup.find_all("a"):#pour chaque lien de la page HTML
                if not link.get("href") is None:#si le lien n'est pas vide
                    href = link.get("href")#obtient le lien
                    if "#" in href:  # supprime les potentiels ancre #
                        href = href.split("#")[0]

                    new_link = urllib.parse.urljoin(page, href)#permet de joindre l'url de la page avec le lien trouvé pour avoir un lien complet
                    blockLink = False
                    if simplify:#si l'option simplify est activé on supprime les liens contenant certains mots à éviter 
                        if re.search(forbidden_pattern,new_link):
                                blockLink = True
                                  
                        if uparse.hostname in new_link and new_link not in link_list and not blockLink:#si le lien est interne et qu'il n'est pas déjà dans la liste et qu'il n'est pas bloqué
                            link_list.append(new_link)
                    else :
                        link_list.append(new_link)

            for script in soup.find_all("script"):
                if not script.get("src") is None:
                    src = script.get("src")
                    new_link = urllib.parse.urljoin(page, src)
                    blockLink = False
                    if simplify:
                        if re.search(forbidden_pattern,new_link):
                            blockLink = True

                        if uparse.hostname in new_link and new_link not in link_list and not blockLink:
                            link_list.append(new_link)
            return link_list
        else:
            return []

    def print_cookies(self):
        #print les cookies de la session
        for cookie in self.session.cookies:
            print(cookie)

    def get_cookies(self):
        #return la liste des cookies de la session sous forme de dictionnaire
        return self.session.cookies

    def _do_crawl(self, queue, page=None,simplify=True):
        #cette fonction recursive permet de crawler l'ensemble d'un site web
        #paramètre queue multiprocessing pour y placer les liens à crawler
        #paramètre page = page recherché sinon utilise self.url
        try:
            if page not in self.link_list and page==None:#ajoute la page racine
                self.link_list.append(self.url)
                self.nbLink += 1
                queue.put(self.url)

            page_links = self.get_page_links(page,simplify=simplify)
            for link in page_links:
                if self.stopped:  # si l'utilisateur souhaite arrêter le scan via le bouton
                    break
                if link not in self.link_list:#evite les doublons
                    self.link_list.append(link)
                    self.nbLink += 1
                    queue.put(link)#ajout du lien à la queue multiprocessing c'est à dire à la file de lien à crawler. En effet, chaque lien doit être ensuite parcourut par le crawler
                    self._do_crawl(queue, link, simplify=simplify)#la fonction se rappelle elle même pour crawler le nouveau lien trouvé à chque fois on incrémente la queue de nouveaux liens
        #gestion des erreurs :
        except KeyboardInterrupt:
            print("\nProgramme terminé par l'utilisateur.")
            sys.exit(1)
        except Exception as e:
            app.webScanner.error.append("Error when crawler scan the link: " +page+" "+ str(e))

    def _crawl_end_callback(self, crawl_thread, crawl_queue):
        # Tâche d'arrière-plan permettant de savoir lorsque le crawling est terminé
        #paramètre crawl_thread: crawl thread à vérifier
        #param crawl_queue: queue multiprocessing à utiliser pour envoyer le message de fin
        crawl_thread.join()# join bloque l'exécution du thread jusqu'à ce que crawl_thread ait terminé son exécution. Permet de s'assurer que le crawl est terminé avant de continuer
        crawl_queue.put("END")# ajoute le message "END" à la fin de la queue. Le message "END" indique que le crawl est terminé et que les autres threads peuvent arrêter leur exécution.

    def crawl(self, crawl_queue, page=None,simplify=True):
        #Crawl une page via une tâche d'arrière-plan
        #multiprocessing queue à utiliser pour les communications
        #param page: la page recherchée, sinon utilise self.url
        crawl_thread = threading.Thread(target=self._do_crawl, args=(crawl_queue, page,simplify))#crée le thread du crawl. La méthode prend en argument la fonction de crawl l'ensemble des liens d'une page
        crawl_thread.start()#demarrage du thread
        watch_thread = threading.Thread(target=self._crawl_end_callback, args=(crawl_thread, crawl_queue)) #créer un thread qui surveille le thread de crawl. Permet de savoir lorsque le crawler à fini
        watch_thread.start()#demarrage du thread de surveillance

    #VULNERABILITE

    def check_vuln(self,link_list):
        #Fonction  utilisée pour lancer la vérification automatique de vulnérabilités
        #prend en paramètre une queue multiprocessing pour executer les fonctions de vérification sur l'ensemble des liens
        #param link_list: la liste de liens à vérifier
        try:
            self.scanStatus = "Analyse : " +str(0)+"%"
            codeSource= app.getCodeSource()
            if codeSource != "" and codeSource != None:
                if "<html" in codeSource:
                    print("Code source défini par l'utilisateur : \n"+codeSource)
                else :
                    app.webScanner.error.append("Le code source n'est pas valide. Veuillez n'entrer uniquement du code HTML :"+codeSource)
                    codeSource = None
            else :
                codeSource = None
            filters = app.getFilters(returned=True)
            print("filters: ",filters)
            for link in link_list:#pour chaque lien on essaye de trouver des vulnérabilités
                #XSS
                if filters[0][1] == True:
                    self.scanStatus = "Analyse : XSS " +"lien n°"+str(link_list.index(link)+1)
                    app.updateStatut(self.scanStatus)
                    XSSScanner=xss.XSS_Scanner(link,codeSource)#test si il y a une faille SQL dans un formulaire
                    trouveXSS =XSSScanner.getVulnFound()
                    if trouveXSS != None:
                        self.vulnFound.append(trouveXSS)
                    app.updateTreeVuln()
                #SQL
                if filters[1][1] == True:
                    print("starting SQL scan")
                    self.scanStatus = "Analyse : SQL " +"lien n°"+str(link_list.index(link)+1)
                    app.updateStatut(self.scanStatus)
                    chk_sql_form = sql.check_sql_form(link,codeSource)#test si il y a une faille SQL dans un formulaire
                    app.updateStatut(self.scanStatus)
                    if chk_sql_form != "":
                        self.vulnFound.append(chk_sql_form)
                        print(self.vulnFound)
                    app.updateTreeVuln()
                #SESSION
                if filters[2][1] == True:
                    print("starting SESSION scan")
                    self.scanStatus = "Analyse : SESSION " +"lien n°"+str(link_list.index(link)+1)
                    app.updateStatut(self.scanStatus)
                    chk_session = session.check_session_vulnerabilities(link,codeSource)#test si il y a une faille de session dans un formulaire
                    if chk_session != "":
                        self.vulnFound.append(chk_session)
                    app.updateTreeVuln()
                #LFI/RFI
                if filters[3][1] == True:
                    print("starting LFI/RFI scan")
                    self.scanStatus = "Analyse : LFI/RFI " +"lien n°"+str(link_list.index(link)+1)
                    app.updateStatut(self.scanStatus)
                    chk_lfi_rfi = rfi_lfi.check_lfi_rfi_vulnerabilities(link,codeSource)#test si il y a une faille de session dans un formulaire
                    if chk_lfi_rfi != "":
                        self.vulnFound.append(chk_session)
                    app.updateTreeVuln()
            return
        except KeyboardInterrupt:
            print("\nProgramme arrêté par l'utilisateur.")
            sys.exit(1)
        except Exception as e:
            app.webScanner.error.append("Error execution analyse : " + str(e)+ "Erreur in xss.py at ligne : "+str(sys.exc_info()[-1].tb_lineno))
        