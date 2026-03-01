graph_cost = {
    'A': {'B': 2, 'C': 1},
    'B': {'D': 4, 'E': 3},
    'C': {'F': 1},
    'D': {},
    'E': {},
    'F': {}
}
def ucs(graph, start, goal):

    frontier = []
    frontier.append([start, 0]) 
    visited = []
    parent = {}
    parent[start] = None
    while len(frontier) > 0:
        min_index = 0
        i = 1

        while i < len(frontier):
            if frontier[i][1] < frontier[min_index][1]:
                min_index = i
            i = i + 1

        current = frontier[min_index][0]
        current_cost = frontier[min_index][1]
        frontier.pop(min_index)
        if current in visited:
            continue
        visited.append(current)
        if current == goal:
            path = []
            node = current
            while node != None:
                path.append(node)
                node = parent[node]
            left = 0
            right = len(path) - 1
            while left < right:
                temp = path[left]
                path[left] = path[right]
                path[right] = temp
                left = left + 1
                right = right - 1

            print("UCS Goal Found")
            print("Path:", path)
            print("Total Cost:", current_cost)
            return
        neighbors = graph[current]
        for neighbor in neighbors:
            if neighbor not in visited:
                new_cost = current_cost + neighbors[neighbor]
                frontier.append([neighbor, new_cost])
                if neighbor not in parent:
                    parent[neighbor] = current
    print("Goal not found")
ucs(graph_cost, 'A', 'E')