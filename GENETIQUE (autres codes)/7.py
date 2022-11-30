#*******#
# * BAKAYOKO Mouan Aude Olivia
# * KOUAKOU Kouadio Aristide
# * Classe  : Master 1 Info A
#*******#

### Utilise pour generer la solution initiale de facon aleatoire
from random import *
import math

### Utils
def combin (n, k) :
    if k > n//2 :
        k = n - k
    x = 1
    y = 1
    i = n - k + 1
    while i <= n :
        x = (x*i)//y
        y += 1
        i += 1
    return x

#Fonction generer la population
def N(taille_population) :
    population = []
    while len(population) < taille_population :
        population.append(sample(range(0,8), 8))

    return population

### Fonction fitness
def fitness(s) :
    cost = 0 
    
    for i in range(len(s)) :
        for j in range(len(s)) :
            if j != i and s[j] == s[i] :
                cost += 1
    
    for i in range(len(s)) :
        for j in range(len(s)) :
            if j != i and abs(s[j] - s[i]) == abs(j - i) :
                cost += 1
    return cost


### Fonction reproduction : pour coupler deux chromosomes
def reproduction(chromosome_1, chromosome_2, niveau_division) :
   
    fils_1 = chromosome_1[0:niveau_division]+chromosome_2[niveau_division:]
    fils_2 = chromosome_2[0:niveau_division]+chromosome_1[niveau_division:]
 
    # Mutation eventuelle
    r = random()
    if(r <= 0.5) :
        temp = fils_2[7]
        fils_2[7] = fils_2[2]
        fils_2[2] = temp
    
    return fils_1, fils_2

def nouvelle_population(population_mere,list_enfants, list_fitness, taille_population) :
    nouvelle_pop = []
    # -  Ordonnez les fitness dans l'ordre croissant 
    temp = list_fitness
    temp.sort()
    temp = list(set(temp))

    # -- Formation de la population
    
    if len(temp) < taille_population :
        for i in temp[:len(temp)] :

            nouvelle_pop.append(list_enfants[list_fitness.index(i)])
        for i in range(len(temp), taille_population) :
            nouvelle_pop.append(population_mere[i])
    else :
        for i in temp[:taille_population] :

            nouvelle_pop.append(list_enfants[list_fitness.index(i)])

    return nouvelle_pop
    
    


### Fonction main
def main():
    nombre_iterations = 0
    taille_population = 5
    continuer = True
   # 1- Generer une population aleatoire
    population = N(taille_population)
    
    while continuer :
        list_fitness = []
        list_enfants = []
       
        #reproduction
        for j in range(0, combin(taille_population, 2)) :
            for k in range(j +1 , taille_population) :
                fils_1, fils_2 = reproduction(population[j],population[k],niveau_division = 5)
                list_enfants.append(fils_1)
                list_enfants.append(fils_2)
        
        # Calcul de fitness
        for i in range(0, len(list_enfants)) : 
            list_fitness.append(fitness(list_enfants[i]))
            
        #choix des enfants meilleurs
        population = nouvelle_population(population, list_enfants, list_fitness, taille_population)
        
        #condition d'arret
        if nombre_iterations == 200 :
            continuer = False
        
        nombre_iterations += 1 
    
    
    print('Le meilleur chromosome est : ' + str(population[0]) + ' Fitness : '+str(fitness(population[0])))



    

#Execution de l'algorithme
main()
                


