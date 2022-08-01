from collections import defaultdict
 
t = int(input())
 
for i in range(t):
    n = int(input())
 
    nums = list(map(int, input().split()))
    
    num = reversed(nums)
    num_count = defaultdict(int)
    ln = len(nums)
    ct = 0
 
    for i in num:
        if num_count[i] == 0:
            num_count[i]+=1
        else:
            break
        ct+=1
    
    answer = ln - ct
    print(answer)