t = int(input())
 
for i in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    # print(nums)
    
    pres = [0] * len(nums)
    pres[0] = nums[0]
    for idx in range(1, len(nums)):
        pres[idx] = max(pres[idx-1], nums[idx])
        # nums[idx] if nums[idx] > nums[idx-1] else nums[idx-1]
    
    posts = [0] * len(nums)
    posts[-1] = nums[-1]
    for idx in range(len(nums)-2, 0, -1):
        # print(idx)
        posts[idx] = max(posts[idx+1], nums[idx])
        # nums[idx] if nums[idx] > nums[idx+1] else nums[idx+1]
    
    ans = "YES"

    # print(pres)
    # print(posts)
    for idx in range(1, len(nums)-1):
        # print(pres[0], posts[0])
        if pres[idx] > nums[idx] and posts[idx] >nums[idx]:
            ans = "NO"
            break
    print(ans)
