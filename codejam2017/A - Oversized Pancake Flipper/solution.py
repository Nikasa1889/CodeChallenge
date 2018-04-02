# https://code.google.com/codejam/contest/3264486/dashboard#s=p0
T = int(input())

cake2num = {'+': 1, '-': 0}

for i_case in range(1, T+1):
  S, K = input().split()
  K, n_flip = int(K), 0
  n_cake = len(S)
  S = [cake2num[cake] for cake in S]
  for (i_cake, cake) in enumerate(S):
    if cake == 0:
      if (n_cake - i_cake) < K:
        n_flip = -1
        break
      for j_cake in range(i_cake, i_cake+K):
        S[j_cake] = 1 - S[j_cake]
      n_flip += 1
  if n_flip < 0:
    print(f'Case #{i_case}: IMPOSSIBLE')
  else:
    print(f'Case #{i_case}: {n_flip}')
