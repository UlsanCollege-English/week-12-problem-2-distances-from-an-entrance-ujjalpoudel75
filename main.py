from collections import deque

def bfs_distances(graph, start):
    if start not in graph:
        return {}

    dist = {start: 0}
    queue = deque([start])

    while queue:
        node = queue.popleft()
        for neighbor in graph.get(node, []):
            if neighbor not in dist:
                dist[neighbor] = dist[node] + 1
                queue.append(neighbor)
    
    return dist
