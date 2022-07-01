from itertools import combinations
from collections import defaultdict

def solution(relation):
    answer = 0
    for count in range(1,len(relation[0])+1):
        predictable_combination_length = len(list(combinations(relation[0], count)))
        pred_combs_indexes = list(combinations(range(len(relation[0])), count))
        # print(pred_combs_indexes)
        to_delete_values = []
        for i in range(predictable_combination_length):
            count_table = defaultdict(int)
            index_table = defaultdict(tuple)
            for idx, _ in enumerate(relation):
                pred_combinations = list(combinations(relation[idx], count))
                count_table[pred_combinations[i]]+=1
                # print(pred_combinations[i], type(pred_combs_indexes[i]))
                index_table[pred_combinations[i]]=pred_combs_indexes[i]
                
            con = True
            # print(count_table)
            for _, key in enumerate(count_table):
                if count_table[key]!= 1:
                    con = False
            print(count_table)
            if con:
                for idx, key in enumerate(index_table):
                    new_relation = []
                    for j in range(len(relation[idx])):
                        if j not in index_table[key]:
                            new_relation.append(relation[idx][j])
                    print(relation[idx], new_relation)
                    # relation[idx] = new_relation
                    
                answer+=1
                
    return answer