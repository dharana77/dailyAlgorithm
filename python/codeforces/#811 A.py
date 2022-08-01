t = int(input())
 
for i in range(t):
    n, h, m = map(int, input().split())
    target_minutes = 60* h + m
 
    mn = 24*60;
    # print(n)
    for _ in range(n):
        nh, nm = map(int, input().split())
        alaram_minutes = nh * 60 + nm
        # print(alaram_minutes, target_minutes)
        
        if alaram_minutes >= target_minutes:
            can_sleep_hours = (alaram_minutes - target_minutes)
        else:
            can_sleep_hours = 24*60 - target_minutes + alaram_minutes
        
        if mn > can_sleep_hours:
                mn = can_sleep_hours    
    
    answer = str(int(mn/60)) + " " + str(mn%60)
    print(answer)