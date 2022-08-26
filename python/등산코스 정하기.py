
from collections import defaultdict

answer = []
dist = defaultdict(list)

def solution(n, paths, gates, summits):
    
    for path in paths:
        x = path[0]
        y = path[1]
        w = path[2]
        dist[x].append({y: w})
        dist[y].append({x: w})
    
    visited = [0] * (n + 1)
    
    for gate in gates:
        dfs(gate, gates, summits, visited, 0)
    return answer


def dfs(start, starts, ends, visited, mx):
    # print("start", start)
    visited[start] = 1
    
    if start in ends:
        if len(answer) == 0:
            answer.append(start)
            answer.append(mx)
        else:
            if mx < answer[1]:
                answer[1] = mx
                answer[0] = start
            elif mx == answer[1]:
                if answer[0] > start:
                    answer[0] = start
        return
    
    
    for nexts in dist[start]:
        nx = list(nexts)[0]
        if nx in starts:
            continue
        w = nexts[nx]
        if visited[nx] != 1:
            temp_mx = mx
            if w > mx:
                mx = w
            dfs(nx, starts, ends, visited, mx)
            visited[nx] = 0
            mx = temp_mx
    