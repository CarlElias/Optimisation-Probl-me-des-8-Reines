#Méthode TABOUS <--- Garder en mémoire une trace des differents minimum qu'on rencontre au cours du parcours des voisins
#Nom : SAHONIN BAYE CARL ELIAS SIMEON
import random
from math import exp

# TableauEntr = [6, 3, 5, 2, 8, 7, 4, 1]
SolIni = []
for k in range(8):
    SolIni.append(random.randint(1,8))

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
    listabou = [] 
    it = 0 # <-- Compteur d'itération
    nbrVois = 5 # <-- Nombre de voisin
    u = tab # u <-- Solution initial
    
    while (f(u) > 0) : 
        it += 1    
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
        
        print('************************* ITERATION ',it,' *************************')
        print(f'Soit un positionnement possible : ', u , ' de conflit : ',f(u))
        print ('On aura pour voisinage : \n')
        print ('Voisin                    |  Conflit')
        print ('--------------------------|------------')
        for i in ns:
            print(i," | ",f(i))
        print()
        if (f(u) <= f(v)): minf = f(u); minp = u; 
        else : minf = f(v); minp = v;
        
        print('le minimum est : ',minp , ' de conflit : ', minf)

        if ( f(v) < f(u) ) :
            listabou.append(v)
            print("==================> CRITERE D'ASPIRATION SATISFAIT \n \n")
            u = v
        else: 
            print("=========> CRITERE D'ASPIRATION NON SATISFAIT")
            print ("==================> RECHERCHE D'UN NOUVEAU MEILLEUR VOISIN \n \n")
        
    
    print('\n \n')
    print ('==========================< LISTE TABOUS >==========================')
    print()
    print ('              Element de la liste Tabous |  Conflit')
    print ('              ---------------------------|------------')
    for i in listabou:
        print("              ",i," | ",f(i))
    print()
    print('========> Solution optimal : ',u, ' dont le conflit est de :', f(u), '\n')

voisinage(SolIni)