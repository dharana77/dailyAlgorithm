def solution(key, lock):
    answer = True
    move_times = [0,1,2,3]
    
    for move_idx, move_time in enumerate(move_times):
        # print(move_time)
        temp_key = move_key(key, move_time)
        # print(temp_key)
        # for l_idx, l_value in enumerate(lock):
        #     for idx, value in enumerate(lock[l_idx]):
        #         print("")
    return answer

def move_key(key, move_time):
    if move_time == 0:
        return key
    
    # print(temp_key)
    while move_time:
        temp_key = [[0 for i in range(len(key))] for i in range(len(key))]
        # print(move_time)
        for i, _ in enumerate(key):
            for j, _ in enumerate(key[i]):
                temp_key[j][len(key[i])-1-i] = key[i][j]
                # print(i,j, temp_key)
        key = temp_key
        move_time-=1
    return key
