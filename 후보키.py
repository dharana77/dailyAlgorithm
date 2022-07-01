from itertools import combinations
from collections import defaultdict

def solution(relation):
    answer = 0
    for count in range(1,len(relation[0])+1):
        predictable_combination_length = len(list(combinations(relation[0], count)))
        for i in range(predictable_combination_length):
            count_table = defaultdict(int)
            for idx, _ in enumerate(relation):
                pred_combinations = list(combinations(relation[idx], count))
                count_table[pred_combinations[i]]+=1
            con = True
            # print(count_table)
            for _, value in enumerate(count_table):
                if value!= 1:
                    con = False
            if con:
                answer+=1
                
    return answer