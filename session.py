from selenium import webdriver
from datetime import datetime, timedelta
from selenium.webdriver.support.ui import WebDriverWait
import re
#SCAN SESSION :

def check_session_vulnerabilities(page=None, source_code=None):
    print("scanning Session...")
    options = webdriver.FirefoxOptions()
    options.add_argument('-headless')
    driver = webdriver.Firefox(options=options)
    driver.get(page)
    WebDriverWait(driver, 10).until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
    if source_code != None:
        driver.execute_script("document.documentElement.innerHTML ="+str(source_code))

    # Utiliser une expression régulière pour rechercher des occurrences de 'session=' ou 'PHPSESSID=' dans l'URL
    session_vuln_in_url = re.search(r"(session=|PHPSESSID=)", driver.current_url)
    if session_vuln_in_url:
        vuln_detected = True
        print("FAILLE DE SESSION DETECTEE DANS LA PAGE " + str(page))
    else:
        print("Aucune vulnérabilité de session dans l'URL.")

    # Utiliser une expression régulière pour rechercher des occurrences de 'session' ou 'PHPSESSID' dans les cookies
    cookies = driver.get_cookies()
    for cookie in cookies:
        if re.search(r"(session|PHPSESSID)", cookie['name']):
            # Vérifie si le cookie de session a l'attribut "secure"
            if not "secure" in cookie.keys():
                return "FAILLE DE SESSION DETECTEE DANS DANS LE COOKIES DE LA PAGE : " + str(page)+" "+cookie['name'] + " n'est pas chiffré"
            # Vérifie si le cookie de session a l'attribut "HttpOnly"
            if not "HttpOnly" in cookie.keys():
                return "FAILLE DE SESSION DETECTEE DANS DANS LE COOKIES DE LA PAGE : " + str(page)+" "+cookie['name'] + " n'est pas protégé contre les accès par les scripts client"
            # Vérifie si le cookie de session a un temps d'expiration raisonnable
            if "expiry" in cookie.keys():
                expiration_time = datetime.fromtimestamp(cookie['expiry'])
                if expiration_time < datetime.now() + timedelta(days=30):
                    return "FAILLE DE SESSION DETECTEE DANS DANS LE COOKIES DE LA PAGE : " + str(page)+" "+cookie['name'] + " a un temps d'expiration trop court"
        else:
            return "FAILLE DE SESSION DETECTEE DANS DANS LE COOKIES DE LA PAGE : " + str(page)+" "+cookie['name'] + " n'a pas de temps d'expiration"
