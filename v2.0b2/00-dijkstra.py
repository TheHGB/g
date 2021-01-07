# Have not done discrete math in 6 years, so it will be sloppy

import random


# Graph representation is an adjacency matrix with weights.  For convenience (lazyness), the first node is always the origin
graph = [[0, 5, 0, 0, 3],
         [5, 0, 1, 1, 1],
         [0, 1, 0, 2, 0],
         [0, 1, 2, 0, 1],
         [3, 1, 0, 1, 0]]

# Manually setting the destination
destination_node = 3 


dijkstra = {}

# First step of the algorithm, populating the resuts matrix with infinite in all nodes but the start
for i in range(len(graph)):
    dijkstra[i]=[float('inf'),['']]

dijkstra[0]=[0, '0']

# Second and third steps of the algorithm. For each node visit the neibourghs and assign them the value of the cost to reach them from the starting node if this is lower than its current value.
for node in dijkstra.keys():
    for vertex in range(len(graph[node])):
        if graph[node][vertex] and  dijkstra[vertex][0] > dijkstra[node][0] + graph[node][vertex]:
            dijkstra[vertex][0] = dijkstra[node][0] + graph[node][vertex]
            dijkstra[vertex][1] = dijkstra[node][1]+'-'+str(vertex)            

# Print the final result
print ("The shortest path to node {} is through {} with a total cost of {}".format(destination_node, dijkstra[destination_node][1], dijkstra[destination_node][0]))
