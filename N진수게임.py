# 9:43 ~ 10:21

def solution(n, t, m, p):
    answer = ''
    end_number = (t * m) + 1
    
    total_rank = 1
    inputted_count = 0
    targets = []
    
    for number in range(end_number):
        # print(number)
        if inputted_count >= t:
            break
        divided = get_divided_by_n(number, n)
        # print(divided)
        
        for target in divided:
            rank = (total_rank-1)%m + 1
            # print("total_rank:", total_rank)
            if rank == p:
                # print("target:", target)
                
                if inputted_count >= t:
                    break
                
                target = convert_number(target)
                targets.append(target)
                inputted_count+=1
            total_rank+=1 
            # print(target)
    answer = "".join(targets)
    return answer


def get_divided_by_n(number, n):
    re = ""
    if number == 0:
        return "0"
    if number < n:
        return [str(number)]
    # print(number, n)
    
    while number!=0:
        temp = number%n
        # print(temp)
        number = int(number/n)
        re += str(temp)
        
    return re[::-1]


def convert_number(number_str):
    number = int(number_str)
    alpha_lists = ["A", "B", "C","D","E", "F"]
    if number >= 10 and number <= 15:
        return alpha_lists[number - 10]
    return number_str