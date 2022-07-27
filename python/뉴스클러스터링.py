
def solution(str1, str2):
    '''
    https://programmers.co.kr/learn/courses/30/lessons/17677
    풀이
    '''
    answer = 0
    str1_list = []
    str2_list = []
    str1_temp = str1[:-1]
    for idx, _ in enumerate(str1_temp):
        if str1[idx].isalpha() and str1[idx+1].isalpha():
            str1_list.append(str1[idx:idx+2])
    
    str2_temp = str2[:-1]
    for idx, _ in enumerate(str2_temp):
        if str2[idx].isalpha() and str2[idx+1].isalpha():
            str2_list.append(str2[idx:idx+2])
    
    str1_list = sorted(str1_list)
    str2_list = sorted(str2_list)
    str1_list = [i.lower() for i in str1_list]
    str2_list = [i.lower() for i in str2_list]
    # print(str1_list ,str2_list)
    
    if str1_list == str2_list:
        return 65536
    
    same_space = defaultdict(int)
    union = defaultdict(int)
    
    str1_count_dict = defaultdict(int)
    str2_count_dict = defaultdict(int)
    for _, str1_value in enumerate(str1_list):
        str1_count_dict[str1_value]+=1
        
    for idx2, str2_value in enumerate(str2_list):
        str2_count_dict[str2_value]+=1
    # print(str1_count_dict, str2_count_dict)
    
    total_str_list = str1_list+str2_list
    # print(total_str_list)
    for idx, s in enumerate(total_str_list):
        if same_space[s]==0:
            same_space[s] = min(str1_count_dict[s], str2_count_dict[s])
        if union[s]==0:
            union[s] = max(str1_count_dict[s], str2_count_dict[s])
    # print(same_space)
    # print(union)
    answer = int(sum(same_space.values())/sum(union.values())*65536)
    return answer