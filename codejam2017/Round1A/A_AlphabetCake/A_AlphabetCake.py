T = int(input())

for i in range(T):
    R, C = map(int, input().split())
    Cake = []
    for r in range(R):
        row = input().split()
        Cake.append(row)
    
    # Fill row to right
    for r in range(0, R):
        for c in range(1, C):
            if Cake[r][c] == '?': Cake[r][c] = Cake[r][c-1]
    # Fill row to left
    for r in range(0, R):
        for c in range(C-2, 0, -1):
            if Cake[r][c] == '?': Cake[r][c] = Cake[r][c+1]
    # Fill column down
    for r in range(1, R):
        for c in range(0, C):
            if Cake[r][c] == '?': Cake[r][c] = Cake[r-1][c]

    # Fill column up:
    for r in range(R-2, 0, -1):
        for c in range(0, C):
            if Cake[r][c] == '?': Cake[r][c] = Cake[r+1][c]

    print ('Case #{}:'.format(i+1))
    for r in range(R):
        print(''.join(Cake[r]))