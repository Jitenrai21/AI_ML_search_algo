from collections import deque

graph = {
    'A' : ['B', 'C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}

def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue :
        vertex = queue.popleft()
        if vertex not in visited:
            print(vertex)
            visited.add(vertex)
            for i in graph:
                if i not in visited:
                    queue.extend(i)
bfs(graph, "A")