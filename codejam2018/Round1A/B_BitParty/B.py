T = int(input())
from math import floor
def is_possible(t):
    MaxCheck = [0 for i in range(C)]
    for i in range(C):
        maxcheck = floor((t - P[i])/S[i])
        if maxcheck < 0: maxcheck = 0
        if (maxcheck > M[i]):
            maxcheck = M[i]
        MaxCheck[i] = maxcheck

    MaxCheck = list(reversed(sorted(MaxCheck)))[:R]
    total = sum(MaxCheck)
    if total >= B:
        return True
    else:
        return False

for i_t in range(T):
    R, B, C = map(int, input().split())
    M, S, P= [], [], []
    for i_c in range(C):
        m, s, p = map(int, input().split())
        M.append(m)
        S.append(s)
        P.append(p)
    min_t = 1
    max_t = 10000000000
    while min_t < max_t:
        mid_t = (min_t + max_t) // 2
        if is_possible(mid_t):
            max_t = mid_t
        else:
            min_t = mid_t + 1
    ans = min_t
    print("Case #{}: {}".format(i_t+1, ans))

'''
3
2 2 2
1 2 3
1 1 2
2 2 2
1 2 3
2 1 2
3 4 5
2 3 3
2 1 5
2 4 2
2 2 4
2 5 1
'''