from random import randint

# 1. Boucle while avec test AND

def fusion(liste1,liste2):
    liste_fusionne = []
    i1 = 0
    i2 = 0
    while i1 < len(liste1) and i2 < len(liste2):
        if liste1[i1] < liste2[i2]:
            liste_fusionne.append(liste1[i1])
            i1 += 1
        else:
            liste_fusionne.append(liste2[i2])
            i2 += 1
    while i1 < len(liste1):
        liste_fusionne.append(liste1[i1])
        i1 += 1 
    while i2 < len(liste2):
        liste_fusionne.append(liste2[i2])
        i2 += 1
    return liste_fusionne

def tri_fusion(liste):
    if len(liste)<2:
        return liste
    else:
        liste1=tri_fusion(liste[0:len(liste)//2])
        liste2=tri_fusion(liste[len(liste)//2:len(liste)])
        return fusion(liste1,liste2)

if __name__ == '__main__':
    t=[randint(-1000,1000) for i in range(20)]
    # fusion([1,5,9,13],[2,3,5,7,10,11,12])
    tri_fusion(t)