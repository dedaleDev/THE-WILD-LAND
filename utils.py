
def convertToBool(chaine:str):
    #fonction permettant la convertion d'une chaine de caractère str() vers un booléan True ou False
    chaine =str(chaine)
    if chaine =="True" or chaine == "true":
        return True
    else : 
        return False
