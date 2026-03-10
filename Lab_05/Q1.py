class Node:
    def __init__(self, position, parent=None):
        self.position = position
        self.parent = parent
        self.h = 0  
    def __lt__(self, other):
        return self.h < other.h  

def heuristic(pos, goals):
    return min(abs(pos[0]-g[0]) + abs(pos[1]-g[1]) for g in goals)

def best_First_Search_Multi_Goal(maze, start, goals):
    rows, cols = len(maze), len(maze[0])
    current_position = start
    full_path = [start] 

    remaining_goals = goals.copy()

    while remaining_goals:
        frontier = [Node(current_position)]
        visited = set()

        while frontier:
            frontier.sort(key=lambda n: n.h)
            current_node = frontier.pop(0)
            pos = current_node.position
            if pos in visited:
                continue
            visited.add(pos)

            if pos in remaining_goals:
                path = []
                while current_node:
                    path.append(current_node.position)
                    current_node = current_node.parent
                path = path[::-1]
                full_path += path[1:]
                current_position = pos
                remaining_goals.remove(pos)
                break

            for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                nr, nc = pos[0]+dx, pos[1]+dy
                if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc]==0 and (nr,nc) not in visited:
                    new_node = Node((nr,nc), current_node)
                    new_node.h = heuristic((nr,nc), remaining_goals)
                    frontier.append(new_node)

    return full_path

maze = [
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 1],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0]
]
start = (0, 0)
goals = [(4,4), (2,3), (0,4)] 

path = best_First_Search_Multi_Goal(maze, start, goals)
print("Path visiting all goals:")
print(path)
