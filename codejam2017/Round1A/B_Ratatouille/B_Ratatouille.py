# Fail large case
T = int(input())
from math import ceil, floor
def cal_range(r, q):
    min_k = ceil(q/(1.1*r))
    max_k = floor(q/(0.9*r))
    if min_k > max_k: return None
    else: return (min_k, max_k)

def merge(rng1, rng2):
    if rng1 is None or rng2 is None: return None
    res = (max(rng1[0], rng2[0]), min(rng1[1], rng2[1]))
    if res[0]>res[1]: return None
    else: return res

def select_p(n, allowed_rng):
    if n == N: return 1
    p = curr_p[n]
    while (p < len(Q[n])) and (Q[n][p][0]<=allowed_rng[1]):
        new_rng = merge(allowed_rng, Q[n][p])
        if new_rng is None:
            curr_p[n] = p+1
        if new_rng is not None:
            res = select_p(n+1, new_rng)
            if res == 1:
                curr_p[n] = p
                return 1
        p = p + 1
    return 0

for i_t in range(T):
    N, P = map(int, input().split())
    R = list(map(int, input().split()))
    Q = []

    for i_n in range(N):
        Q.append(list(map(int, input().split())))
    for i in range(N):
        for j in range(P):
             Q[i][j] = cal_range(R[i], Q[i][j])
        Q[i] = sorted([rng for rng in Q[i] if rng is not None])
    curr_p = [0 for i in range(N)]
    ans = 0
    for rng_0 in Q[0]:
        ans += select_p(1, rng_0)

    print("Case #{}: {}".format(i_t+1, ans))