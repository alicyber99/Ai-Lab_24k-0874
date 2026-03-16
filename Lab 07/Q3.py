import random
import math

def dist(a,b):
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

def total(route, cities):
    d = 0
    for i in range(len(route)-1):
        d += dist(cities[route[i]], cities[route[i+1]])
    return d

def crossover(p1,p2):
    cut = random.randint(1,len(p1)-2)
    child = p1[:cut]
    for c in p2:
        if c not in child:
            child.append(c)
    return child

def mutate(route):
    i = random.randint(0,len(route)-1)
    j = random.randint(0,len(route)-1)
    route[i],route[j] = route[j],route[i]
    return route

cities = [(0,0),(2,3),(5,2),(6,6),(8,3),(1,7),(4,5),(7,2),(3,8),(9,5)]

pop = []
for i in range(20):
    r = list(range(10))
    random.shuffle(r)
    pop.append(r)

for g in range(100):

    pop.sort(key=lambda x: total(x,cities))
    new_pop = pop[:5]

    while len(new_pop) < 20:
        p1 = random.choice(pop[:10])
        p2 = random.choice(pop[:10])
        child = crossover(p1,p2)

        if random.random() < 0.3:
            child = mutate(child)
        new_pop.append(child)

    pop = new_pop


best = pop[0]

print("Best Route:", best)
print("Distance:", total(best,cities))
