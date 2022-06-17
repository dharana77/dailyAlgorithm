def solution(lines):
    answer = 0
    logs = []
    max_end_time = 0
    
    for line in lines:
        end_time = line.split(" ")[1]
        duration = float(line.split(" ")[2][:-1])
        
        hour = int(end_time.split(":")[0])
        minute = int(end_time.split(":")[1])
        second = float(end_time.split(":")[2])
        
        end_time_by_second = 3600*(hour) + 60*minute + second
        start_time_by_second = end_time_by_second - (duration) + 1
        logs.append({"start":start_time_by_second, "end":end_time_by_second})
    
    time = 0
    
    for log in logs:
        log_start_time = log["start"]
        log_end_time = log["end"]
        
        is_start_time_in = False
        is_end_time_in = False
        count = 0
        for line in lines:
            end_time = line.split(" ")[1]
            duration = float(line.split(" ")[2][:-1])
            hour = int(end_time.split(":")[0])
            minute = int(end_time.split(":")[1])
            second = float(end_time.split(":")[2])

            line_end_time = 3600*(hour) + 60*minute + second
            line_start_time = end_time_by_second - (duration) + 1
            
            #start time~1 체크
            if not (log_start_time + 1 < line_start_time) and not (log_start_time > line_end_time):
                is_start_time_in = True
            #end_time~1체크
            if not (log_end_time +1 < line_start_time) and not (log_end_time > line_end_time):
                is_end_time_in = True
            if(is_start_time_in or is_end_time_in):
                count+=1
        if count>answer:
            answer = count
    return answer