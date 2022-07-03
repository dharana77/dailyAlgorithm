from collections import defaultdict


def solution(user_id, banned_id):
    answer = 0
    banned_set = set()
    bid_dict = defaultdict(set)
    visited = {}
    for bid in banned_id:
        for uid in user_id:
            if is_same_format(bid, uid) :
                bid_dict[bid].add(uid)
                visited[bid + ":" + uid] = False
                
    lst = [value for key, value in bid_dict.items()]
    total_result = set()
    
    # print(bid_dict)
    while True:
        visited_ct = 0
        for v in visited.values():
            if v:
                visited_ct+=1
        if visited_ct == len(visited):
            break
        
        result = set()
        for bid in banned_id:
            # print(bid)
            for value in bid_dict[bid]:
                if not visited[bid+":"+value] and value not in result:
                    print(bid,value)
                    result.add(value)
                    visited[bid+":"+value]=True
                    break
        
        total_result.add(tuple(result))
    answer= len(total_result)
    return answer

def is_same_format(bid: str, uid: str):
    if len(bid) != len(uid):
        return False
    for idx, bstr in enumerate(bid):
        if bid[idx]!=uid[idx]:
            if bid[idx]!='*' and uid[idx]!='*':
                return False
    return True