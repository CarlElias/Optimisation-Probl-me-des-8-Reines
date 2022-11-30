import random as rdm
import copy

# fitness
def fitn(v):
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
    p1 = rdm.sample(range(1, 9), 8)
    p2 = rdm.sample(range(1, 9), 8)
    p3 = rdm.sample(range(1, 9), 8)
    p4 = rdm.sample(range(1, 9), 8)
    p = [p1,p2,p3,p4]
    return p


# Fonction pour scindé
def scin(n):
     l = []
     n1 = n[:4]
     n2 = n[4:]
     l.append(n1)
     l.append(n2)
     return l

# associer
def asso(n1, n2):
    n = n1 + n2
    return n

# perdmuter
def perdmute(p):
    p[0], p[1] = p[1], p[0]
    return p

# Fonction qui obtient une grande population
def gListe(liste):
    k = 0
    g_liste = []
    for i0 in liste:
        g_liste.append([i0, fitn(i0)])
    for i in liste:
        k = k + 1
        for j in liste[k:]:
            e1 = asso(scin(i)[0], scin(j)[1])
            r = rdm.randrange(0,2)
            if r == 0:
                e1 = perdmute(e1)

            e2 = asso(scin(j)[0], scin(i)[1])
            r = rdm.randrange(0,2)
            if r == 0:
                e2 = perdmute(e2)

            g_liste.append([e1,fitn(e1)])
            g_liste.append([e2,fitn(e2)])
    return g_liste

#nouvelle liste
def new_Liste(g_liste):
    pris = []
    n_l2 = g_liste
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


# Fonction principale
def main():
    liste = gener()
    it = 0
    for i in range(250):
        it = it +1
        g_liste = gListe(liste)
        newListe = new_Liste(g_liste)
        liste = newListe

    print("Derniere population")
    for i in liste:
        print(i,fitn(i))

main()
