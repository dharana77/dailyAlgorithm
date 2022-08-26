
from collections import defaultdict

#푸는 중
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
        dfs(gate, gates, summits, gate, visited, 0, 0, False, [])
    return answer


def dfs(start, starts, ends, first_started, visited, mx, ln, arrived, paths):
    print("start", start)
    visited[start] = 1
    ln+=1
    paths.append(start)
    print(paths)
    if start in ends:
        arrived = True
    
    if arrived and start == first_started:
        if len(answer) == 0:
            answer.append(ln)
            answer.append(mx)
        else:
            if mx < answer[1]:
                answer[1] = mx
                answer[0] = ln
            elif mx == answer[1]:
                answer[1] = mx
                if answer[0] > ln:
                    answer[0] = ln
        return
    
    for nexts in dist[start]:
        nx = list(nexts)[0]
        if nx in starts:
            continue
        w = nexts[nx]
        if visited[nx] != 1:
            if w > mx:
                mx = w
            dfs(nx, starts, ends, first_started, visited, mx, ln, arrived, paths)
            visited[nx] = 0
            paths = paths[:-1]
    
    