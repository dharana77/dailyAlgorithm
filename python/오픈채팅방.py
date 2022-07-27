def solution(record):
    answer = []
    nickname_by_id = {}
    for re in record:
        commands = re.split(" ")
        state = commands[0]
        
        if state == "Enter" or state == "Change":
            user_id = commands[1]
            user_nickname = commands[2]
            nickname_by_id[user_id] = user_nickname
        
    
    for re in record:
        commands = re.split(" ")
        state = commands[0]
        if state == "Enter":
            user_id = commands[1]
            user_nickname = commands[2]
            phrase = nickname_by_id[user_id]+"님이 들어왔습니다."
            answer.append(phrase)
        elif state == "Leave":
            user_id = commands[1]
            phrase = nickname_by_id[user_id]+"님이 나갔습니다."
            answer.append(phrase)
    return answer