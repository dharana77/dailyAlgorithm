from collections import defaultdict

answer = 0

def solution(want, number, discount):
    
    total = sum(number)
    for idx, dis in enumerate(discount):
        if (idx + total -1) < len(discount):
            is_want_suitable(idx, discount, want, number)

    return answer


def is_want_suitable(start, discount, want, number):
    global answer
    discount_table = defaultdict(int)
    total_count = sum(number)

    for idx in range(total_count):
        target = discount[start+idx]
        discount_table[target]+=1
    
    answer_count = defaultdict(int)
    for idx, wa in enumerate(want):
        answer_count[wa] = number[idx]
    
    # print("discount_table")
    # print(discount_table)
    # print("answer_table")
    # print(answer_count)
    if discount_table == answer_count:
        answer+=1
