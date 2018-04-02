# Read input
import numpy as np
import itertools
from tqdm import tqdm

def map2int(ls):
    return [int(st) for st in ls]

def read_int_list(f):
    return map2int(f.readline().split(' '))

def cal_distance(x0, y0, x1, y1):
    return abs(x1-x0) + abs(y1-y0)

def cal_end2start(ride1, ride2):
    return cal_distance(ride1['x'], ride1['y'], ride2['a'], ride2['b'])

def possible_follow(ride1, ride2, end2start):
    earliest_finish = ride1['start_els'] + ride1['distance']
    return (earliest_finish + end2start <= ride2['critical_start'])

#fname = 'b_should_be_easy.in'
#fout = 'b_should_be_easy.out'
#fname = 'c_no_hurry.in'
#fout = 'c_no_hurry.out'
#fname = 'd_metropolis.in'
#fout = 'd_metropolis.out'
fname = 'e_high_bonus.in'
fout = 'e_high_bonus.out'

with open(fname) as f:
    R, C, F, N, B, T = read_int_list(f)
    rides = []
    #Rend2start = np.full((N+1, N+1), -np.inf, dtype=float)   
    for i_ride in range(N):
        x0, y0, x1, y1, start_els, finish = read_int_list(f)
        distance = cal_distance(x0, y0, x1, y1)
        rides.append({'a': x0, 'b':y0, 'x':x1, 'y':y1, 
                      'distance': distance, 'critical_start': finish-distance,
                      'start_els':start_els, 'finish':finish})
        
    # Ride N+1 is the starting point
    rides.append({'a':0, 'b':0, 'x':0, 'y':0,
                  'distance': 0, 'critical_start': 0,
                  'start_els': 0, 'finish': 0})
    
    # Precalculate rides that can follow R
    R_links = {}
    End2Start = np.zeros((N+1, N+1), dtype=int)
    for i_ride1 in tqdm(range(N+1)):
        ride1 = rides[i_ride1]
        R_links[str(i_ride1)] = list()
        for i_ride2 in range(N+1):
            if i_ride1 == i_ride2: continue
            ride1, ride2 = rides[i_ride1], rides[i_ride2]
            end2start = cal_end2start(ride1, ride2)
            End2Start[i_ride1, i_ride2] = dist
            if possible_follow(ride1, ride2, end2start):
                R_links[str(i_ride1)].append(i_ride2)
            #print(len(R_links[i_ride1]))
        
def cal_loss_waiting_time(waiting_time):
    return waiting_time * coeff_waiting_loss

def cal_loss_bonus(distance):
    return distance * coeff_bonus_loss

def is_possible(ride2, end2start, cur_t):
    return (cur_t + end2start <= ride2['critical_start'])
        
    
def cal_reward(ride1, ride2, cur_t, end2start):
    bonus = 0
    # Bonus
    if cur_t + end2start <= ride2['start_els']:
        bonus = B
    dist = ride2['distance']
    
    waiting_time = end2start
    if cur_t + end2start < ride2['start_els']:
        waiting_time += ride2['start_els'] - (cur_t + end2start)
        
    loss_waiting = cal_loss_waiting_time(waiting_time)
    loss_bonus = cal_loss_bonus(dist)
    return (bonus, bonus + dist, waiting_time, dist, bonus + dist - loss_waiting - loss_bonus)

coeff_waiting_loss = 0.5
coeff_bonus_loss = 0.5
VclRides = [list() for _ in range(F)]
selected_rides = set()
selected_rides.add(N)

for i_vcl in tqdm(range(F)):
    i_cur_ride = N
    cur_t = 0
    cur_ride = rides[i_cur_ride]
    total_reward = 0
    total_bonus = 0
    while True:
        max_reward = -np.inf
        max_i_ride_follow = None
        max_bonus = None
        max_real_reward = None
        max_waiting_time = None
        max_dist = None
        max_end2start = None
        for i_ride_follow in R_links[str(i_cur_ride)]:
            ride_follow = rides[i_ride_follow]
            end2start = End2Start[i_cur_ride, i_ride_follow] 
            if i_ride_follow in selected_rides: continue
            if not is_possible(ride_follow, end2start, cur_t): continue
            bonus, real_reward, waiting_time, dist, reward = cal_reward(cur_ride, ride_follow, cur_t, end2start)
            if reward > max_reward:
                max_reward = reward
                max_real_reward = real_reward
                max_i_ride_follow = i_ride_follow
                max_bonus = bonus
                max_waiting_time = waiting_time
                max_dist = dist
                max_end2start = end2start
        if max_i_ride_follow is None: break
        total_reward += max_real_reward
        total_bonus += max_bonus
        
        cur_t += max_waiting_time + max_dist + max_end2start
        coeff_waiting_loss = total_reward / cur_t
        coeff_bonus_loss = total_bonus / cur_t
        
        i_cur_ride = max_i_ride_follow
        cur_ride = rides[i_cur_ride]
        
        VclRides[i_vcl].append(i_cur_ride)
        selected_rides.add(i_cur_ride)

with open(fout, 'w') as f:
    for i, vcl in enumerate(VclRides):
        ride_ls = ' '.join([str(i_ride) for i_ride in vcl])
        f.write(f'{len(vcl)} {ride_ls} \n')