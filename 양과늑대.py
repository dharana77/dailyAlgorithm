#1차 12:53~01:32(40분)
from collections import defaultdict
from copy import deepcopy

answer = 0
wolves = list()
nodes = defaultdict(list)
visited = list()

def solution(info, edges):
    global answer
    global wolves
    global nodes
    global visited
    
    wolves = info
    visited = [0]* (len(info) + 1)
    # print(wolves)
    for edge in edges:
        start = edge[0]
        end = edge[1]
        nodes[start].append(end)
    # print(nodes)
    # print(len(visited))
    visit_node(0,0,0, [])
    return answer


def visit_node(start, sheep_count, wolf_count, nexts):
    global wolves
    global nodes
    global answer
    global visited
    # print(start, wolves)
    print("Start", start)
    # visited[start] = 1
    if wolves[start] == 0:
        sheep_count+=1
        print(sheep_count)
    else:
        wolf_count+=1
    
    if wolf_count >= sheep_count:
        return
    
    if answer < sheep_count:
        answer = sheep_count
    
    nexts.extend(nodes[start])
    
    for next_node in nexts:
        # if visited[next_node]!=1:
        visit_node(next_node, sheep_count, wolf_count, nexts)
        
    