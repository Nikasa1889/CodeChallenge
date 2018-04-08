def update_E(E, x, y):
    for d_x in [-1, 0, 1]:
        for d_y in [-1, 0, 1]:
            x_1,y_1 = x+d_x,y+d_y
            if (x_1, y_1) in E:
                E[(x_1, y_1)] -= 1

def best_point(E):
    return max(E, key=E.get)

T = int(input())

for _ in range(T):
    A = int(input()) #either 20 or 200
    if A == 20:
        len_x, len_y = 4, 5
    else:
        len_x, len_y = 14, 15

    x_TL, y_TL = 300, 300
    print('{} {}'.format(x_TL, y_TL), flush=True)
    x_TL, y_TL = map(int, input().split())

    E = {} # Empties at each possible point
    M = [[False]*len_y for x in range(len_x)]

    for i in range(x_TL+1, x_TL + len_x-1):
        for j in range(y_TL+1, y_TL + len_y-1):
            E[(i, j)] = 9

    done = False
    while not done:
        point = best_point(E)
        print('{} {}'.format(*point), flush=True)
        x, y = map(int, input().split())
        if (x == 0) and (y == 0):
            break
        #stderr.write(x, y)
        if not M[x-x_TL][y-y_TL]:
            update_E(E, x, y)
            M[x-x_TL][y-y_TL] = True
