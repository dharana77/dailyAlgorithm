def solution(s):
    answer = len(s)
    for ln in range(1,len(s)):
        temp_string = ""
        start = 0
        same_string_count = 1
        while (start+2*ln) <= len(s):
            if s[start:start+ln] == s[start+ln:start+2*ln]:
                same_string_count+=1
            else:
                temp_string+=s[start:start+ln]
                if same_string_count != 1:
                    temp_string += str(same_string_count)
                same_string_count=1
            start+=ln
        temp_string += s[start:]
        if same_string_count!=1:
            temp_string+= str(same_string_count)
        # print(start, ln, temp_string)
        if len(temp_string)<answer:
            answer = len(temp_string)
    return answer