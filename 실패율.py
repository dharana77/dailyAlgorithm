from collections import defaultdict

def solution(N, stages):
    answer = [0 for i in range(N)]
    
    stage_reached_uncleared = 0
    stage_reached = 0
    stages = sorted(stages)
    
    ct = 1
    total = len(stages)
    for idx in range(len(stages)-1):
        if stages[idx] == stages[idx+1]:
            ct+=1
        else:
            # print(stages[idx]-1)
            if stages[idx]-1 < N:
                answer[stages[idx]-1] = ct/total
                # print("stages", stages[idx]-1, ct, total)
                total-=ct
                ct = 1
    ct = 0
    total = len(stages)
    for idx, value in enumerate(stages):
        if stages[-1] == stages[idx]:
            ct+=1
        else:
            total-=1
    if stages[-1]<=N:
        answer[stages[-1]-1] = ct/total
    test = defaultdict(int)
    for idx, value in enumerate(answer):
        test[idx] = value
    
    test = sorted(test.items(), key= lambda item: item[1] , reverse=True)
    print(test)
    answer = [i[0]+1 for i in test]
    return answer