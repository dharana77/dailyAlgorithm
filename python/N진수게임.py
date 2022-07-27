# 9:43


def solution(n, t, m, p):
    answer = ''
    end_number = (t * m) + 1
    
    total_rank = 1
    inputted_count = 0
    targets = []
    # print("test, ", get_divided_by_n(15,16))
    for number in range(end_number*2):
        # print(number)
        if inputted_count >= t:
            break
        # print("number", number, n)
        divided = get_divided_by_n(number, n)
        # print(divided)
        
        for target in divided:
            rank = (total_rank-1)%m + 1
            # print("total_rank:", total_rank)
            if rank == p:
                # print("target:", target)
                
                if inputted_count >= t:
                    break
                
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
        return [convert_number(str(number))]
    # print(number, n)
    
    while number!=0:
        temp = number%n
        # print(temp)
        number = int(number/n)
        temp = convert_number(str(temp))
        # print(temp)
        re += str(temp)
        #31
        # 0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F,10,11,12,13,14,15,16,17,18,19,1A,1B,1C,1D,1E,1F,20,21
    return re[::-1]


def convert_number(number_str):
    number = int(number_str)
    alpha_lists = ["A", "B", "C", "D", "E", "F"]
    if number >= 10 and number <= 15:
        return alpha_lists[number - 10]
    return number_str