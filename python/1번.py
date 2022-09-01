import math
import os
import random
import re
import sys
import time
from bisect import bisect_left

def getMaxBarrier(initialEnergy, th):
# Write your code here
    mx = max(initialEnergy)
    ans = -1
    print(sum(initialEnergy))
    
    initialEnergy = sorted(initialEnergy)
    print(initialEnergy)
    ln = len(initialEnergy) - 1
    current = (initialEnergy[ln] - initialEnergy[0])//2
    print("current", current)
    test = find_first_minus(initialEnergy, th, 0, ln, current)
    print(test, initialEnergy[test])

def find_first_minus(initialEnergy, th, start, end, current):
    idx = bisect_left(initialEnergy, current)
    total = sum(initialEnergy[idx:])
    print(idx)
    while start <= end:
        if total < th:
            current = initialEnergy[(start + idx)//2]
            find_first_minus(initialEnergy, th, start, idx, current)
        else:
            current = initialEnergy[(idx + end)//2]
            find_first_minus(initialEnergy, th, idx, end, current)
    
    return idx



start = time.time()
# [2,4,5,10,13]
arr = [4,5,2,13,10]
test = getMaxBarrier(arr, 8)
# arr = [1000000000] * (10 ** 5)
# test = getMaxBarrier(arr, 100)
print(test)
end = time.time()
print(end - start)

#정렬 미리 해두고
#안쪽에서는 이진 탐색으로 들어갈 자리 파악하고
#들어갈자리부터 양수이므로 해당 값부터 다 더하면
