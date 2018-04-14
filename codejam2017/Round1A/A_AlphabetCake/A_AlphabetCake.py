T = int(input())

for i in range(T):
    R, C = map(int, input().split())
    Cake = []
    for r in range(R):
        row = list(input())
        Cake.append(row)
    # Fill row to right
    for r in range(R):
        for c in range(1, C):
            if Cake[r][c] == '?': Cake[r][c] = Cake[r][c-1]
    # Fill row to left
    for r in range(R):
        for c in reversed(range(C-1)):
            if Cake[r][c] == '?': Cake[r][c] = Cake[r][c+1]
    # Fill column down
    for r in range(1, R):
        for c in range(C):
            if Cake[r][c] == '?': Cake[r][c] = Cake[r-1][c]

    # Fill column up:
    for r in reversed(range(R-1)):
        for c in range(C):
            if Cake[r][c] == '?': Cake[r][c] = Cake[r+1][c]

    print ('Case #{}:'.format(i+1))
    for r in range(R):
        print(''.join(Cake[r]))