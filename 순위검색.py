def solution(info, query):
    answer = []
    #cpp, java, python
    #backend, frontend
    #junior, senior
    #chicken, pizza
    for q in query:
        q = q.split(" ")
        # print(q, len(q))
        language = q[0]
        position = q[2]
        title = q[4]
        soul = q[6]
        score = q[7]
        ct = 0
        print("q:", q)
        
        for inf in info:
            inf = inf.split(" ")
            # print(inf, len(inf))
            inf_language = inf[0]
            inf_position = inf[1]
            inf_title = inf[2]
            inf_soul = inf[3]
            inf_score = inf[4]
            con = True
            if language != '-':
                if language!=inf_language:
                    con = False
                    continue 
            if position != '-':
                if inf_position!=position:
                    con = False
                    continue
            if title != '-':
                if inf_title != title:
                    con = False
                    continue
            if soul!='-':
                if inf_soul != soul:
                    con = False
                    continue
            if int(score)<=int(inf_score):
                ct+=1
                # print(inf, ct)
        answer.append(ct) 
    return answer