scores = {"R":0 , "T":0, "C":0, "F":0, 
              "J":0, "M":0, "A":0, "N":0}
    
    
def solution(survey, choices):
    answer = ''
    
    for idx, s_value in enumerate(survey):
        choice = choices[idx]
        getValue(s_value, choice)
    
    ks = list(scores.keys())
    vs = list(scores.values())
    
    for i, k in enumerate(ks):
        if i%2 == 0:
            if vs[i] < vs[i+1]:
                max_idx = i+1
            else:
                max_idx = i
            answer += ks[max_idx]
    
    return answer


def getValue(s_value, choice):
    if choice == 1:
        target = s_value[0]
        scores[target] += 3
    elif choice == 2:
        target = s_value[0]
        scores[target] += 2
    elif choice == 3:
        target = s_value[0]
        scores[target] += 1
    elif choice ==5:
        target = s_value[1]
        scores[target] += 1
    elif choice == 6:
        target = s_value[1]
        scores[target] += 2
    elif choice == 7:
        target = s_value[1]
        scores[target] += 3
        