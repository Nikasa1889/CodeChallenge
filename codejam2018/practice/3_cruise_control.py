T = int(input())

for i in range(T):
    D, N = map(int, input().split())
    max_t = 0
    for _ in range(N):
        K , S = map(int, input().split())
        t = (D - K)/S
        if t > max_t: max_t = t
    max_s = D / max_t
    print('Case #{}: {}'.format(i+1, max_s))
