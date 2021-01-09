# Have not done discrete math in 6 years, so it will be sloppy

import random


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


graph = graph2

# Initially setting all distances as infinite and distance to the origin node as 0
dijkstra = [float('inf') for node in graph] 
dijkstra[0] = 0

# Adding fist tnode to the visited nodes list and initializing with values of the edges from the first node
visited_nodes = [0]
for edge in range(len(graph[0])):
    if graph[0][edge] != 0:
        dijkstra[edge] = graph[0][edge]



# While there are nodes not visited, visit the node with the lowest value that has not been visited yet and update all the values of it edges following Dijkstra's algorithm
while len(visited_nodes) is not len(graph):
    lowest_node = dijkstra.index(sorted(dijkstra)[len(visited_nodes)])
    visited_nodes.append(lowest_node)
    for edge in range(len(graph[lowest_node])):
        if graph[lowest_node][edge] != 0 and dijkstra[edge] > dijkstra[lowest_node] + graph[lowest_node][edge]:
            dijkstra[edge] = dijkstra[lowest_node] + graph[lowest_node][edge]

# List with the minimum distance to each node
print(dijkstra)

