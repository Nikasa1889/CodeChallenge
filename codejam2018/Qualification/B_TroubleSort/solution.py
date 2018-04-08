T = int(input())

for i_t in range(T):
    N = int(input())
    A = list(map(int, input().split()))

    A[0::2] = sorted(A[0::2])
    A[1::2] = sorted(A[1::2])
    ans = 'OK'
    for i in range(len(A)-1):
        if A[i]>A[i+1]:
            ans = i
            break
    print('Case #{}: {}'.format(i_t + 1, ans))
