from math import cos, sin, pi

Corner_down = (-0.5, -0.5, 0.5)
Corner_up = (0.5, 0.5, -0.5)
Center_1 = (0.5, 0, 0)
Center_2 = (0, 0.5, 0)
Center_3 = (0, 0, 0.5)

def rotate_z(theta, point): # around z
    theta = -theta
    x, y, z = point
    new_x = x*cos(theta) - y*sin(theta)
    new_y = x*sin(theta) + y*cos(theta)
    new_z = z
    return (new_x, new_y, new_z)

def cal_A(theta):
    new_corner_down = rotate_z(theta, Corner_down)
    new_corner_up = rotate_z(theta, Corner_up)
    x1, y1, z1 = new_corner_down
    x2, y2, z2 = new_corner_up
    return abs(x2-x1)*abs(z2-z1)

def eq_eps(a, b, eps=1e-6):
    return abs(a - b) <= 1e-6

T = int(input())

for i_t in range(T):
    A = float(input())
    min_theta = 0.0
    max_theta = pi/4
    min_A = 1.0
    max_A = cal_A(max_theta)
    if eq_eps(min_A, A):
        ans = min_theta
    elif eq_eps(max_A, A):
        ans = max_theta
    else:
        while True:
            mid_theta = (min_theta + max_theta)/2
            mid_A = cal_A(mid_theta)
            if eq_eps(A, mid_A):
                ans = mid_theta
                break
            else:
                if A > mid_A:
                    min_theta, min_A = mid_theta, mid_A
                else:
                    max_theta, max_A = mid_theta, max_A

    c_1 = rotate_z(ans, Center_1)
    c_2 = rotate_z(ans, Center_2)
    c_3 = rotate_z(ans, Center_3)

    print('Case #{}:'.format(i_t + 1))
    print('{} {} {}'.format(*c_1))
    print('{} {} {}'.format(*c_2))
    print('{} {} {}'.format(*c_3))

