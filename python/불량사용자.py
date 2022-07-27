from itertools import permutations

def solution(user_id, banned_id):
    answer = 0
    all_lists = list(permutations(user_id, len(banned_id)))
    
    banned_set = set()
    for per in all_lists:
        con, per = check(per,banned_id,banned_set)
        # print("per",per)
        if con:
            # print("sec per", per)
            banned_set.add(tuple(per))
    # print(banned_set)
        # print("why")
    answer = len(banned_set)
    return answer

def check(per, banned_id, banned_set):
    for idx, p in enumerate(per):
        if not compare(p, banned_id[idx]):
            return False, per
    per = set(sorted(list(per)))
    if len(per & banned_set)!=0:
        return False, per
    
    return True, per

def compare(p, banned_id):
    if len(p)!= len(banned_id):
        return False
    for idx, v in enumerate(p):
        if v!=banned_id[idx]:
            if banned_id[idx]!="*":
                return False
    return True