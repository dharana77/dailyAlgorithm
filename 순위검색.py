from collections import defaultdict
from bisect import bisect_left

def solution(info, query):
    answer = []
    #cpp, java, python
    #backend, frontend
    #junior, senior
    #chicken, pizza
    hash_map = defaultdict(list)
    for inf in info:
        inf = inf.split(" ")
        language = inf[0]
        position = inf[1]
        title = inf[2]
        soul = inf[3]
        score = inf[4]
        lan = ["-"] if language == "-" else ["-", language]
        pos = ["-"] if position == "-" else ["-", position]
        tit = ["-"] if title =="-" else ["-", title]
        so = ["-"] if soul == "-" else ["-", soul]
        
        for a in lan:
            for b in pos:
                for c in tit:
                    for d in so:
                        key = a + b + c + d
                        hash_map[key].append(int(score))
    for key in hash_map:
        hash_map[key] = sorted(hash_map[key])
        
    for q in query:
        q = q.split(" ")
        # print(q, len(q))
        language = q[0]
        position = q[2]
        title = q[4]
        soul = q[6]
        score = int(q[7])
        ct = 0
        # print("q:", q)
        
        ct = 0
        key = language + position + title + soul
        target = hash_map[key]
        # print(target)
        ln = len(target)
        # print(target)
        x = bisect_left(target, int(score))
        # if ln-x>0:
        #     print("플러스", ln-x, "x", x)
        ct += (ln - x)
        answer.append(ct) 
    return answer