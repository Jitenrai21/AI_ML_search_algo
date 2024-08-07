import heapq
graph = {
    'A' : ['B', 'C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}
heuritic = {
    'A' : 7,
    'B' : 9,
    'C' : 8,
    'D' : 6,
    'E' : 0,
    'F' : 0
}
def best_first_search(graph, start, goal, heuristic):
    pq = []
    heapq.heappush(pq, (heuristic[start], start))
    visited = set()
    came = {start: None}
    while pq:
        a, current = heapq.heappop(pq)
        if current in visited:
            continue
        visited.add(current)
        if current== goal:
            path = []
            while current:
                path.append(current)
                current = came[current]
            return path[::-1]
        for neighbour in graph[current]:
            if neighbour not in visited:
                came[neighbour] = current
                heapq.heappush(pq, (heuritic[neighbour], neighbour))
    return None
print(best_first_search(graph,'A','F',heuritic))
