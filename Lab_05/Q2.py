maze = [
    [0, 0, 0, 0],
    [0, 1, 0, 1],
    [0, 0, 0, 0],
    [0, 1, 0, 0]
]
start = (0,0)
goal = (3,3)

edge_costs = {}
for r in range(len(maze)):
    for c in range(len(maze[0])):
        if maze[r][c] == 0:
            for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                nr, nc = r+dr, c+dc
                if 0 <= nr < len(maze) and 0 <= nc < len(maze[0]) and maze[nr][nc]==0:
                    edge_costs[((r,c),(nr,nc))] = 1

def heuristic(a,b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def simple_dynamic_a_star(start, goal):
    open_list = [(start, heuristic(start, goal))]
    came_from = {}
    g_score = {start: 0}
    visited = []

    step = 0
    while open_list:
        open_list.sort(key=lambda x: x[1])
        current, f = open_list.pop(0)
        visited.append(current)

        if current == goal:
            path = [current]
            while current in came_from:
                current = came_from[current]
                path.append(current)
            return path[::-1]
        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            neighbor = (current[0]+dr, current[1]+dc)
            if 0 <= neighbor[0] < len(maze) and 0 <= neighbor[1] < len(maze[0]) and maze[neighbor[0]][neighbor[1]]==0:
                cost = edge_costs.get((current, neighbor), 1)
                tentative_g = g_score[current] + cost
                if neighbor not in g_score or tentative_g < g_score[neighbor]:
                    g_score[neighbor] = tentative_g
                    f_score = tentative_g + heuristic(neighbor, goal)
                    came_from[neighbor] = current
                    if neighbor not in visited:
                        open_list.append((neighbor, f_score))
        step += 1
        if step == 3:
            edge_costs[((0,1),(0,2))] = 5  
        if step == 5:
            edge_costs[((2,1),(2,2))] = 4

    return None

path = simple_dynamic_a_star(start, goal)
print("A* path:")
print(path)
