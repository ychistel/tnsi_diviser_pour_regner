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
        self.case_libre = None
        
    def grille_case_grise(self):
        if not self.case_grise:
            self.case_grise = choice(self.grille)
            
    def grille_case_libre(self,case_libre):
        self.case_libre = case_libre
        
    def proche_case_grise(self,n,sommet,case_grise):
        x,y = sommet
        a,b = case_grise
        print("sommet:",x,y,"case grise:",a,b)
        return (x <= a < x + 2**(n-1)) and (y <= b < y + 2**(n-1))
        
    def ajouter_triomino(self,n,sommet,case_grise):
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
        print("n=",n,sommet,case_grise,triplet)
        self.grille_triominos.append(Triomino(triplet))
        
def recouvrir_grille(n,grille,sommet,case_grise):
    if n == 1:
        # cas de base : grille de côté 2
        # on ajoute le triomino
        grille.ajouter_triomino(n,sommet,case_grise)
    else:
        print("n=",n,"sommet",sommet,"case grise:",case_grise)
        x,y = sommet
        a,b = case_grise
        # on découpe la grille en 4 grilles
        if x <= a < x + 2**(n-1) and y <= b < y + 2**(n-1):
            print("1)")
            # la case grise est dans le premier quart
            recouvrir_grille(n-1,grille,(x,y),case_grise)
            # on recouvre le second quart avec la case grise au centre
            recouvrir_grille(n-1,grille,(x,y + 2**(n-1)),(x + 2**(n-1)-1,y + 2**(n-1)))
            # on recouvre le troisième quart avec la case grise au centre
            recouvrir_grille(n-1,grille,(x + 2**(n-1),y),(x + 2**(n-1),y + 2**(n-1)-1))
            # on recouvre le dernier quart avec la case grise au centre
            recouvrir_grille(n-1,grille,(x + 2**(n-1),y + 2**(n-1)),(x + 2**(n-1),y + 2**(n-1)))
            # on ajoute le triomino au centre sur les 3 cases grises
            
        elif x <= a < x + 2**(n-1) and y + 2**(n-1) <= b < y + 2**n:
            print("2)")
            # on recouvre le premier quart avec la case grise au centre
            recouvrir_grille(n-1,grille,(x,y),(x + 2**(n-1)-1,y + 2**(n-1)-1))
            print("fin 2 a)",n)
            # la case grise est dans le second quart
            recouvrir_grille(n-1,grille,(x,y + 2**(n-1)),case_grise)
            print("fin 2 b)",n)
            # on recouvre le troisième quart avec la case grise au centre
            recouvrir_grille(n-1,grille,(x + 2**(n-1),y),(x + 2**(n-1),y + 2**(n-1)-1))
            # on recouvre le dernier quart avec la case grise au centre
            recouvrir_grille(n-1,grille,(x + 2**(n-1),y + 2**(n-1)),(x + 2**(n-1),y + 2**(n-1)))
            # on ajoute le triomino au centre sur les 3 cases grises
            print("fin 2)")           
        elif x + 2**(n-1) <= a < x + 2**n and y <= b < y + 2**(n-1):
            print("3)")
            # on recouvre le premier quart avec la case grise au centre
            recouvrir_grille(n-1,grille,(x,y),(x + 2**(n-1)-1,y + 2**(n-1)-1))
            # on recouvre le second quart avec la case grise au centre
            recouvrir_grille(n-1,grille,(x,y + 2**(n-1)),(x + 2**(n-1)-1,y + 2**(n-1)))
            # la case grise est dans le troisième quart
            recouvrir_grille(n-1,grille,(x + 2**(n-1),y),case_grise)
            # on recouvre le dernier quart avec la case grise au centre
            recouvrir_grille(n-1,grille,(x + 2**(n-1),y + 2**(n-1)),(x + 2**(n-1),y + 2**(n-1)))
            # on ajoute le triomino au centre sur les 3 cases grises
            
        elif x + 2**(n-1) <= a < x + 2**n and y + 2**(n-1) <= b < y + 2**n:
            print("4)")
            # on recouvre le premier quart avec la case grise au centre
            recouvrir_grille(n-1,grille,(x,y),(x + 2**(n-1)-1,y + 2**(n-1)-1))
            # on recouvre le second quart avec la case grise au centre
            recouvrir_grille(n-1,grille,(x,y + 2**(n-1)),(x + 2**(n-1)-1,y + 2**(n-1)))
            # on recouvre le troisième quart avec la case grise au centre
            recouvrir_grille(n-1,grille,(x + 2**(n-1),y),(x + 2**(n-1),y + 2**(n-1)-1))
            # la case grise est dans le dernier quart
            recouvrir_grille(n-1,grille,(x + 2**(n-1),y + 2**(n-1)),case_grise)
        
        
        
        
# dimension de la grille 2^n
n = 4
# création de la grille
G = Grille(n,0,0)
# choix aléatoire de la case grise
G.grille_case_grise()
recouvrir_grille(n,G,(0,0),(6,2))
for val in G.grille_triominos:
    print(val.triplet)
    