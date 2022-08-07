##Fichier d'aide a la gestion d'un csv
import csv
#save = csv.reader(open('save.csv'))
def valCorrespondante(chaine): #renvoie la valeur en face d'une chaine de char
    save = csv.reader(open('save.csv'), delimiter=',')
    csvListe = list(save)
    chaine = chaine+" "
    for line in csvListe :
        if line[0]==chaine:
            return line[1]

def remplacerVal(chaine, ecriture, ajout=False): #ajout = doit on ajouter la valeur si elle n'est pas trouvé
    save = csv.reader(open('save.csv', newline=''), delimiter=',')
    trouve=False
    csvListe = list(save)
    chaine = chaine+" "
    for line in csvListe :
        if line and line[0]==chaine:
            line[1]=ecriture
            trouve=True
    if not trouve and ajout:
        csvListe.append([chaine, ecriture])
    writer = csv.writer(open('save.csv', 'w', newline=''))
    writer.writerows(csvListe)


