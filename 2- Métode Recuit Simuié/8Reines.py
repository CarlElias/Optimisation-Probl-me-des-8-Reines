#Recuit Simiulé
#Nom : SAHONIN BAYE CARL ELIAS SIMEON
import random
from math import exp

# TableauEntr = [6, 3, 5, 2, 8, 7, 4, 1]
TableauEntr = []
for k in range(8):
    TableauEntr.append(random.randint(1,8))

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

def voisinage(tab):
    e = 10**(-3)
    t = 300
    cool = 0.995
    nbrVois = 5 # <-- Nombre de voisin
    u = tab # u <-- Solution initial
    while (t > e) : 
        confns = [] # <-- Liste contenant la valeur des conflits respective de ns
        #Voisinage & conflit de chaque voisin
        ns = [ [] for i in range(nbrVois)]
        for i in range(nbrVois):
            ns[i] = list(range(1,9))
            random.shuffle(ns[i])
            confns.append(f(ns[i]))
        #index du conflit le plus faible      
        for i in range(nbrVois):
            m=confns
            m.index(min(confns))
        v = ns[m.index(min(m))]
        
        print(f'Soit un positionnement possible : ', u , ' de conflit : ',f(u))
        print ('On aura pour voisinage : ')
        print('\n'.join(map(str, ns)))
        print('Ayant respectivement pour conflit : ')
        print('\n'.join(map(str, confns))) 
        print('le voisin minimum est : ',v , ' de conflit : ', f(v),' \n')
        
        #Application du recuit simulé
        if ( f(v) < f(u) ): 
            u = v 
        else: 
            r = random.randint(0,1)
            if r < exp( (f(u)-f(v))/t ): 
                u = v
        t = t*cool
        
        # if (f(u) == 0) : break
        
    print('========> On aura pour positionnement min : ',u, ' dont le conflit est de :', f(u), '\n')
    
voisinage(TableauEntr)