import pygame

class Tuile(pygame.sprite.Sprite):
    def __init__(self, type, posX, posY, game):
        super().__init__()
        self.game = game
        
        
        ####     SPECIFICITE    ####
        
        self.type = type
        self.canon = False
        self.scierie = False
        self.moulin = False
        self.puit= False
        self.forge = False
        self.port = False
        self.mine=False
        self.pieux=False
        self.aEteModifie = True
        self.champs = False
        self.elevage=False
        self.tour = False
        self.pieux=False
        self.mortier=False
        self.ventilo=False
        self.frigo=False
        self.sableMouvant=False
        self.trou=False
        ####     GENREATION    ####
        self.probaSup_mer = 0
        self.probaSup_roche = 0
        self.probaSup_foret = 0
        self.probaSup_desert = 0
        self.probaSup_neige = 0
        self.autoriserNeige = False 
        self.autoriserDesert = True
        
        
        self.estSelect = False
        self.isExplored = self.type==7
        
        ####     POSITION ET IMAGE    ####
        
        self.posX = posX
        self.posY = posY
        self.image= game.images.returnImg(self.type)
        self.imageO=game.images.returnImgO(self.type)

        self.rect = self.image.get_rect()
        self.rect.x = self.avoirX()
        self.rect.y = self.avoirY()
        self.Xoriginal = self.rect.x
        self.Yoriginal = self.rect.y
        self.mask=pygame.mask.from_surface(self.image)
    
    
    def getExplored(self):
        return self.isExplored
    
    def setExplored(self, bool):
        self.aEteModifie=True
        self.isExplored = bool

    def getRectX(self):
        return  self.rect.x

    def setSelect(self, bool):
        self.estSelect = bool

    def getRectY(self):
        return  self.rect.y


    def avoirX(self):
        return self.posX*244//2+self.posY*244//2-10

    def estPlaine(self):
        return self.type==1
    def estForet(self):
        return self.type==4
    def avoirY(self):
        return self.posY*142//2-self.posX*142//2+142//2*self.game.taille_matriceY

    def caseBloquante(self):
        return self.type==2 or self.type==7 or self.type == 3
    
    def setType(self, entier):
        self.type=entier
        self.imageO = self.game.images.returnImgO(entier)

    

    def getType(self):
        return self.type

    def getProbaMer(self):
        return self.probaSup_mer
    
    def getProbaDesert(self):
        return self.probaSup_desert

    def getProbaRoche(self):
        return self.probaSup_roche

    def getProbaNeige(self):
        return self.probaSup_neige

    def getProbaForet(self):
        return self.probaSup_foret

    def getCanon(self):
        return self.canon

    def getAutoriserNeige(self):
        return self.autoriserNeige
    
    def getAutoriserDesert(self):
        return self.autoriserDesert
    
    def setInterdireDesert(self):
        self.autoriserDesert = False
    
    def setAutoriserNeige(self):
        self.autoriserNeige = True
    
    def interdireNeige(self):
        self.autoriserNeige = False
    
    def augmenterProbaMer(self, entier):
        self.probaSup_mer += entier

    def augmenterProbaRoche(self, entier):
        self.probaSup_roche += entier

    def augmenterProbaForet(self, entier):
        self.probaSup_foret += entier
    def augmenterProbaDesert(self, entier):
        self.probaSup_desert += entier
    def augmenterProbaNeige(self, entier):
        self.probaSup_neige += entier

    def estMontagne(self):
        return self.type==2
    def estForet(self):
        return self.type==4
    
    def tuileHaute(self):
        return self.type==2 or self.type==7

    def pasPort(self):
        return not self.port
    
    def estMer(self):
        return self.type==3

    def decalerX(self, valeur):
        self.rect.x+=valeur
        
    def decalerY(self, valeur):
        self.rect.y+=valeur
