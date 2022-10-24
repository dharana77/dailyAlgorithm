from itertools import combinations
from collections import Counter

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        ans = 0
        
        #O(n)*m (16*26)
        for i in arr:
            target = Counter(i)
            con = True
            for t in target:
                if target[t] > 1:
                    con = False
                    break
            if con and len(i) > ans:
                ans = len(i)
        
        #16(n)
        for i in range(1, len(arr)+1):
            lst = combinations(arr, i)
            
            #16C8
            for target in lst:
                # print(target)
                counters = []
                a = Counter()
                
                #16
                for t in target:
                    counters.append(Counter(t))
                    a = a + Counter(t)
                
                go_out = False
                
                #26
                for j in a:
                    if a[j] > 1:
                        go_out = True
                        break
                
                #16
                if not go_out and len("".join(i for i in target)) > ans:
                    ans = len("".join(i for i in target))
        return ans
