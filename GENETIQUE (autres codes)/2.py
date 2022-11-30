
import random as rdm
def calcul_conflit(tab):
    nbre_conflit=0;
    for i in range(0,8):
        for j in range (0,8):
            #s'il y'a conflit sur la colonne, incremente le nombre de conflit
            if i!=j and tab[i]==tab[j]:
                nbre_conflit=nbre_conflit+1;
            #s'il y'a conflit sur la diagonal, incremente le nombre de conflit    
            elif i!=j and valeur_absolue(tab[i],tab[j])==valeur_absolue(i,j):
                nbre_conflit=nbre_conflit+1;

    return nbre_conflit 

# valeur absolue
def valeur_absolue(a,b):
    if a-b>0:
        return a-b
    else:
        return b-a

# Liste de la generation de depart
def premiereGeneration():
    G=[]
    g1=rdm.sample(range(1, 9), 8)
    g2=rdm.sample(range(1, 9), 8)
    g3=rdm.sample(range(1, 9), 8)
    g4=rdm.sample(range(1, 9), 8)
    G.append(g1)
    G.append(g2)
    G.append(g3)
    G.append(g4)
    return G



# Fonction de permutation
def permute(p):
    p[0], p[1] = p[1], p[0]
    return p

# Fonction split pour sciender les elemenent en deux groupes
def split(n):
    l = []
    n1 = n[:4]
    n2 = n[4:]
    l.append(n1)
    l.append(n2)
    return l

# Fonction pour couler deux elements les elements pour en faire un indivudus
def coller(n1, n2):
    n = n1 + n2
    return n


# Fonction qui obtient une grande population
def populationPlus(tab):
    k = 0
    population = []
    for a in tab:
        population.append([a, calcul_conflit(a)])
    for i in tab:
        k = k + 1
        for j in tab[k:]:
            
            e1 = coller(split(i)[0], split(j)[1])
            r = rdm.randrange(0,2)
            if r == 0:
                e1 = permute(e1)

            e2 = coller(split(j)[0], split(i)[1])
            r = rdm.randrange(0,2)
            if r == 0:
                e2 = permute(e2)

            population.append([e1,calcul_conflit(e1)])
            population.append([e2,calcul_conflit(e2)])
    return population

# creer une nouvelle population
def nouvelleListe(population):
    pris = []
    n_l2 = population
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


# LE PROGRAMME PRINCIPAL 
def genetique():
    liste = premiereGeneration()
    it = 0
    for i in range(250):
        it = it +1
        population = populationPlus(liste)
        nouvelle_liste = nouvelleListe(population)
        liste = nouvelle_liste
 
    print("la derniere population est ")
    for i in liste:
        print(i," son conflit est: ",calcul_conflit(i))

genetique()

