import sys
import math

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    n = int(input())
    while n > 0:
        n -= 1
        p = math.floor((a+b)/2)
        print(p, flush=True)
        ans = input()
        if ans == 'CORRECT': break
        if ans == 'WRONG_ANSWER': sys.exit("Wrong Answer")
        if ans == 'TOO_BIG': b = p
        if ans == 'TOO_SMALL': a = p+1

