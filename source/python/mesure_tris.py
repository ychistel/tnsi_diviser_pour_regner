from random import randint
from time import time
from tri_fusion import fusion,tri_fusion

def tri_selection(tableau):
    i=0
    while i<len(tableau):
        k=i
        j=k
        while k < len(tableau):
            if tableau[k] < tableau[j]:
                j=k
            k=k+1
        tableau[i],tableau[j] = tableau[j],tableau[i]
        i=i+1
    return tableau

def tri_insertion(tableau):
    
    n = len(tableau)
    i = 1
    
    while i < n:
        j = i - 1
        tampon = tableau[i]

        while j >= 0 and tableau[j] > tampon:
            tableau[j+1] = tableau[j]
            j = j - 1
        
        tableau[j+1] = tampon
        i = i + 1
    return tableau


def mesure_tri(fct,n):
    
    tps = 0.0
    
    # on effectue 100 mesures de temps d'exécution de la fonction
    for _ in range(10):
        # on crée un tableau de dimension n
        t = [randint(0,100000) for i in range(n)]
        expression = fct + "(t)"
        
        # relevé du temps initial
        t_0 = time()
        
        # on exécute la fonction de tri
        eval(expression)

        # relevé du temps final
        t_1 = time()
        
        # on ajoute le temps d'exécution de la fonction
        tps = tps + (t_1-t_0)
    
    # on renvoie le temps moyen d'exécution de la fonction
    return tps/10


# on définit la taille du tableau
n = 4000
# on mesure les temps moyens d'exécution des tris
tps_selection = round(mesure_tri("tri_selection",n),3)
tps_insertion = round(mesure_tri("tri_insertion",n),3)
tps_fusion = round(mesure_tri("tri_fusion",n),3)
print(f"le temps de tri par insertion de {n} nombres est {tps_insertion} seconde")
print(f"le temps de tri par sélection de {n} nombres est {tps_selection} seconde")
print(f"le temps de tri fusion de {n} nombres est {tps_fusion} seconde")