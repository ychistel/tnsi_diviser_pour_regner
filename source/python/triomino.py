from ipythonblocks import BlockGrid
from random import randint,choice

# définition des couleurs pour les triominos
couleurs = [(255,0,0),(0,255,0),(0,0,255),(255,255,0),(255,0,255),(0,255,255),(128,0,128)]

class Triomino:
    
    def __init__(self,triplet):
        """triomino représenté par un triplet de 2-uplet:
            paramètre : liste de 3 2-uplets
            attribut : triplet de 2-uplets
        """
        self.triplet = triplet
            
class Grille:
    
    def __init__(self,n):
        """
        On définit les attributs:
        - 'dimension' définit la taille de la grille : 2, 4, 8, 16, etc.
        - 'grille' est un tableau contenant des 2-uplets dont les valeurs sont les indices de position.
          Par exemple : grille = [(0,0),(0,1),(1,0),(1,1)] est une grille de 4 cases.
        - 'grille_triominos' comme grille contenant des triplets représentant chaque triomino posé sur la grille.
        - 'case_grise' est la case sur laquelle on ne peut pas poser de triomino.
        """
        self.grille = [(i,j) for i in range(2**n) for j in range(2**n)]
        self.grille_triominos = []
        self.case_grise = choice(self.grille)
       
    def cases_grises(self,n,sommet,case_grise):
        """renvoie les 4 cases grises lors d'un appel récursif avec les 4 sous grilles"""
        x,y = sommet
        a,b = case_grise
        cote = 2**n
        if x <= a < x + cote//2 and y <= b < y + cote//2:
            return (case_grise,(x + cote//2-1,y + cote//2),(x + cote//2,y + cote//2-1),(x + cote//2,y + cote//2))         
        elif x <= a < x + cote//2 and y + cote//2 <= b < y + cote:
            return ((x + cote//2-1,y + cote//2-1),case_grise,(x + cote//2,y + cote//2-1),(x + cote//2,y + cote//2))
        elif x + cote//2 <= a < x + cote and y <= b < y + cote//2:
            return ((x + cote//2-1,y + cote//2-1),(x + cote//2-1,y + cote//2),case_grise,(x + cote//2,y + cote//2))
        elif x + cote//2 <= a < x + cote and y + cote//2 <= b < y + cote:
            return ((x + cote//2-1,y + cote//2-1),(x + cote//2-1,y + cote//2),(x + cote//2,y + cote//2-1),case_grise)
        
    def ajouter_triomino(self,sommet,case_grise):
        """on découpe une grille en 4 sous-grilles jusqu'à obtenir des grilles de 4 carrés.
        Parmi ces 4 carrés, une case est une case grise non recouvrable. Les 3 autres carrés sont recouverts 
        par un triomino que l'on crée dans dans cette méthode.
        Chaque nouveau triomino est ajouté à l'attributs "triominos" de l'objet grille
        """
        triplet = []
        x,y = sommet
        if (x,y) != case_grise:
            triplet.append((x,y))
        if (x,y+1) != case_grise:
            triplet.append((x,y+1))
        if (x+1,y) != case_grise:
            triplet.append((x+1,y))
        if (x+1,y+1) != case_grise:
            triplet.append((x+1,y+1))
        self.grille_triominos.append(Triomino(triplet))

    def recouvrir_cases_grises(self,cases_grises,case_grise):
        """on recouvre par un triomino les trois cases grises adjacentes"""
        triplet = []
        for case in cases_grises:
            if case != case_grise:
                triplet.append(case)
        self.grille_triominos.append(Triomino(triplet))

def afficher(n,G):
    # affichage de la grille recouverte de triominos
    grille = BlockGrid(2**n, 2**n, block_size=120//n,fill=(255,255,192))
    
    i = 0
    
    for triomino in G.grille_triominos:
        """
        v = randint(0,255)
        rouge = v
        vert = (v + 30)%255
        bleu = (v + 60)%255
        """
        r,g,b = couleurs[i%7]
        for val in triomino.triplet:
            for cellule in grille:
                if (cellule.col,cellule.row)==val:
                    cellule.set_colors(r,g,b)
                if (cellule.col,cellule.row) == G.case_grise:
                    cellule.set_colors(25,25,25)
        i += 1
    return grille
