# From https://en.wikipedia.org/wiki/Ford%E2%80%93Fulkerson_algorithm
import collections

# This class represents a directed graph using adjacency matrix representation
class Graph:
    def __init__(self, graph):
        self.graph = graph  # residual graph
        self.ROW = len(graph)

    def BFS(self, s, t, parent):
        '''Returns true if there is a path from source 's' to sink 't' in
        residual graph. Also fills parent[] to store the path '''

        # Mark all the vertices as not visited
        visited = [False] * (self.ROW)

        # Create a queue for BFS
        queue = collections.deque()

        # Mark the source node as visited and enqueue it
        queue.append(s)
        visited[s] = True

        # Standard BFS Loop
        while queue:
            u = queue.popleft()

            # Get all adjacent vertices's of the dequeued vertex u
            # If a adjacent has not been visited, then mark it
            # visited and enqueue it
            for ind, val in enumerate(self.graph[u]):
                if visited[ind] == False and val > 0:
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u

        # If we reached sink in BFS starting from source, then return
        # true, else false
        return visited[t]

    # Returns the maximum flow from s to t in the given graph
    def EdmondsKarp(self, source, sink):

        # This array is filled by BFS and to store path
        parent = [-1] * (self.ROW)

        max_flow = 0  # There is no flow initially

        # Augment the flow while there is path from source to sink
        while self.BFS(source, sink, parent):

            # Find minimum residual capacity of the edges along the
            # path filled by BFS. Or we can say find the maximum flow
            # through the path found.
            path_flow = float("Inf")
            s = sink
            while s != source:
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

            # Add path flow to overall flow
            max_flow += path_flow

            # update residual capacities of the edges and reverse edges
            # along the path
            v = sink
            while v != source:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]

        return max_flow

from random import randint
from math import floor, ceil
# graph = [[0, 16, 13, 0, 0, 0],
#          [0, 0, 10, 12, 0, 0],
#          [0, 4, 0, 0, 14, 0],
#          [0, 0, 9, 0, 0, 20],
#          [0, 0, 0, 7, 0, 4],
#          [0, 0, 0, 0, 0, 0]]

# General Graph: Max V = 300
V = 100
graph = [[0 for j in range(V)] for i in range(V)]
for i in range(V):
    for j in range(i+1, V):
        x = randint(0, 1)
        if x > 0:
            graph[i][j] = 1
            graph[j][i] = 1
source = 0
sink = V - 1

# Graph with N layer (max possible flow is max number of element in a layer)
# V is source, connect with all node in first layer, V+1 is sink
V = 1000
N_layer = 30
N_V_layer = int(V/N_layer)
graph = [[0 for j in range(V+2)] for i in range(V+2)]
for i in range(V):
    for j in range(i+1, V):
        if (floor(j/N_V_layer) - floor(i/N_V_layer)) == 1:
            x = randint(0, 1)
            if x > 0:
                graph[i][j] = 1
                graph[j][i] = 1
# Connect source to all node in first layer, and sink to all node in last layer
source = V
sink = V+1

for j in range(N_V_layer):
    graph[source][j] = 1
    graph[j][source] = 1
for j in range(V-N_V_layer, V):
    graph[sink][j] = 1
    graph[j][sink] = 1

graph = Graph(graph)
max_flow = graph.EdmondsKarp(source, sink)
print(max_flow)