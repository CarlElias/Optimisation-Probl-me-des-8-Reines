# KONE KORONAN / KOUADIO YANN FREDDY MASTER INFO 1 A (Algorithme génétique appliqué au probleme des huits reines)

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
def newreine(t):
    q=[]
    for i in range(len(t)):
        q.append(rd.randrange(1,len(t)+1))
    return q
        
    

# t=[2,4,3,6,5,7,7,1]
# print(conflit(t))

s=[2,4,3,6,5,7,7,1]
T=1000
epsi=0.01
alpha=0.01
n=0
V=[]
while(T>epsi):
    V.append(s)
    if(conflit(s)==0):
        print(s)
        break
    sn=newreine(s)
    Df=conflit(sn)-conflit(s)
    if(Df<=0):
        s=sn
    else:
        a=exp(-Df/T)
        p=rd.randrange(0,11)/10
        T=T-alpha
        if(p<=a):
            s=sn
        else:
            n+=1
# conf=[]
# for i in range(len(V)):
#     conf.append(conflit(V[i]))
# print(min(conf),V[conf.index(min(conf))])
#             