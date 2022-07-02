#2:12
#3:37
def solution(gems):
    answer = []
    unique = set()
    unique_count = []
    for g in gems:
        unique.add(g)
        unique_count.append(len(unique))
    mx = max(unique_count)
    mx_idx = -1
    mn = 1e5
    temp_count = set()
    i =0
    j =1
    while i < len(gems) and j <=len(gems):
        target = gems[i:j]
        # print(i,j, target)
        if len(set(target)) == mx:
            if (j-i)<mn:
                # print("ans",i+1,j)
                mn = j-i
                answer = [i+1,j]
            i+=1
        else:
            j+=1
    return answer