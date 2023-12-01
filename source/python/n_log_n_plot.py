from matplotlib import pyplot
from math import log2
from random import randint
from time import time

def tri_fusion(liste):
    if len(liste)<2:
        return liste
    else:
        liste1=tri_fusion(liste[0:len(liste)//2])
        liste2=tri_fusion(liste[len(liste)//2:len(liste)])
        return fusion_tableau(liste1,liste2)
    
def fusion_tableau(t1,t2):
    i=0 # indice de t1
    j=0 # indice de t2
    t = []
    while i < len(t1) and j < len(t2):
        if t1[i] <= t2[j]:
            t.append(t1[i])
            i += 1
        else:
            t.append(t2[j])
            j += 1
        #print(t)
    while i < len(t1):
        t.append(t1[i])
        i += 1
    while j < len(t2):
        t.append(t2[j])
        j += 1
    return t

def tri_selection(tableau):
    i=0
    while i<len(tableau):
        k=i
        j=k
        while k<len(tableau):
            if tableau[k] < tableau[j]:
                j=k
            k=k+1
        tableau[i],tableau[j] = tableau[j],tableau[i]
        i=i+1
    return tableau

def mesure_tri(fct,n=100):
    
    tps = 0
    nb = 1
    for _ in range(nb):
        # on crée un tableau de dimension n
        t = [randint(0,10000) for _ in range(n)]

        # relevé du temps initial
        t_0 = time()

        eval(fct)

        # relevé du temps final
        t_1 = time()

        tps = tps + (t_1-t_0)
        
    return tps/nb


dimension_tableau = []
temps_tri_fusion = []
temps_tri_selection = []

for i in range(1,16):
    dim = i* 1000
    dimension_tableau.append(dim)
    
    # mesure du temps exécution tri fusion
    t = round(mesure_tri("tri_fusion(t)",dim),5)
    temps_tri_fusion.append(t)
    
    # mesure temps exécution tri selection
    t = round(mesure_tri("tri_selection(t)",dim),5)
    temps_tri_selection.append(t)
    
    
n_log_n = [n*log2(n)/2000000 for n in [i*1000 for i in range(1,16)]]

pyplot.plot(dimension_tableau,temps_tri_fusion)
pyplot.plot(dimension_tableau,temps_tri_selection,c='red')
pyplot.plot([i*1000 for i in range(1,16)],n_log_n)
pyplot.show()