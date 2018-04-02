# The same as codejam2017 Qualification, problem 3
from math import floor, ceil

T = int(input())

for i_case in range(1, T+1):
    N, K = [int(st) for st in input().split()]
    high = 1
    while high <= K:
        high *= 2
    low = high >> 1
    n_segments = low
    n_occupied = low - 1
    n_free = N - n_occupied
    n_long_segs = n_free % n_segments
    len_short = n_free // n_segments - 1 # the last
    len_long = len_short + 1
    extra = K - low + 1
    if extra <= n_long_segs:
        l = len_long
    else:
        l = len_short

    m = l % 2
    print(f'Case #{i_case}: {(l >> 1) + m} {l >> 1}')
