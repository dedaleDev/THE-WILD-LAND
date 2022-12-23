import pygame
import os
class Tuto():
    def __init__(self,game,filename:str):
        self.name = str((filename.split("_")[1]).split(".")[0])
        self.game = game
        self.fenetre=game.fenetre
        self.infoObject=game.infoObject
        self.img =self.tutoImgLoad()
        self.imgRect = self.img.get_rect()
        self.fps= 500
        self.imgRect.x=game.infoObject[0]*0.7
        self.imgRect.y=game.infoObject[1]*0.1
        self.statut=False
    
    def getName(self):
        return self.name

    def tutoImgLoad(self): #charge l'image du tuto
        img=pygame.image.load("data/tuto/"+"tuto_"+self.name+".png").convert_alpha()
        img=pygame.transform.scale(img,(int(self.game.diagonalEcran*img.get_width()*0.0004),int(self.game.diagonalEcran*img.get_height()*0.0004)))
        return img

    def setStatut(self,statut:bool): #met à jour le statut du tuto (affiché ou non)
        self.statut=statut

    def getStatut(self):
        return self.statut

    def CheckClic(self,pos):#permet de savoir si le tuto est cliqué pour le masquer ensuite
        # Fonction qui charge et affiche une image à l'écran
        print(pos)
        if self.imgRect.collidepoint(pos[0],pos[1]):
            self.game.listeTuto.remove(self)




def createTuto(game): #fonction qui créer et charge les tutos
    path = os.path.dirname(__file__)
    path += "/data/tuto"
    listeTuto=[]
    for filename in os.listdir(path):
        if filename.endswith(".png"):
            listeTuto.append(Tuto(game,filename))
    return listeTuto
    
def getImgTuto(game):
    for tuto in game.listeTuto:
        if tuto.getStatut() ==True:
            return tuto.img

def upadateStatutTuto(game,nom:str, bool=True):
    for tuto in (game.listeTuto):
        if tuto.name == str(nom):
            tuto.setStatut(bool)
            return
def disableTuto(game):
    #ATTENTION : cette fonction peux avoir de serieuse consequence sur le jeu 
    # Merci de ne pas l'utiliser si vous ne savez pas ce que vous faites
    for tuto in game.listeTuto:
        if tuto.getStatut() == True:
            game.listeTuto.remove(tuto)

def afficherTuto(fenetre, game):
    for tuto in game.listeTuto:
        if tuto.getStatut():
            tuto.fps-=1
            fenetre.blit(tuto.img,(tuto.imgRect.x,tuto.imgRect.y))
            if tuto.fps<=0:
                game.listeTuto.remove(tuto)
            return
