#!/usr/bin/env python
#
# http://en.wikipedia.org/wiki/Ford-Fulkerson_algorithm
# Ford-Fulkerson algorithm computes max flow in a flow network.
#
# NOTE: Too slow and use recursion that is too deep. Can't work on large graph
import builtins

DEBUG=False

def dprint(*args, **kwargs):
    if DEBUG: builtins.print(*args, **kwargs)

class Edge(object):
  def __init__(self, u, v, w):
    self.source = u
    self.target = v
    self.capacity = w

  def __repr__(self):
    return "%s->%s:%s" % (self.source, self.target, self.capacity)

class FlowNetwork(object):
  def  __init__(self):
    self.adj = {}
    self.flow = {}

  def AddVertex(self, vertex):
    self.adj[vertex] = []

  def GetEdges(self, v):
    return self.adj[v]

  def AddEdge(self, u, v, w):
    if u == v:
      raise ValueError("u == v")
    edge = Edge(u, v, w)
    redge = Edge(v, u, 0)
    edge.redge = redge
    redge.redge = edge
    self.adj[u].append(edge)
    self.adj[v].append(redge)
    # Intialize all flows to zero
    self.flow[edge] = 0
    self.flow[redge] = 0

  def FindPath(self, source, target, path):
    if source == target:
      return path
    for edge in self.GetEdges(source):
      residual = edge.capacity - self.flow[edge]
      if residual > 0 and not (edge, residual) in path:
        result = self.FindPath(edge.target, target, path + [(edge, residual)])
        if result != None:
          return result

  def MaxFlow(self, source, target, debug=False):
    path = self.FindPath(source, target, [])
    if debug:
        print('path after enter MaxFlow: %s' % path)
        for key in self.flow:
          print('%s:%s' % (key,self.flow[key]))
        print('-' * 20)
    while path != None:
      flow = min(res for edge, res in path)
      for edge, res in path:
        self.flow[edge] += flow
        self.flow[edge.redge] -= flow
      if debug:
          for key in self.flow: print('%s:%s' % (key,self.flow[key]))
      path = self.FindPath(source, target, [])
      if debug: print('path inside of while loop: %s' % path)
    if debug:
      for key in self.flow: print('%s:%s' % (key,self.flow[key]))
    return sum(self.flow[edge] for edge in self.GetEdges(source))


# if __name__ == "__main__":
#   g = FlowNetwork()
#   for v in ['s', 'o', 'p', 'q', 'r', 't']: g.AddVertex(v)
#   g.AddEdge('s', 'o', 5)
#   g.AddEdge('s', 'p', 3)
#   g.AddEdge('o', 'p', 2)
#   g.AddEdge('o', 'q', 3)
#   g.AddEdge('p', 'r', 4)
#   g.AddEdge('r', 't', 3)
#   g.AddEdge('q', 'r', 4)
#   g.AddEdge('q', 't', 2)
#   print(g.MaxFlow('s', 't'))

from math import ceil, floor

def cal_range(r, q):
    min_k = ceil(q/(1.1*r))
    max_k = floor(q/(0.9*r))
    if min_k > max_k: return None
    else: return (min_k, max_k)

def is_overlap(rng1, rng2):
    min_r, max_r = (max(rng1[0], rng2[0]), min(rng1[1], rng2[1]))
    if min_r >max_r:
        return False
    else:
        return True

T = int(input())
for i_t in range(T):
    N, P = map(int, input().split())
    R = list(map(int, input().split()))
    Q = []

    for i_n in range(N):
        Q.append(list(map(int, input().split())))
    for i in range(N):
        for j in range(P):
             Q[i][j] = cal_range(R[i], Q[i][j])
        Q[i] = [rng for rng in Q[i] if rng is not None]
    g = FlowNetwork()
    g.AddVertex('Start'); g.AddVertex('End')
    for i_n in range(N):
        for i_q, q in enumerate(Q[i_n]):
            g.AddVertex((i_n, i_q))
            if i_n == 0:
                g.AddEdge('Start', (i_n, i_q), 1)
            else:
                for i_q_pre, q_pre_n in enumerate(Q[i_n-1]):
                    if is_overlap(q_pre_n, q):
                        g.AddEdge((i_n-1, i_q_pre), (i_n, i_q), 1)
            if i_n == N-1:
                g.AddEdge((i_n, i_q), 'End', 1)

    ans = g.MaxFlow('Start', 'End', debug=DEBUG)
    print("Case #{}: {}".format(i_t+1, ans))
    # Test Case
'''
6
2 1
500 300
900
660
2 1
500 300
1500
809
2 2
50 100
450 449
1100 1101
2 1
500 300
300
500
1 8
10
11 13 17 11 16 14 12 18
3 3
70 80 90
1260 1500 700
800 1440 1600
1700 1620 900

'''