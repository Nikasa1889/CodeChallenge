"""
    A Minimum Cut Solver

    This python script is for solving the ACM problem Q2914: Minimum Cut.
    http://acm.pku.edu.cn/JudgeOnline/problem?id=2914

    Instead of using Ford-Fulkerson method, I use Stoer and Wagner's Min cut Algorithm.
    http://www.cs.dartmouth.edu/~ac/Teach/CS105-Winter05/Handouts/stoerwagner-mincut.pdf

    However I also include the max flow method (from wiki) for benchmark.
    The code can be found at: http://en.wikipedia.org/wiki/Ford-Fulkerson_algorithm

    Copyright 2009 Shao-Chuan Wang <shaochuan.wang@gmail.com>

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in
    all copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
    THE SOFTWARE.
"""
# From: http://code.activestate.com/recipes/576907-minimum-cut-solver/
__author__ = "Shao-Chuan Wang"
__email__ = "shaochuan.wang@gmail.com"
__version__ = "1.0"
__URL__ = "http://shao-chuan.appspot.com"

class UndirectedGraph(object):
    def __init__(self):
        self.vertices = []
        self.edges = {}

    def add_vertex(self, v):
        self.vertices.append(v)
        self.edges[(v, v)] = 0

    def add_vertices(self, v_s):
        self.vertices.extend(v_s)
        for v in v_s:
            self.edges[(v, v)] = 0

    def add_edge(self, u, v, w):
        self.edges[(u, v)] = w
        self.edges[(v, u)] = w

    def adjacents(self, u):
        li = []
        for v in self.vertices:
            w = self.edges.get((u, v), 0)
            if w:
                li.append((v, w))
        return li

    def merge(self, u, v):
        ''' merge u to v, where v is in the graph
        '''
        u_adjs = self.adjacents(u)
        for z, w in u_adjs:
            self.edges.pop((u, z))
            self.edges.pop((z, u))
        self.vertices.remove(u)
        v_adjs = dict(self.adjacents(v))
        for n, w in u_adjs:
            if n == v:
                continue
            v_adjs[n] = v_adjs.get(n, 0) + w
        for n, w in v_adjs.items():
            self.edges[(v, n)] = w
            self.edges[(n, v)] = w


def w(g, A, y):
    assert y not in A
    return sum(w for v, w in g.adjacents(y) if v in A)


def min_cut_phase(g, a):
    A = set([a])
    V = set(g.vertices)
    order = [a]
    while A != V:
        w_candidates = [(w(g, A, v), v) for v in V - A]  #: candidates for most tightly connected
        _, x = max(w_candidates)
        A.add(x)
        order.append(x)
    t, s = order[-1], order[-2]

    min_cut = sum(w for v, w in g.adjacents(t))
    g.merge(t, s)
    return min_cut


def minimum_cut(g, a):
    min_cut = sum(w for v, w in g.adjacents(a))
    while len(g.vertices) > 1:
        min_cut_candidate = min_cut_phase(g, a)
        if min_cut_candidate < min_cut:
            min_cut = min_cut_candidate
    return min_cut

import time
from random import randint
if __name__ == '__main__':

    V = 100
    graph = [[0 for j in range(V)] for i in range(V)]
    graph = UndirectedGraph()
    graph.add_vertices([i for i in range(V)])
    for i in range(V):
        for j in range(i + 1, V):
            x = randint(0, 1)
            if x > 0:
                graph.add_edge(i, j, 1)
    start_time = time.time()
    print(minimum_cut(graph, 0))
    print(time.time() - start_time)
