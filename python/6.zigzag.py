class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        answer = ["" for i in range(numRows)]
        if numRows==1:
            return s
        dir = "down"
        ct = 0
        #스트링 하나하나씩
        for j in range(len(s)):
            #방향 전환
            if j!=0 and (j % (numRows-1)) == 0:
                if dir == "down":
                    dir = "up"
                else:
                    dir = "down"
                    
            #최고로우길이까지
            if dir == "down":
                answer[ct]+=s[j]
                ct+=1
            elif dir == "up":
                answer[ct]+=s[j]
                ct-=1
                
        temp = ""
        for i in answer:
            print(i)
            temp+=i
        return temp