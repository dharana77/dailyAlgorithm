t = int(input())
 
for i in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    # print(nums)
    mn = min(nums)
    ans = "YES"
    for j in range(1,len(nums)-1):
        if nums[j] == mn:
            ans = "NO"
            break
    print(ans)