def conflit(t):
    a=0
    for i in range(len(t)):
        for j in range(len(t)):
            if(t[i]==t[j] and i!=j):
                a+=1
            if(abs(t[i]-t[j])==abs(i-j) and i!=j):
                a+=1
    return a

import random as rd
from math import *
def newreine(n):
    q=[]
    for i in range(n):
        q.append(rd.randrange(1,n+1))
    return q

def croiser(X,Y):
    return [X[0:int(len(X)/2)]+Y[int(len(Y)/2):],Y[0:int(len(X)/2)]+X[int(len(Y)/2):]]

def mutation(X):
    x1=rd.randint(0,len(X)-1)
    x2=rd.randint(0,len(X)-1)
    if(conflit(X[:min(x1,x2)]+[X[max(x1,x2)]]+X[min(x1,x2)+1:max(x1,x2)]+[X[min(x1,x2)]]+X[max(x1,x2)+1:])<conflit(X) and x1!=x2):
        return X[:min(x1,x2)]+[X[max(x1,x2)]]+X[min(x1,x2)+1:max(x1,x2)]+[X[min(x1,x2)]]+X[max(x1,x2)+1:]
    else:
        return X


def selectionner(X):
    if(int(conflit(X)/2)>=10):
        return False
    return True

def selection(i):
    return [K[i],K[i+1]]

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

# GENERATION D'UNE POPULATION D'INDIVIDUS DE TAILLE n
n=20
x=[]
for i in range(n):
    ind=newreine(8)
    if(not(ind in x)):
        x.append(ind)

term=0
L=x
while(term<100):
    evaluationx,K=evaluer(x)
    xprim=[]
    for i in range(0,len(K),2):
        a,b=selection(i)
        a,b=croiser(a,b)
        a,b=mutation(a),mutation(b)
        xprim.append(a)
        xprim.append(b)
        L.append(a)
        L.append(b)
    x=xprim
    term=term+1
t=True
evaluationx,x=evaluer(x)
print("\nLa solution optimale est : x =",x[0],"et son nombre de conflits est :",conflit(x[0]))
            
