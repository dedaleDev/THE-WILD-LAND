import re
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import re

#LFI /RFI: 
def check_lfi_rfi_vulnerabilities(page=None, source_code=None):
    print("scanning LFI/RFI")
    options = webdriver.FirefoxOptions()
    options.add_argument('-headless')
    driver = webdriver.Firefox(options=options)
    driver.get(page)
    WebDriverWait(driver, 10).until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
    if source_code != None:
        driver.execute_script("document.documentElement.innerHTML ="+str(source_code))

    # Recherche des URL qui contiennent des paramètres de type 'file' ou 'path'
    links = driver.find_elements_by_xpath("//a[@href]")
    for link in links:
        link_url = link.get_attribute("href")
        if re.search(r"(file=|path=)", link_url):
            # Vérifie si l'URL contient des caractères suspects tels que "../" ou "..\"
            if re.search(r"(\.\.\/|\.\.\\|\.\.%2F|\.\.%5C)", link_url):
                print("Vulnérabilité LFI/RFI détectée dans l'URL : " + link_url)
            else:
                print("Vulnérabilité LFI/RFI potentielle détectée dans l'URL : " + link_url)

    # Recherche de formulaires qui acceptent des fichiers
    forms = driver.find_elements_by_xpath("//form[@enctype='multipart/form-data']")
    for form in forms:
        form_action = form.get_attribute("action")
        if re.search(r"(file=|path=)", form_action):
            print("Vulnérabilité LFI/RFI potentielle détectée dans le formulaire avec action : " + form_action)

    # Recherche de champs de saisie qui acceptent des fichiers
    file_inputs = driver.find_elements_by_xpath("//input[@type='file']")
    for file_input in file_inputs:
        file_input_name = file_input.get_attribute("name")
        if file_input_name:
            print("Vulnérabilité LFI/RFI potentielle détectée dans le champ de saisie de fichier : " + file_input_name)

    driver.quit()
