from calendar import month_abbr
#from PIL import Image, ImageDraw
images = []
import time





def make_step(k, m, a):
  for i in range(len(m)):
    for j in range(len(m[i])):
      
      if m[i][j] == k:
        
        if i>0 and m[i-1][j] == 0 and a[i-1][j] == 0:
          m[i-1][j] = k + 1
        if j>0 and m[i][j-1] == 0 and a[i][j-1] == 0:
          m[i][j-1] = k + 1
        if i<len(m)-1 and m[i+1][j] == 0 and a[i+1][j] == 0:
          m[i+1][j] = k + 1
        if j<len(m[i])-1 and m[i][j+1] == 0 and a[i][j+1] == 0:
           m[i][j+1] = k + 1
        ###ajout
        
        if i>0 and j>0 and m[i-1][j-1] == 0 and a[i-1][j-1] == 0:
              m[i-1][j-1] = k + 1
              
        if i<len(m)-1 and j<len(m[i])-1 and m[i+1][j+1] == 0 and a[i+1][j+1] == 0:
              m[i+1][j+1] = k + 1
              
        if i>0 and j<len(m[i])-1 and m[i-1][j+1] == 0 and a[i-1][j+1] == 0:
              m[i-1][j+1] = k + 1
              
        if i<len(m)-1 and j>0 and m[i+1][j-1] == 0 and a[i+1][j-1] == 0:
              m[i+1][j-1] = k + 1

def print_m(m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            print( str(m[i][j]).ljust(2),end=' ')
        print()


def draw_matrix(a, m, zoom, start, end, borders, the_path = []):
    im = Image.new('RGB', (zoom * len(a[0]), zoom * len(a)), (255, 255, 255))
    draw = ImageDraw.Draw(im)
    for i in range(len(a)):
        for j in range(len(a[i])):
            color = (255, 255, 255)
            r = 0
            if a[i][j] == 1:
                color = (0, 0, 0)
            if i == start[0] and j == start[1]:
                color = (0, 255, 0)
                r = borders
            if i == end[0] and j == end[1]:
                color = (0, 255, 0)
                r = borders
            draw.rectangle((j*zoom+r, i*zoom+r, j*zoom+zoom-r-1, i*zoom+zoom-r-1), fill=color)
            if m[i][j] > 0:
                r = borders
                draw.ellipse((j * zoom + r, i * zoom + r, j * zoom + zoom - r - 1, i * zoom + zoom - r - 1),
                               fill=(255,0,0))
    for u in range(len(the_path)-1):
        y = the_path[u][0]*zoom + int(zoom/2)
        x = the_path[u][1]*zoom + int(zoom/2)
        y1 = the_path[u+1][0]*zoom + int(zoom/2)
        x1 = the_path[u+1][1]*zoom + int(zoom/2)
        draw.line((x,y,x1,y1), fill=(255, 0,0), width=5)
    draw.rectangle((0, 0, zoom * len(a[0]), zoom * len(a)), outline=(0,255,0), width=2)
    im = im.rotate(45)
    images.append(im)




def findPos(game, posDebutX, posDebutY, posFinX, posFinY, aqua=False, aerien=False, desertique=False):
    
    startTime = time.time()
    
    if aerien:
        a=game.mapVide
    elif not aqua :
        a = game.mapMontagneMer
    elif desertique:
        a = game.mapDesert
    else :
        a = game.mapMer
    
    if not type(posDebutX)==int and type(posDebutY)==int and type(posFinX)==int and type(posFinY)==int and game.verifierCo(posDebutX, posDebutY) and game.verifierCo(posFinX, posDebutY):
        print("ATTENTION BUG : posDebutX, posDebutY=", posDebutX, posDebutY, "posFinX, posFinY=", posFinX, posFinY)
        return [[posFinX, posFinY]]
    
    zoom = 20
    borders = 6
    start = (posDebutY, posDebutX)
    end = (posFinY, posFinX)
    
    m = []
    for i in range(len(a)):
        m.append([])
        for j in range(len(a[i])):
            m[-1].append(0)
    
    i,j = start
    
    try:
        m[i][j] = 1
    except IndexError:
        print("BUG !!! merci de l'envoyer avec tout le rapport d'erreur")
        print("fonction findPos, i,j=",i,j,"out of range try exept")
        print("posFin, posDebut=", end[0], end[1])
        print("hauteur = ", len(m), "largeur=", len(m[0]))
        return [[posDebutX, posDebutY]]

    k = 0
    while m[end[0]][end[1]] == 0 and time.time()-startTime<0.005:
        
        k += 1

        make_step(k, m, a)
        #draw_matrix(a, m, zoom, start, end, borders)


    i, j = end
    k = m[i][j]
    the_path = [(i,j)]
    while k > 1 and time.time()-startTime<0.005:
        
        if j > 0 and m[i][j - 1] == k-1:
            i, j = i, j-1
            the_path.append((i, j))
            k-=1
        elif i < len(m) - 1 and m[i + 1][j] == k-1:
            i, j = i+1, j
            the_path.append((i, j))
            k-=1
        elif j < len(m[i]) - 1 and m[i][j + 1] == k-1:
            i, j = i, j+1
            the_path.append((i, j))
            k -= 1
        elif i > 0 and j>0 and m[i - 1][j-1] == k-1:
            i, j = i-1, j-1
            the_path.append((i, j))
            k-=1
        elif j > 0 and i<len(m)-1 and m[i+1][j - 1] == k-1:
            i, j = i+1, j-1
            the_path.append((i, j))
            k-=1
        elif i < len(m) - 1 and j < len(m[i]) - 1 and m[i + 1][j+1] == k-1:
            i, j = i+1, j+1
            the_path.append((i, j))
            k-=1
        elif i >0 and j<len(m[i])-1 and m[i-1][j+1] == k-1:
            i, j = i-1, j+1
            the_path.append((i, j))
            k -= 1
        elif i > 0 and m[i - 1][j] == k-1:
            i, j = i-1, j
            the_path.append((i, j))
            k-=1
        #draw_matrix(a, m, zoom, start, end, borders, the_path)

    """for i in range(10):
        if i % 2 == 0:
            draw_matrix(a, m, zoom, start, end, borders, the_path)
        else:
            draw_matrix(a, m, zoom, start, end, borders)"""

    #print_m(m)


    #print("--- %s seconds ---" % (time.time() - startTime))

    """images[0].save('maze.gif',
                save_all=True, append_images=images[1:],
                optimize=False, duration=1, loop=0)"""
    if len(the_path)==1:
        return the_path
    return the_path[1:]
