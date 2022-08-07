t = int(input())
 
for i in range(t):
    n = int(input())
    numbers = []
    mn_x = 0
    mn_y = 0
    mx_x = 0
    mx_y = 0
    ans = 0
    for j in range(n):
        x, y = map(int, input().split(" "))
        if x>0 and mx_x<x:
            mx_x = x
        elif x<0 and mn_x>x:
            mn_x = x
        if y>0 and mx_y < y:
            mx_y = y
        elif y< 0 and mn_y > y:
            mn_y = y
    
    ans = mx_x + mx_y + abs(mn_x) + abs(mn_y)
    print(ans * 2)