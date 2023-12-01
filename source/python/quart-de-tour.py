from PIL import Image
im = Image.open("tux256.png")
largeur,hauteur=im.size
px = im.load()

for k in range(4):
    for l in range(4):
        px[255-k,255-l]=(255,0,0,255)

def rotation_aux(px,x,y,t):
    if t>1:
        t=t//2
        rotation_aux(px,x,y,t)
        rotation_aux(px,x+t,y,t)
        rotation_aux(px,x,y+t,t)
        rotation_aux(px,x+t,y+t,t)
        for i in range(x,x+t):
            for j in range(y,y+t):
                px[i,j],px[i,j+t],px[i+t,j+t],px[i+t,j]=px[i+t,j],px[i,j],px[i,j+t],px[i+t,j+t]
                
def rotation(px,taille):
    rotation_aux(px,0,0,taille)
    return im

image=rotation(px,largeur)
image.show()