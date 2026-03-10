deliveries = [
    ('A', 10),  
    ('B', 5),
    ('C', 8),
    ('D', 12)
]

distances = {
    ('A','B'): 4, ('A','C'): 2, ('A','D'): 7,
    ('B','C'): 1, ('B','D'): 5,
    ('C','D'): 3
}
for (a,b), d in list(distances.items()):
    distances[(b,a)] = d

def greedy_delivery_route(deliveries, distances, start='A'):
    unvisited = deliveries.copy()
    route = [start]
    current = start
    while unvisited:
        unvisited.sort(key=lambda x: (x[1], distances.get((current,x[0]), 100)))
        next_stop = unvisited.pop(0)[0]
        route.append(next_stop)
        current = next_stop
    return route

route = greedy_delivery_route(deliveries, distances)
print("Optimized delivery route: ")
print(route)
