graph = {
    'KT': ['Fc', 'GG', 'AB3'],
    'Fc': ['M'],
    'M': ['T'],
    'GG': ['AB3'],
    'AB3': ['T'],
    'T': []
}

def bfs(graph, start, goal):
    queue = [(start, [start])]  # (node, path)
    visited = set()
    
    while queue:
        node, path = queue.pop(0)
        if node == goal:
            return path
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                queue.append((neighbor, path + [neighbor]))
    return None

bfs_path = bfs(graph, 'KT', 'T')

print("BFS path:", bfs_path)