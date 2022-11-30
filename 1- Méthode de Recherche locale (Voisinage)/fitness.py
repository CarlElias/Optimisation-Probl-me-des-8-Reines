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
    print(cmpt) 

individu = [8, 5, 7, 1, 8, 5, 3, 2]
conflit(individu)