class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x = str(x)
        minus = False
        if x[0]=="-":
            minus = True
            x = x[1:]
        x = x[::-1]
        print(x)
        answer = ""
        start_index = 0
        if x[0] == "0":
            print(x)
            for i in range(len(x)):
                if x[i]!="0":
                    start_index = i
                    answer = x[start_index:]
                    
                    break
            
        else:
            answer = x
        if x=="0":
            return 0
        
        if minus:
            answer = "-" + answer
        
        if (int(answer)>(2**31)-1) or (int(answer)<-(2**31)):
            answer = 0
        return answer
        