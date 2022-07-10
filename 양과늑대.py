#10:26 ~
from collections import defaultdict, deque
from copy import deepcopy

is_wolf = list()
num_to_edges = defaultdict(list)
max_sheep = 0


def find_max_recursive(current_loc, nsheep, nwolf, can_go):
    global max_sheep
    if is_wolf[current_loc]:
        nwolf+=1
    else:
        nsheep+=1
        max_sheep = max(max_sheep, nsheep)
        
    if nsheep <= nwolf:
        return
    
    can_go.extend(num_to_edges[current_loc])
    for next_loc in can_go:
        find_max_recursive(next_loc, nsheep, nwolf, can_go=[loc for loc in can_go if loc!= next_loc])
                           
                           
def solution(info, edges):
    global is_wolf, num_to_edges, max_sheep
    is_wolf = info
    
    for edge_from, edge_to in edges:
        num_to_edges[edge_from].append(edge_to)
    print(num_to_edges)
    for i, v in num_to_edges.items():
        print(i,":",v)
    find_max_recursive(0, 0, 0, [])
    
    return max_sheep