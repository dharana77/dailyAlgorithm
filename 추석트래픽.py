
def solution(lines):
    answer = 0
    logs = []
    max_end_time = 0
    
    # print(round(3604.002 + 0.999 +0.5, 3))
    for line in lines:
        end_time = line.split(" ")[1]
        duration = float(line.split(" ")[2][:-1])
        
        hour = int(end_time.split(":")[0])
        minute = int(end_time.split(":")[1])
        second = float(end_time.split(":")[2])
        
        end_time_by_second = 3600*(hour) + 60*minute + second
        start_time_by_second = end_time_by_second - (duration) + 0.001
        logs.append({"start":start_time_by_second, "end":end_time_by_second})
    
    time = 0
    # print(logs)
    for log in logs:
        log_start_time = log["start"]
        log_end_time = log["end"]
        
        
        times = [log_start_time, log_end_time]
        for i in range(2):
            current_start_time = times[i]
            current_end_time = round(times[i] + 0.999,3)
            count = 0
            for line in lines:
                is_start_time_in = False
                is_end_time_in = False
                end_time = line.split(" ")[1]
                duration = float(line.split(" ")[2][:-1])
                hour = int(end_time.split(":")[0])
                minute = int(end_time.split(":")[1])
                second = float(end_time.split(":")[2])

                line_end_time = 3600*(hour) + 60*minute + second
                line_start_time = line_end_time - (duration) + 0.001
                # print(current_start_time , current_end_time)
                # print(line_start_time, line_end_time)
                is_in = False
                #start time~1 체크
                if (not (current_end_time < line_start_time) and not(current_start_time > line_end_time)):
                    is_in = True
                # print(current_end_time < line_start_time, current_start_time > line_end_time)
                # print(is_in)
                if(is_in):
                    count+=1
            # print("카운트", count)
            if count>answer:
                answer = count
    return answer