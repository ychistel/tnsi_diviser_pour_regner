from PIL import Image

# création de la variable img associée à une image
# img est un objet de type PIL
img = Image.open("../img/tux256.png")

# on récupère les dimensions de l'image avec l'attribut size de img
largeur,hauteur = img.size

# on crée une variable px avec la méthode load()
# la variable px est un tableau contenant chaque pixel de l'image
# chaque pixel est un triplet de couleurs RGB
px = img.load()

def quart_de_tour(px,x,y,t):
    """
    - px : tableau contenant les pixel de l'image
    - x,y : indices du premier pixel d'une image carrée
    - t : côté d'une image carrée
    """    
    if t>1:
        # on divise la taille image par 2
        t=t//2
        # on tourne le quart haut gauche de l'image
        quart_de_tour(px,x,y,t)
        # on tourne le quart haut droit de l'image
        quart_de_tour(px,x+t,y,t)
        # on tourne le quart bas droit de l'image
        quart_de_tour(px,x+t,y+t,t)
        # on tourne le quart bas gauche de l'image
        quart_de_tour(px,x,y+t,t)
        # dans chaque carré d'image on décale les pixel
        for i in range(x,x+t):
            for j in range(y,y+t):
                px[i,j],px[i,j+t],px[i+t,j+t],px[i+t,j]=px[i+t,j],px[i,j],px[i,j+t],px[i+t,j+t]
     
if largeur==hauteur:
    quart_de_tour(px,0,0,largeur)
else:
    print("L'image n'est pas carrée !")

img.show()
