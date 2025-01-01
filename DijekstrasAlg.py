""" 05.04.2024
Yahya Shafique
Dijkstra's algorithm - shortest path

"""

def createGraph():
    
    graph = {
        "A": {"B": 1, "C": 4, "D": 2},
        "B": {"A": 9, "E": 5},
        "C": {"A": 4, "F": 15},
        "D": {"A": 10, "F": 7},
        "E": {"B": 3, "J": 7},
        "F": {"C": 11, "D": 14, "K": 3, "G": 9},
        "G": {"F": 12, "I": 4},
        "H": {"J": 13},
        "I": {"G": 6, "J": 7},
        "J": {"H": 2, "I": 4},
        "K": {"F": 6}
    }
    return graph

def dijkstra(graph, startVertex):
    
    shortestPaths = {}
    predecessors = {}
    unvisited = graph.copy()
    infinity = float('inf')

    for vertex in unvisited:
        shortestPaths[vertex] = infinity
    shortestPaths[startVertex] = 0

    while unvisited:
        minVertex = None
        for vertex in unvisited:
            if minVertex is None:
                minVertex = vertex
            elif shortestPaths[vertex] < shortestPaths[minVertex]:
                minVertex = vertex

        for adjacentVertex, weight in graph[minVertex].items():
            if weight + shortestPaths[minVertex] < shortestPaths[adjacentVertex]:
                shortestPaths[adjacentVertex] = weight + shortestPaths[minVertex]
                predecessors[adjacentVertex] = minVertex
        unvisited.pop(minVertex)

    return predecessors, shortestPaths

def getShortestPath(predecessors, start, end):
    
    path = []
    vertex = end
    while vertex != start:
        path.insert(0, vertex)
        vertex = predecessors[vertex]
    path.insert(0, start)
    return path


if __name__ == "__main__":
    graph = createGraph()
    print("Graph dictionary:")
    for vertex, edges in graph.items():
        print(f"{vertex}: {edges}")
    print("\nStarting Dijkstra's Algorithm...")

    start = "A"
    end = "H"
    predecessors, shortestPathInfo = dijkstra(graph, start)
    path = getShortestPath(predecessors, start, end)
    print(f"\nThe shortest path from {start} to {end} is: {' -> '.join(path)} with distance {shortestPathInfo[end]}")
