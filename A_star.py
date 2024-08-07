import heapq
# graph = {
#     'A' : [('B',1), ('C',2)],
#     'B' : [('D',3), ('E',2)],
#     'C' : [('F',2)],
#     'D' : [],
#     'E' : [('F',1)],
#     'F' : []
# }
graph = {
    'A' : [('B',1), ('C',3)],
    'B' : [('D',3),('C', 5), ('F', 4)],
    'C' : [('E',2), ('F', 1)],
    'D' : [('F',2)],
    'E' : [('F',1)],
    'F' : []
}
heuristic = {
    'A' : 7,
    'B' : 9,
    'C' : 8,
    'D' : 6,
    'E' : 0,
    'F' : 0
}


def a_star_search(graph, start, goal, heuristic, costs):
    pq = []
    heapq.heappush(pq, (heuristic[start], 0, start))
    visited = set()
    came_from = {start : None}
    g_costs = {start : 0}

    while pq:
        _, current_g, current = heapq.heappop(pq)
        if current in visited:
            continue
        visited.add(current)
        if current==goal:
            path = []
            while current:
                path.append(current)
                current = came_from[current]
            return path[::-1]
        
        for neighbour, cost in graph[current]:
            if neighbour in visited:
                continue
            new_g = current_g + cost
            if neighbour not in g_costs or new_g < g_costs[neighbour]:
                g_costs[neighbour] = new_g
                f = new_g + heuristic[neighbour]
                came_from[neighbour] = current
                heapq.heappush(pq,(f,new_g, neighbour))
    return None


path = a_star_search(graph, 'A', 'F', heuristic, graph)
print(path)