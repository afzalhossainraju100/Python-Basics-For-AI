graph = {
    'KT': ['Fc', 'GG', 'AB3'],
    'Fc': ['M'],
    'M': ['T'],
    'GG': ['AB3'],
    'AB3': ['T'],
    'T': []
}

def dfs(graph, start, goal, path=None, visited=None):
    if path is None:
        path = [start]
    if visited is None:
        visited = set()
    
    visited.add(start)
    
    if start == goal:
        return path
    
    for neighbor in graph[start]:
        if neighbor not in visited:
            result = dfs(graph, neighbor, goal, path + [neighbor], visited)
            if result:
                return result
    return None


dfs_path = dfs(graph, 'KT', 'T')
print("DFS path:", dfs_path)