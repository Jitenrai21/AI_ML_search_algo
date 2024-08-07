graph = {
    "A" : ["B", "C"],
    "B" : ['D', 'E'],
    "C" : ["F"],
    "D" : [],
    "E" : [],
    "F" : []
}
print(graph)
def dfs (graph, start, visited = None):
    if (visited == None):
        visited = []
    visited.append(start)
    print(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
dfs(graph, "A")


