def is_chocolate(c):
    if c == '@':
        return 1
    else:
        return 0
def count_chips(min_r, max_r, min_c, max_c):
    total = 0
    for r in range(min_r, max_r):
        for c in range(min_c, max_c):
            total+=Cake[r][c]
    return total

T = int(input())
for i_t in range(T):
    ans='IMPOSSIBLE'
    R, C, H, V = map(int, input().split())
    Cake = []
    total_chips = 0
    total_slices = (H+1)*(V+1)
    for i_r in range(R):
        row = list(map(is_chocolate, list(input())))
        Cake.append(row)
        total_chips += sum(row)
    if total_chips % total_slices == 0:
        try:
            expected_row = total_chips / (H+1)
            expected_col = total_chips / (V+1)
            expected_slice = total_chips / ((H+1)*(V+1))
            h_cuts = [0]
            v_cuts = [0]
            cur_chip = 0
            for h in range(R):
                cur_chip += sum(Cake[h])
                if cur_chip == expected_row:
                    cur_chip = 0
                    h_cuts.append(h+1)
                if cur_chip > expected_row:
                    raise Exception('Impossible')
                if len(h_cuts) == H+1:
                    break
            if (len(h_cuts)!= H+1): raise Exception

            h_cuts.append(R)
            cur_chip = 0
            for v in range(C):
                cur_chip += count_chips(0, R, v, v+1)
                if cur_chip == expected_col:
                    cur_chip = 0
                    v_cuts.append(v+1)
                if cur_chip > expected_col:
                    raise Exception('Impossible')
                if len(v_cuts) == V+1:
                    break
            if (len(v_cuts)!= V+1): raise Exception

            v_cuts.append(C)
            # Check each slices
            for h in range(1, len(h_cuts)):
                for v in range(1, len(v_cuts)):
                    if count_chips(h_cuts[h-1], h_cuts[h], v_cuts[v-1], v_cuts[v]) != expected_slice:
                        raise Exception('IMPOSSIBLE')

            ans = 'POSSIBLE'
        except:
            ans = 'IMPOSSIBLE'

    print("Case #{}: {}".format(i_t+1, ans))
'''
8
6 6 2 1
@@@@@@
@@@@@@
@@@@@@
@@@@@@
@@@@@@
@@@@@@
4 4 1 1
.@.@
.@.@
.@.@
.@.@
3 6 1 1
.@@..@
.....@
@.@.@@
4 3 1 1
@@@
@.@
@.@
@@@
4 5 1 1
.....
.....
.....
.....
4 4 1 1
..@@
..@@
@@..
@@..
3 4 2 2
@.@@
@@.@
@.@@
3 4 1 2
.@.@
@.@.
.@.@
'''