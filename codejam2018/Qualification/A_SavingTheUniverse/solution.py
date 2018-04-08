T = int(input())
for i_t in range(T):
    D, P = input().split()
    D = int(D); P = list(P)
    C_pos = []
    S_total = 0
    ans = 0
    for i in range(len(P)):
        if P[i] == 'C':
            C_pos.append(i)
        else:
            S_total += 1

    if S_total > D:
        ans = 'IMPOSSIBLE'
    else:
        total_D = 0
        cur_charge = 1
        for i in range(len(P)):
            if P[i] == 'C':
                cur_charge *= 2
            else:
                total_D += cur_charge

        while total_D > D:
            for i_c in reversed(range(len(C_pos))):
                adj = 1 << i_c
                pos = C_pos[i_c]
                while (pos+1<len(P)) and (P[pos+1] == 'S') and (total_D > D):
                    P[pos] = 'S'
                    P[pos+1] = 'C'
                    pos += 1
                    total_D -= adj
                    ans += 1
                if (total_D <= D):
                    break

    print('Case #{}: {}'.format(i_t+1, ans))