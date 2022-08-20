## list를 디큐로 변경해서 빨라졌으나 변경된 시간복잡도 계산과
## 목표값을 target으로 잡아 한쪽에서만 빼고 변경하는 부분
## 왜 mx_len * 2 + 2 보다 클때인지
from collections import deque
[1,1,10,1,] 1, 
[2,2,1,2,], 3 +3 

[]

def solution(queue1, queue2):
    answer = 0
    tot = 0
    mx = 0
    a_tot = 0
    b_tot = 0 
    mx_len = max(len(queue1), len(queue2))
    
    for a in queue1:
        tot += a
        a_tot += a
        if mx < a:
            mx = a
    for b in queue2:
        tot += b
        b_tot += b
        if mx < b:
            mx = b
            
    div_target = tot/2
    if mx > div_target or div_target %1 !=0:
        answer = -1
        return answer
    
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    
    while a_tot != b_tot:
        if a_tot > b_tot:
            target = queue1.popleft()
            queue2.append(target)
            a_tot -= target
            b_tot += target

        elif b_tot > a_tot:
            target = queue2.popleft()
            queue1.append(target)
            a_tot += target
            b_tot -= target

        elif a_tot == b_tot:
            return answer
        answer+=1
        if answer > mx_len * 2 + 2: #아직 이해 못한부분
            return -1
    
    return answer