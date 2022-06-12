def solution(s):
    answer = len(s)
    for ln in range(2,len(s)):
        temp_string = ""
        start = 0
        same_string_count = 1
        for start in range(0,len(s),ln):
            if start+ln*2 <= len(s):
                if s[start:start+ln] == s[start+ln:start+ln*2]:
                    same_string_count+=1
                else:
                    if same_string_count !=1:
                        temp_string+=s[start:start+ln]+str(same_string_count)
                    else:
                        temp_string+=s[start:start+ln]
                    same_string_count = 1
            else:
                temp_string+=s[start:start+ln]    
        print(temp_string)
    return answer