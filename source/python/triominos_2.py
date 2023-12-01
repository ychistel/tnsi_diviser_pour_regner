from random import randint,choice

class Triomino:
    
    def __init__(self,triplet):
        """triomino représenté par un triplet de 2-uplet:
            paramètre : liste de 3 2-uplets
            attribut : triplet de 2-uplets
        """
        self.triplet = triplet
            
class Grille:
    
    def __init__(self,n,x,y):
        self.dimension = 2**n
        self.grille = [(x+i,y+j) for i in range(self.dimension) for j in range(self.dimension)]
        self.grille_triominos = []
        self.case_grise = None
        
    def la_case_grise(self):
        if not self.case_grise:
            self.case_grise = choice(self.grille)
        return self.case_grise
       
    def cases_grises(self,n,sommet,case_grise):
        """renvoi les 4 cases grises pour l'appel récursif avec les 4 sous grilles"""
        x,y = sommet
        a,b = case_grise
        if x <= a < x + 2**(n-1) and y <= b < y + 2**(n-1):
            return (case_grise,(x + 2**(n-1)-1,y + 2**(n-1)),(x + 2**(n-1),y + 2**(n-1)-1),(x + 2**(n-1),y + 2**(n-1)))            
        elif x <= a < x + 2**(n-1) and y + 2**(n-1) <= b < y + 2**n:
            return ((x + 2**(n-1)-1,y + 2**(n-1)-1),case_grise,(x + 2**(n-1),y + 2**(n-1)-1),(x + 2**(n-1),y + 2**(n-1)))
        elif x + 2**(n-1) <= a < x + 2**n and y <= b < y + 2**(n-1):
            return ((x + 2**(n-1)-1,y + 2**(n-1)-1),(x + 2**(n-1)-1,y + 2**(n-1)),case_grise,(x + 2**(n-1),y + 2**(n-1)))
        elif x + 2**(n-1) <= a < x + 2**n and y + 2**(n-1) <= b < y + 2**n:
            return ((x + 2**(n-1)-1,y + 2**(n-1)-1),(x + 2**(n-1)-1,y + 2**(n-1)),(x + 2**(n-1),y + 2**(n-1)-1),case_grise)
        
    def ajouter_triomino(self,sommet,case_grise):
        """on découpe une grille en 4 sous-grilles jusqu'à obtenir des grilles de 4 carrés.
        Parmi ces 4 carrés, un est une case grise non recouvrable. Les 3 autres carrés sont recouverts 
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
        
def recouvrir_grille(n,grille,sommet,case_grise):
    if n == 1:
        # cas de base : grille de côté 2
        # on ajoute le triomino
        grille.ajouter_triomino(sommet,case_grise)
    else:
        print("n=",n,"sommet",sommet,"case grise:",case_grise)
        cote = 2**n
        x,y = sommet
        a,b = case_grise
        # on détermine les cases grises de chaque carré à recouvrir
        cases_grises = grille.cases_grises(n,sommet,case_grise)
        print("les cases grises:",cases_grises)
        # on découpe la grille en 4 grilles
        recouvrir_grille(n-1,grille,(x,y),cases_grises[0])
        # on recouvre le second quart avec la case grise au centre
        recouvrir_grille(n-1,grille,(x,y + 2**(n-1)),cases_grises[1])
        # on recouvre le troisième quart avec la case grise au centre
        recouvrir_grille(n-1,grille,(x + 2**(n-1),y),cases_grises[2])
        # on recouvre le dernier quart avec la case grise au centre
        recouvrir_grille(n-1,grille,(x + 2**(n-1),y + 2**(n-1)),cases_grises[3])
        # on ajoute le triomino au centre sur les 3 cases grises
        grille.recouvrir_cases_grises(cases_grises,case_grise)
    
# dimension de la grille 2^n
n = 3
# création de la grille
G = Grille(n,0,0)
# choix aléatoire de la case grise
case_grise = G.la_case_grise()
recouvrir_grille(n,G,(0,0),case_grise)
for val in G.grille_triominos:
    print(val.triplet)
    