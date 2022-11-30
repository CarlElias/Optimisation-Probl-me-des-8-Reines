#---------------------------------------------------------
# Coded by Pondo Kouakou Alexis and Fofana Naminata Nafi #
#---------------------------------------------------------



# Importer la bibliothèque random
import random as rm

# La fonction fitness qui represente ici le cout(colision)
######################################################################################################
def fitness(v):
    # Colision de façcon verticale
    k1 = 0
    for i1 in range(0, 8):
        for j1 in range(0, 8):
            if i1 != j1:
                if v[i1] == v[j1]:
                    k1 = k1 + 1

    # Colision sur la diagonale
    k2 = 0
    for i2 in range(0, 8):
        for j2 in range(0, 8):
            if i2 != j2:
                if abs(v[i2] - v[j2]) == abs(i2 - j2):
                    k2 = k2 + 1
    k = k1 + k2
    return k
######################################################################################################


# On genere de façon aléatoire une population de depart composé de 4 individus
######################################################################################################
def population_depart():
    p1 = rm.sample(range(1, 9), 8)
    p2 = rm.sample(range(1, 9), 8)
    p3 = rm.sample(range(1, 9), 8)
    p4 = rm.sample(range(1, 9), 8)
    p = [p1,p2,p3,p4]
    return p
######################################################################################################


# Fonction pour scinder la liste en deux sous listes
######################################################################################################
def scinde(n):
     l = []
     n1 = n[:4] # La première partie de la liste
     n2 = n[4:] # La deuxième partie de la liste
     l.append(n1)
     l.append(n2)
     return l
######################################################################################################


# Fonction qui associe deux sous listes scindée en une liste
######################################################################################################
def assoc(n1, n2):
    n = n1 + n2
    return n
######################################################################################################


# Fonction qui permet de permuter les deux premiers éléments d'une liste
######################################################################################################
def permute(p):
    p[0], p[1] = p[1], p[0]
    return p
######################################################################################################


# Fonction qui permet de creer à partir de la population initiale une population generale (les differents enfants y compris)
######################################################################################################
def grandeListe(liste):
    k = 0
    grande_liste = []
    for i0 in liste:
        grande_liste.append([i0, fitness(i0)]) # On insere les 4 parents de la population initiale dans les 4 premières position de la grande liste
    for i in liste:
        k = k + 1
        for j in liste[k:]:
            e1 = assoc(scinde(i)[0], scinde(j)[1]) # On crèe un premier enfant provenat de la jointure des deux parents
            r = rm.randrange(0,2) # On fait un tirage au sort pour savoir si l'enfant obtenu doit subir des modifications ou pas
            if r == 0:
                e1 = permute(e1)

            e2 = assoc(scinde(j)[0], scinde(i)[1]) # On crèe un deuxième enfant provenant de la jointure des deux parents
            r = rm.randrange(0,2) # On fait un tirage au sort pour savoir si l'enfant obtenu doit subir des modifications ou pas
            if r == 0:
                e2 = permute(e2)

            grande_liste.append([e1,fitness(e1)]) # Ici on ajoute à la suite de la population initiale les enfants obtenus
            grande_liste.append([e2,fitness(e2)]) # Ici on ajoute à la suite de la population initiale les enfants obtenus
    return grande_liste
######################################################################################################


# Fonction qui crée une nouvelle population à partir de la population generale en se basant sur leurs fitness
######################################################################################################
def nouvelleListe(grande_liste):
    pris = []
    nouvelle_liste = []

    # crée une nouvelle population à partir de la population generale en se basant sur leurs fitness
    while len(nouvelle_liste) != 4:
        cout = []
        for m in grande_liste:
            cout.append(m[1])
        minim = min(cout)
        for i in grande_liste:
            if (i[1] == minim):
                if (i[1] in pris):
                    grande_liste.remove(i)
                else:
                    grande_liste.remove(i)
                    nouvelle_liste.append(i[0])
                    pris.append(i[1])
    return nouvelle_liste
######################################################################################################


# Corps du programme
######################################################################################################
def main():
    liste = population_depart()
    print("\nPopulation initiale:")
    k0 = 0
    for i in liste:
        k0 = k0 +1
        print("{}) {} avec un fitness de {}".format(k0,i,fitness(i)))

    it = 0
    # On fait 250 ittération
    for i in range(250):
        it = it +1
        print("\nIttération n°{}".format(it))
        print("======================================================================================================================")
        grande_liste = grandeListe(liste)
        nouvelle_liste = nouvelleListe(grande_liste)

        k0 = 0
        for i in nouvelle_liste:
            k0 = k0 + 1
            print("{}) {} avec un fitness de {}".format(k0, i, fitness(i)))
######################################################################################################

# Appel du programme
main()
