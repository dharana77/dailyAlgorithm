## 시간초과
def solution(queue1, queue2):
    answer = 0
    tot = 0
    mx = 0
    a_tot = 0
    b_tot = 0 
    
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
    
    if answer != -1:
        while a_tot != b_tot:
            if a_tot > b_tot:
                target = queue1[0]
                queue1 = queue1[1:]
                queue2.append(target)
                a_tot -= target
                b_tot += target
                
            elif b_tot > a_tot:
                target = queue2[0]
                queue2 = queue2[1:]
                queue1.append(target)
                a_tot += target
                b_tot -= target
                
            answer+=1
    
    return answer