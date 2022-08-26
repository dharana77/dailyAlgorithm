from collections import deque

def solution(n, paths, gates, summits):
    summits.sort()

    q = deque([])

    dist = [float("inf")] * (n + 1)
    weights = [[] for i in range(n+1)]
    
    for p in paths:
        start = p[0]
        end = p[1]
        w = p[2]
        weights[start].append((end,w))
        weights[end].append((start,w))

    for g in gates:
        q.append(g)
        dist[g] = 0
    
    while q:
        node = q.popleft()

        if node in summits:
            continue

        for next_node, w in weights[node]:
            temp_w = max(dist[node], w)
            if dist[next_node] <= temp_w:
                continue
            dist[next_node] = temp_w
            q.append(next_node)

    answer = []
    ans_node, min_w = -1, 1e9
    for s in summits:
        if dist[s] < min_w:
            min_w = dist[s]
            ans_node = s
    answer.append(ans_node)
    answer.append(min_w)
    return answer

