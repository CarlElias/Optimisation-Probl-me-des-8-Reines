"CLASSE : MASTER 1 IABD"

"NOM : KONE BINTOU FINE"

import random as rm

# Fitness
def fitness(v):
    k1 = 0
    for i1 in range(0, 8):
        for j1 in range(0, 8):
            if i1 != j1:
                if v[i1] == v[j1]:
                    k1 = k1 + 1
    k2 = 0
    for i2 in range(0, 8):
        for j2 in range(0, 8):
            if i2 != j2:
                if abs(v[i2] - v[j2]) == abs(i2 - j2):
                    k2 = k2 + 1
    k = k1 + k2
    return k

# Liste de départ
def gener():
    p1 = rm.sample(range(1, 9), 8)
    p2 = rm.sample(range(1, 9), 8)
    p3 = rm.sample(range(1, 9), 8)
    p4 = rm.sample(range(1, 9), 8)
    p = [p1,p2,p3,p4]
    return p


# Fonction pour scinder
def scinde(n):
     l = []
     n1 = n[:4]
     n2 = n[4:]
     l.append(n1)
     l.append(n2)
     return l

# Fonction pour associer
def assoc(n1, n2):
    n = n1 + n2
    return n

# Fonction pour permuter
def permute(p):
    p[0], p[1] = p[1], p[0]
    return p

# Fonction qui obtient une grande population
def grandeListe(liste):
    k = 0
    grande_liste = []
    for i0 in liste:
        grande_liste.append([i0, fitness(i0)])
    for i in liste:
        k = k + 1
        for j in liste[k:]:
            e1 = assoc(scinde(i)[0], scinde(j)[1])
            r = rm.randrange(0,2)
            if r == 0:
                e1 = permute(e1)

            e2 = assoc(scinde(j)[0], scinde(i)[1])
            r = rm.randrange(0,2)
            if r == 0:
                e2 = permute(e2)

            grande_liste.append([e1,fitness(e1)])
            grande_liste.append([e2,fitness(e2)])
    return grande_liste

# Fonction qui crèe une nouvelle liste
def nouvelleListe(grande_liste):
    pris = []
    n_l2 = grande_liste
    nl2 = []
    while len(nl2) != 4:

        cout = []
        for m in n_l2:
            cout.append(m[1])
        minim = min(cout)
        for i in n_l2:
            if (i[1] == minim):
                if (i[1] in pris):
                    n_l2.remove(i)
                else:
                    n_l2.remove(i)
                    nl2.append(i[0])
                    pris.append(i[1])
    return nl2


# Corp
def main():
    liste = gener()
    it = 0
    for i in range(250):
        it = it +1
        grande_liste = grandeListe(liste)
        nouvelle_liste = nouvelleListe(grande_liste)
        liste = nouvelle_liste

    print("Voici la derniere population")
    for i in liste:
        print(i,fitness(i))

main()
