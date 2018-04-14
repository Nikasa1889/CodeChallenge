# Library must implement for list and matrix:
# Argmax, Argmin, Index, Sum,
from math import sqrt
T = int(input())
for i_t in range(T):
    N, P = map(int, input().split())
    W = [0]*N
    H = [0]*N
    for i_n in range(N):
        w, h = map(int, input().split())
        W[i_n], H[i_n]=w, h

    PiMax = sum(W)
    D = {}
    D[0] = 0
    for i in range(N):
        pi = 2*W[i]
        flex = 2*sqrt(W[i]*W[i] + H[i]*H[i]) - 2*W[i]
        for dpi in list(D):
            dflex = D[dpi]
            poss_flex = D.get(pi+dpi, 0)
            if poss_flex < dflex+flex:
                D[pi+dpi] = dflex + flex
    base = (sum(W) + sum(H)) * 2
    for i in D.keys():
        D[i] += base
    min_dist = P
    for pi, flex in D.items():
        if (P > pi):
            if (pi+flex>=P):
                min_dist=P
                break
            else:
                min_dist = pi+flex
    print("Case #{}: {}".format(i_t+1, min_dist))

'''
4
1 7
1 1
2 920
50 120
50 120
1 32
7 4
3 240
10 20
20 30
30 10
'''