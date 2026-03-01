graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}
def dls(graph, start, goal, depth_limit):
    visited = []
    def dfs(node, depth):
        visited.append(node)
        if node == goal:
            return visited
        if depth == depth_limit:
            visited.pop()
            return None
        neighbors = graph[node]
        i = 0
        while i < len(neighbors):
            if neighbors[i] not in visited:
                path = dfs(neighbors[i], depth + 1)
                if path:
                    return path
            i = i + 1
        visited.pop()
        return None
    result = dfs(start, 0)
    if result:
        print("DLS Goal Found. Path:", result)
    else:
        print("Goal not found within depth")
dls(graph, 'A', 'E', 2)
