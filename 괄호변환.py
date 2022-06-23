def solution(p):
    answer = ''
    correct_p = check_balance(p)
    
    if correct_p:
        return p
    
    if p == "":
        return answer
    
    u, v = split_string(p)
    # print("u",u,"v",v)
    if check_balance(u):
        answer = u + solution(v)
        return answer
    else:
        answer+="("
        answer+=solution(v)
        answer+=")"
        # print("answer",answer)
        u = u[1:-1]
        temp = ""
        for j in u:
            if j =="(":
                temp+=")"
            else:
                temp+="("
        u = temp
        # print("u",u)
        answer += u
        return answer


def split_string(p):
    u = ""
    v = ""
    print(p)
    left_count = 0
    right_count = 0
    for i in p:
        if left_count>0 and (left_count == right_count):
            v+=i
        elif i == "(":
            left_count+=1
            u+=i
        elif i== ")":
            right_count+=1
            u+=i
        # print(u, left_count, right_count)
    # print("uv",u,v)
    return u, v


def check_balance(p):
    q = []
    con = True
    for i in p:
        if i == '(':
            q.append(i)
        else:
            if len(q)>0:
                q.pop()
            else:
                con = False
                break
    return con