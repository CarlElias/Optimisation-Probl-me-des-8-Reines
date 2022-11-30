#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random as rm


# In[2]:


# Liste de départ
def creer_liste():
    p1 = rm.sample(range(1, 9), 8)
    p2 = rm.sample(range(1, 9), 8)
    p3 = rm.sample(range(1, 9), 8)
    p4 = rm.sample(range(1, 9), 8)
    p = [p1,p2,p3,p4]
    return p


# In[3]:


# Fonction qui permet de calculer le cout
def calculer_cout(v):
    k1 = 0
    for i1 in range(0, 8):
        for j1 in range(0, 8):
            if i1 != j1:
                if v[i1] == v[j1]:
                    k1 = k1 + 1
    k2 = 0
    for i2 in range(0, 8):
        for j2 in range(0, 8):
            if i2 != j2:
                if abs(v[i2] - v[j2]) == abs(i2 - j2):
                    k2 = k2 + 1
    k = k1 + k2
    return k


# In[4]:


# Fonction pour scinder
def scinder(n):
     l = []
     n1 = n[:4]
     n2 = n[4:]
     l.append(n1)
     l.append(n2)
     return l


# In[5]:


def permuter(p):
    p[0], p[1] = p[1], p[0]
    return p


# In[13]:


# Fonction pour associer
def associer(n1, n2):
    n = n1 + n2
    return n


# In[14]:


def grandeListe(liste):
    k = 0
    grande_liste = []
    for i0 in liste:
        grande_liste.append([i0, calculer_cout(i0)])
    for i in liste:
        k = k + 1
        for j in liste[k:]:
            e1 = associer(scinder(i)[0], scinder(j)[1])
            r = rm.randrange(0,2)
            if r == 0:
                e1 = permuter(e1)

            e2 = associer(scinder(j)[0], scinder(i)[1])
            r = rm.randrange(0,2)
            if r == 0:
                e2 = permuter(e2)

            grande_liste.append([e1,calculer_cout(e1)])
            grande_liste.append([e2,calculer_cout(e2)])
    return grande_liste


# In[15]:


def nouvelleListe(grande_liste):
    pris = []
    n_l2 = grande_liste
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


# In[16]:


def runApp():
    liste = creer_liste()
    it = 0
    for i in range(250):
        it = it +1
        grande_liste = grandeListe(liste)
        nouvelle_liste = nouvelleListe(grande_liste)
        liste = nouvelle_liste

    print("Voici la derniere population")
    for i in liste:
        print(i,calculer_cout(i))


# In[17]:


runApp()


# In[ ]:




