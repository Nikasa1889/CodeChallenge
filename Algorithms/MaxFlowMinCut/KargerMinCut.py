# Note: Too slow, only run with V = 100
import random
import copy

cuts = []
graph = {}


def kargerMinCut(graph):
    while len(graph) > 2:
        v = random.choice(list(graph.keys()))
        w = random.choice(graph[v])
        contract(graph, v, w)

    # Calculating and recording the mincut
    mincut = len(graph[list(graph.keys())[0]])
    cuts.append(mincut)


def contract(graph, v, w):
    for node in graph[w]:  # merge the nodes from w to v
        if node != v:  # we dont want to add self-loops
            graph[v].append(node)
        graph[node].remove(w)  # delete the edges to the absorbed node 'w' and change them to the source node 'v'
        if node != v:
            graph[node].append(v)

    del graph[w]  # delete the absorbed vertex 'w'

if __name__ == '__main__':
    from random import randint
    from collections import defaultdict
    # graph = readGraphFromFile("graph.txt") # read the graph from a text file
    #graph[1] = [2, 4]
    #graph[2] = [1, 3, 4]
    #graph[3] = [2, 4]
    #graph[4] = [1, 2, 3]
    V = 100
    numberOfRepeatedTrials = 10
    graph = defaultdict(list)#[[] for i in range(V)]
    for i in range(V):
        for j in range(i+1, V):
            x = randint(0,1)
            if x>0:
                graph[i].append(j)
                graph[j].append(i)
    for i in range(1, numberOfRepeatedTrials):  # we do repeated trials to find the minimum cut.
        copiedGraph = copy.deepcopy(graph)
        kargerMinCut(copiedGraph)
    print("MinCut is " + str(min(cuts)))
