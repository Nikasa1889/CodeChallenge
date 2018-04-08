from math import cos, sin, pi

Corner_down = (-0.5, -0.5, 0.5)
Corner_up = (0.5, 0.5, -0.5)
C_1 = (0.5, 0, 0)
C_2 = (0, 0.5, 0)
C_3 = (0, 0, 0.5)

def rotate_z(theta, point): # around z
    theta = -theta
    x, y, z = point
    new_x = x*cos(theta) - y*sin(theta)
    new_y = x*sin(theta) + y*cos(theta)
    new_z = z
    return (new_x, new_y, new_z)

def rotate_x(theta, point): # around x
    theta = -theta
    x, y, z = point
    new_x = x
    new_y = cos(theta)*y - sin(theta)*z
    new_z = sin(theta)*y + cos(theta)*z
    return (new_x, new_y, new_z)

P_A = rotate_z(pi/4, (-0.5, -0.5, 0.5))
P_B = rotate_z(pi/4,(0.5, 0.5, 0.5))
P_C = rotate_z(pi/4,(0.5, 0.5, -0.5))
P_D = rotate_z(pi/4,(-0.5, -0.5, -0.5))
P_E = rotate_z(pi/4,(0.5, -0.5, 0.5))
P_F = rotate_z(pi/4,(-0.5, 0.5, -0.5))

def area(A, B, C):
    A_x, A_y, A_z = A
    B_x, B_y, B_z = B
    C_x, C_y, C_z = C
    return abs(0.5*(A_x*(B_z-C_z) + B_x*(C_z-A_z) + C_x*(A_z-B_z)))

def cal_A(theta):
    new_corner_down = rotate_z(theta, Corner_down)
    new_corner_up = rotate_z(theta, Corner_up)
    x1, y1, z1 = new_corner_down
    x2, y2, z2 = new_corner_up
    return abs(x2-x1)*abs(z2-z1)

def cal_A_2R(theta):
    A, B, C, D, E, F = [rotate_x(theta, P) for P in [P_A, P_B, P_C, P_D, P_E, P_F]]
    a = area(A, B, E) + area(A, B, C) + area(A, F, D) + area(A, C, F)
    return a

def eq_eps(a, b, eps=1e-6):
    return abs(a - b) <= 1e-6

def find_theta(min_theta, max_theta, f):
    min_A = f(min_theta)
    max_A = f(max_theta)
    if eq_eps(min_A, A):
        return min_theta
    elif eq_eps(max_A, A):
        return max_theta
    if A > max_A:
        return None
    while True:
        mid_theta = (min_theta + max_theta) / 2
        mid_A = f(mid_theta)
        if eq_eps(A, mid_A):
            return mid_theta
        else:
            if A > mid_A:
                min_theta, min_A = mid_theta, mid_A
            else:
                max_theta, max_A = mid_theta, max_A

T = int(input())

for i_t in range(T):
    A = float(input())
    ans_theta_x = 0
    ans_theta_z = find_theta(0.0, pi/4, cal_A)
    if ans_theta_z is None:
        ans_theta_z = pi/4
        ans_theta_x = find_theta(0.0, 783653/1000000*pi/4, cal_A_2R)

    print('Case #{}:'.format(i_t + 1))
    print('{} {} {}'.format(*rotate_x(ans_theta_x, rotate_z(ans_theta_z, C_1))))
    print('{} {} {}'.format(*rotate_x(ans_theta_x, rotate_z(ans_theta_z, C_2))))
    print('{} {} {}'.format(*rotate_x(ans_theta_x, rotate_z(ans_theta_z, C_3))))




