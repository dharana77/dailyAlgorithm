from itertools import combinations

def solution(n):
    answer = 0
    targets = [i for i in range(1,n+1)]

    for i in range(1, n+1):
        target = list(combinations(targets, i))
        # print(target)
        for j in target:
            if is_can_be_eat(j):
                answer+=1
    # n + 
    # 3     4.         5
    # 1 3.  13 14 24.   13 4 5. 245 35
    return answer


def is_can_be_eat(current):
    current = list(current)

    for idx, target in enumerate(current):
        if idx != len(current) - 1:
            if abs(current[idx] - current[idx+1]) == 1:
                return False
    return True
