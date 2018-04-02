def sort_index(ls):
    sorted_ls = sorted(ls, reverse=True)
    sorted_idx = sorted(range(len(ls)), key= lambda k: ls[k], reverse=True)
    return (sorted_ls, sorted_idx)

def idx2char(idxs):
    return [chr(ord('A')+idx) for idx in idxs]

def evac_to(P, idx, target, plan):
    while P[idx] > target:
        if P[idx] - target >= 2: n_evac = 2 
        else: n_evac = 1
        plan.append(idx2name[idx]*n_evac)
        P[idx] -= n_evac

def evac_biggest(P, plan):
    evac_to(P, 0, P[1], plan)

def evac_all_small(P, plan):
    for i in range(len(P)-1, 1, -1):
        evac_to(P, i, 0, plan)

def evac_two_biggest(P, plan):
    while P[0] > 0:
        plan.append(idx2name[0]+idx2name[1])
        P[0] -= 1

idx2name = []
t = int(input())
for i in range(t):
    n = int(input())
    P = []
    P = list(map(int, input().split()))
    P, idx_order = sort_index(P)
    idx2name = idx2char(idx_order)
    plan = []
    evac_biggest(P, plan)
    evac_all_small(P, plan)
    evac_two_biggest(P, plan)
    plan_str = ' '.join(plan)
    print('Case #{}: {}'.format(i+1, plan_str))
