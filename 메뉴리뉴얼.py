from itertools import combinations

from collections import defaultdict

def solution(orders, course):
    answer = []
    count_dict = defaultdict(int)
    for num in course:
        for order in orders:
            all_lists = list(combinations(order, num))
            
            for current in all_lists:
                current = sorted(current)
                target = ""
                for cu in list(current):
                    target += cu
                
                count_dict[target]+=1
    # print(count_dict)
    for num in course:
        mx = 0
        target_dict = defaultdict(int)
        for key, value  in count_dict.items():
            if len(key) == num:
                target_dict[key] = value
                if mx < value:
                    mx = value
        for key, value in target_dict.items():
            if mx == value:
                if value>1:
                    answer.append(key)
    return sorted(answer)