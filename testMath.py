import math



def produit(v1, v2):
      
      return sum((a*b) for a, b in zip(v1, v2))

def longueur(v):
   
  return math.sqrt(produit(v, v))

def angle(v1, v2):
  
  return math.acos(produit(v1, v2) / (longueur(v1) * longueur(v2)))

def genererAngle():
        #dx, dy = self.cibleX - self.rect.x, self.cibleY - self.rect.y
        dx,dy = 274, 249
        return angle([1,0],[-1,0])*180/math.pi
a = angle([1, 0], [274,249])

a   =    genererAngle()
