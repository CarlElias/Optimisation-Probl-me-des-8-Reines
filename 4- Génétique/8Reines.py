#Génétique
    #Nom : SAHONIN BAYE CARL ELIAS SIMEON
    #Classe : MASTRER 1 IABD
import random

#function fitness
def f(tab):
    cmpt = 0
    #Verification colonne
    for i in range(8):
        for j in range(8):
            if ( (tab[i] == tab[j]) and (i != j) ):
                cmpt += 1
    #Verification Ligne           
    for i in range(8):
        for j in range(8):
            if ( ( abs(tab[i] - tab[j]) == abs(i-j) ) and (i != j) ):
                cmpt += 1
    return cmpt

#Fonction generer la population
def population_depart() :
    p = []
    while len(p) < 4 :
        p.append(random.sample(range(0,8), 8))
    return p

#Fonction pour scinder la liste en deux sous listes
def scinde(n):
     l = []
     n1 = n[:4] # La première partie de la liste
     n2 = n[4:] # La deuxième partie de la liste
     l.append(n1)
     l.append(n2)
     return l
 
#Fonction qui associe deux sous listes scindée en une liste
def assoc(n1, n2):
    n = n1 + n2
    return n

#Fonction qui permet de permuter les deux premiers éléments d'une liste
def permute(p):
    p[0], p[1] = p[1], p[0]
    return p

#Fonction qui permet de creer à partir de la population initiale une population generale (les differents enfants y compris)
def grandeListe(liste):
    k = 0
    grande_liste = []
    for i0 in liste:
        grande_liste.append([i0, f(i0)]) # On insere les 4 parents de la population initiale dans les 4 premières position de la grande liste
    for i in liste:
        k = k + 1
        for j in liste[k:]:
            e1 = assoc(scinde(i)[0], scinde(j)[1]) # On crèe un premier enfant provenat de la jointure des deux parents
            r = random.randrange(0,2) # On fait un tirage au sort pour savoir si l'enfant obtenu doit subir des modifications ou pas
            if r == 0:
                e1 = permute(e1)

            e2 = assoc(scinde(j)[0], scinde(i)[1]) # On crèe un deuxième enfant provenant de la jointure des deux parents
            r = random.randrange(0,2) # On fait un tirage au sort pour savoir si l'enfant obtenu doit subir des modifications ou pas
            if r == 0:
                e2 = permute(e2)

            grande_liste.append([e1,f(e1)]) # Ici on ajoute à la suite de la population initiale les enfants obtenus
            grande_liste.append([e2,f(e2)]) # Ici on ajoute à la suite de la population initiale les enfants obtenus
    return grande_liste

# Fonction qui crée une nouvelle population à partir de la population generale en se basant sur leurs fitness
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






liste = population_depart()
print("\nPopulation initiale:")
k0 = 0
for i in liste:
    k0 = k0 +1
    print("{}) {} avec un fitness de {}".format(k0,i,f(i)))

it = 0
nbrIt = int(input("\nNombre d'itération : "))
# On fait des itération ittération
for i in range(nbrIt):
    it = it +1
    print("\nPopulation obtenue à l'ittération N°",it)
    print("================================================================================")
    grande_liste = grandeListe(liste)
    nouvelle_liste = nouvelleListe(grande_liste)
    #population = nouvelle_liste
    popconf = []
    for j in nouvelle_liste:
        popconf.append(f(j))
        l = popconf
        m = l.index(min(popconf))
    
    k0 = 0
    for i in nouvelle_liste:
        k0 = k0 + 1
        print("{}) {} avec pour conflit {}".format(k0, i, f(i)))      
    
print("\n Le Meilleur Individu de la population à l'intération N°",nbrIt,' est : ', nouvelle_liste[m],"| ", f(nouvelle_liste[m]))
print('\n')
        