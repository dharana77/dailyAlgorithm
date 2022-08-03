from collections import defaultdict
 
t = int(input())

for i in range(t):
    n = int(input())
    #greedy로 풀면 됌
    
    answer = ""
    for j in range(9,0,-1):
        # print("j:" + str(j))
        if n>=j:
            n-=j
            answer = str(j) + answer
    
    print(answer)
    