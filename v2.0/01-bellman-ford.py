# Have not done discrete math in 6 years, so it will be sloppy

# Graph representation is an adjacency matrix with weights.  For convenience (lazyness), the first node is always the origin
graph1 = [[0, 5, 0, 0, 3],
         [5, 0, 1, 1, 1],
         [0, 1, 0, 2, 0],
         [0, 1, 2, 0, 1],
         [3, 1, 0, 1, 0]]


graph2 = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
        [4, 0, 8, 0, 0, 0, 0, 11, 0],
        [0, 8, 0, 7, 0, 4, 0, 0, 2],
        [0, 0, 7, 0, 9, 14, 0, 0, 0],
        [0, 0, 0, 9, 0, 10, 0, 0, 0],
        [0, 0, 4, 14, 10, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 1, 6],
        [8, 11, 0, 0, 0, 0, 1, 0, 7],
        [0, 0, 2, 0, 0, 0, 6, 7, 0]
        ];

graph_neg = [[0, 1, 0, 0, 0, 0],
             [1, 0, 3, 2, 2, 0],
             [0, 3, 0, 2, 0, 0],
             [0, 2, 2, 0, -3, 2],
             [0, 2, 0, -3, 0, 0],
             [0, 0, 0, 0, 2, 0]]

graph = graph1


# Initializing the diferent elements of dist to infinite and the first one to 0
dist = [float('inf') for node in graph]
dist[0] = 0

# First part of the Bellman-Ford algorithm. Visit each edge of each node N-1 times and assign the lowest distance value
for i in range(len(graph)-1):
    for node in range(len(graph)):
        for edge in range(len(graph[node])):
            if graph[node][edge] and dist[edge] > dist[node] + graph[node][edge]:
                dist[edge] = dist[node] + graph[node][edge]

# Second part of the Bellman-Ford algorithm. Check if there are negative cycles
for node in range(len(graph)):
    for edge in range(len(graph[node])):
        if graph[node][edge] and dist[edge] > dist[node] + graph[node][edge]:
            print('There are negative cycles on the graph')
            exit(0)

# Print distances
print (dist)
