# KOUASSI YAO KAN
# ANOH KASSI JEAN-LUC
# DION ARMEL

import random as rand

# Calcule le nombre de conflits pour une configuration donnee des Reines
# @return : conflits, entier : le nombre de conflits trouves
# @param : 
#           liste, list : configuration des Reines
def conflit(liste):
    conflits=0
    for i in range(len(liste)):
        for j in range(len(liste)):
            if i == j:
                pass
            if liste[i] == liste[j]:
                conflits += 1
            if abs(liste[i] - liste[j]) == abs(i-j):
                conflits+=1
    return conflits

# Genere une nouvelle disposition des Reines
# @return : liste, list : disposition des Reines
# @param : 
#           n, entier : le nombre de lignes sur l'echiquier
def generer_nouvelle_liste(n):
    liste=[rand.randint(1,n+1) for i in range(n)]
    return liste

# Effectue un "croisement" de deux individus
# @return : list : liste de nouveaux individus
# @param : 
#           X;Y : list, induvidus parents
def croiser(X,Y):
    return [X[0:int(len(X)/2)]+Y[int(len(Y)/2):],Y[0:int(len(X)/2)]+X[int(len(Y)/2):]]

# Effectue une "mutation" d'un individu
# @return : list : un nouvel individu
# @param : 
#           X : list, induvidu mutant
def muter(X):
    x1=rand.randint(0,len(X)-1)
    x2=rand.randint(0,len(X)-1)
    if(conflit(X[:min(x1,x2)]+[X[max(x1,x2)]]+X[min(x1,x2)+1:max(x1,x2)]+[X[min(x1,x2)]]+X[max(x1,x2)+1:])<conflit(X) and x1!=x2):
        return X[:min(x1,x2)]+[X[max(x1,x2)]]+X[min(x1,x2)+1:max(x1,x2)]+[X[min(x1,x2)]]+X[max(x1,x2)+1:]
    else:
        return X

# Selectionne un individu
# @return : list : une nouvelle liste d'individus
# @param : 
#           X : list, induvidus
def selectionner(X):
    if(int(conflit(X)/2)>=10):
        return False
    return True

def selection(i):
    return [K[i],K[i+1]]

# Evalue un individu
# @return : list : un individus
# @param : 
#           X : list, induvidu a evaluer
def evaluer(x):        
    evaluation=dict()
    for i in range(57):
        evaluation[i]=[]
    for i in range(len(x)):
        evaluation[conflit(x[i])].append(x[i])
    K=[]
    for i in range(len(evaluation)):
        for j in range(len(evaluation[i])):
            K.append(evaluation[i][j])
    return [evaluation,K]   


# GENERATION D'UNE NOUVELLE POPULATION D'INDIVIDUS DE TAILLE n
n=20
x=[]
for i in range(n):
    index=generer_nouvelle_liste(8)
    if(not(index in x)):
        x.append(index)

fin=0
L=x
while(fin<250):
    evaluationx,K=evaluer(x)
    xprim=[]
    for i in range(0,len(K),2):
        a,b=selection(i)
        a,b=croiser(a,b)
        a,b=muter(a),muter(b)
        xprim.append(a)
        xprim.append(b)
        L.append(a)
        L.append(b)
    x=xprim
    fin+=1
t=True
evaluationx,x=evaluer(x)
print("\nSolution optimale : ",x[0],"\nNombre de conflits :",conflit(x[0]))
            
