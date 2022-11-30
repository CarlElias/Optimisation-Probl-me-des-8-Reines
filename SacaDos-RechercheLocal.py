import random

nInitial = []
for k in range(7):nInitial.append(random.randint(1,8))

#function fitness
def fitness(n, C):
    resultat = 0 
    rem = C
    for _ in range(len(n)):
        if rem >= n[_]:
            rem = rem - n[_]
        else: 
            resultat += 1
            rem = C - n[_]
    
    return resultat

#fonction pour trouver le voisinage de nInitial
def Principal(tab):
    C = 10
    fitvois = []
    nbrVois = 3
    tab1 = tab
    #Voisinage & fitness de chaque voisin
    vois = [ [] for i in range(nbrVois)]
    for i in range(nbrVois):
        vois[i] = list(range(1,8))
        random.shuffle(vois[i])
        fitvois.append(fitness(vois[i], C))
    #index du conflit le plus faible      
    for i in range(nbrVois):
        m=fitvois
        m.index(min(fitvois))
    
    print(f'Soit un n possible : ', tab1 , ' de fitness : ',fitness(tab1, C))
    print ('On aura pour voisinage : ')
    print('\n'.join(map(str, vois)))
    print('Ayant respectivement pour conflit : ')
    print('\n'.join(map(str, fitvois))) 
                #msg1 va contenir le positionnement minimum
                #msg2 va contenir la valeur du positionnement minimum
    if (fitness(tab1, C) <= min(fitvois)) : 
        msg1 = tab1
        msg2 = fitness(tab1,C)
    else : 
        msg1 = vois[m.index(min(m))]
        msg2 = min(fitvois)
    print('========> On aura pour positionnement min : ',msg1, ' dont le conflit est de :', msg2, '\n')
    if ( msg2 == 0 ): 
        return print('')
    else: Principal(msg1)


C = 10
Principal(nInitial)
