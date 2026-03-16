def dist(a,b):
    return ((a[0]-b[0])**2 + (a[1]-b[1])**2) ** 0.5

def total(route):
    d = 0
    for i in range(len(route)-1):
        d = d + dist(route[i], route[i+1])
    return d

def hill(points):

    route = points[:]
    best = total(route)

    for i in range(len(route)):
        for j in range(i+1, len(route)):

            new = route[:]
            new[i], new[j] = new[j], new[i]

            if total(new) < best:
                route = new
                best = total(new)

    return route, best


points = [(0,0),(2,3),(5,2),(6,6)]

r,d = hill(points)
print("Best Route:", r)
print("Total Distance:", d)
