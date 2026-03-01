tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H'],
    'E': [],
    'F': ['I'],
    'G': [],
    'H': [],
    'I': []
}
def dls_Id(tree, node, goal, depth):
    if node == goal:
        return [node]
    if depth == 0:
        return None
    neighbors = tree[node]
    i = 0
    while i < len(neighbors):
        path = dls_Id(tree, neighbors[i], goal, depth - 1)
        if path:
            return [node] + path
        i = i + 1
    return None

def iddfs(tree, start, goal, max_depth):
    depth = 0
    while depth <= max_depth:
        print("Checking Depth:", depth)
        result = dls_Id(tree, start, goal, depth)
        if result:
            print("Goal found with IDDFS")
            print("Path:", result)
            return
        depth = depth + 1
    print("Goal not found")
iddfs(tree, 'A', 'I', 5)