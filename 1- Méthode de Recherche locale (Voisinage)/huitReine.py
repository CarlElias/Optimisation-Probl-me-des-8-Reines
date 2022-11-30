#Donne un positionnement initial, Recherche des voisin et determine minimum jusqu'a ce que conflit=0


import random

# TableauEntr = [6, 4, 7, 3, 1, 2, 8, 5]
TableauEntr = []
for k in range(8):
    TableauEntr.append(random.randint(1,8))

#function pour calucler le conflit
def conflit(tab):
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
 
#fonction pour trouver le voisinage du TableauEntr
def voisinage(tab):
    confvois = []
    nbrVois = 3
    tab1 = tab
    #Voisinage & conflit de chaque voisin
    vois = [ [] for i in range(nbrVois)]
    for i in range(nbrVois):
        vois[i] = list(range(1,9))
        random.shuffle(vois[i])
        confvois.append(conflit(vois[i]))
    #index du conflit le plus faible      
    for i in range(nbrVois):
        m=confvois
        m.index(min(confvois))
    
    print(f'Soit un positionnement possible : ', tab1 , ' de conflit : ',conflit(tab1))
    print ('On aura pour voisinage : ')
    print('\n'.join(map(str, vois)))
    print('Ayant respectivement pour conflit : ')
    print('\n'.join(map(str, confvois))) 
                #msg1 va contenir le positionnement minimum
                #msg2 va contenir la valeur du positionnement minimum
    if (conflit(tab1) <= min(confvois)) : 
        msg1 = tab1
        msg2 = conflit(tab1)
    else : 
        msg1 = vois[m.index(min(m))]
        msg2 = min(confvois)
    print('========> On aura pour positionnement min : ',msg1, ' dont le conflit est de :', msg2, '\n')
    if ( msg2 == 0 ): 
        return print('')
    else: voisinage(msg1)



voisinage(TableauEntr)