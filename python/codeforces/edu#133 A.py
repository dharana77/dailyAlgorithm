t = int(input())
 
 
for i in range(t):
    n = int(input())
    if n==1:
        print(2)
        continue
    if n==2 or n==3:
        print(1)
        continue
    ans = int((n-1)/3) +1
    print(ans)
 
 
# 1 2 3 4 5 6 7 8 9 10 11 12 13
# 2  1 1 2 2 2 3 3 3 4   4  4  5