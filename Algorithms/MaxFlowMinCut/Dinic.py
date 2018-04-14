#Dinic Algorithm
# https://github.com/anxiaonong/Maxflow-Algorithms/blob/master/Dinic's%20Algorithm.py
# Can't run with V > 300
#build level graph by using BFS
def Bfs(C, F, s, t):  # C is the capacity matrix
        n = len(C)
        queue = []
        queue.append(s)
        global level
        level = n * [0]  # initialization
        level[s] = 1
        while queue:
            k = queue.pop(0)
            for i in range(n):
                    if (F[k][i] < C[k][i]) and (level[i] == 0): # not visited
                            level[i] = level[k] + 1
                            queue.append(i)
        return level[t] > 0

#search augmenting path by using DFS
def Dfs(C, F, k, cp):
        tmp = cp
        if k == len(C)-1:
            return cp
        for i in range(len(C)):
            if (level[i] == level[k] + 1) and (F[k][i] < C[k][i]):
                f = Dfs(C,F,i,min(tmp,C[k][i] - F[k][i]))
                F[k][i] = F[k][i] + f
                F[i][k] = F[i][k] - f
                tmp = tmp - f
        return cp - tmp

#calculate max flow
#_ = float('inf')
def MaxFlow(C,s,t):
        n = len(C)
        F = [n*[0] for i in range(n)] # F is the flow matrix
        flow = 0
        while(Bfs(C,F,s,t)):
               flow = flow + Dfs(C,F,s,100000)
        return flow

#-------------------------------------
# make a capacity graph
# node   s   o   p   q   r   t
#C = [[ 0, 3, 3, 0, 0, 0 ],  # s
#     [ 0, 0, 2, 3, 0, 0 ],  # o
#     [ 0, 0, 0, 0, 2, 0 ],  # p
#     [ 0, 0, 0, 0, 4, 2 ],  # q
#     [ 0, 0, 0, 0, 0, 2 ],  # r
#     [ 0, 0, 0, 0, 0, 3 ]]  # t
# General Graph
from random import randint
from math import floor
V = 300
graph = [[0 for j in range(V)] for i in range(V)]
for i in range(V):
    for j in range(i+1, V):
        x = randint(0, 1)
        if x > 0:
            graph[i][j] = 1
            graph[j][i] = 1

source = 0
sink = V-1

# Graph with N layer (max possible flow is max number of element in a layer)
# V is source, connect with all node in first layer, V+1 is sink
V = 1000
N_layer = 50
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


print("Dinic's Algorithm")
max_flow_value = MaxFlow(graph, source, sink)
print("max_flow_value is", max_flow_value)