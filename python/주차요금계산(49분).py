#7:08~ 7:57
from collections import defaultdict

def solution(fees, records):
    answer = []
    cars = defaultdict(list)
    car_cost = defaultdict(int)
    
    for record in records:
        time, car, state = record.split(" ")
        cars[car].append(time)
        
    for car in cars:
        key = car
        values = cars[car]
        cost = 0
        spend_time = 0 
        for idx, time in enumerate(values):
               
            # print(idx,time)
            if idx%2==0:
                if len(values) > idx + 1:
                    spend_time += get_time_to_minutes(values[idx+1]) - get_time_to_minutes(time)
                elif idx == len(values)-1:
                    spend_time += (23*60 + 59) - get_time_to_minutes(time)  
                # print("spend", spend_time)
        cost += get_cost(spend_time, fees)
        car_cost[car] = cost
    
    car_cost = sorted(car_cost.items(), key= lambda item : item[0])
    answer = [i[1] for i in car_cost]
    return answer


def get_time_to_minutes(times):
    hours, minutes = times.split(":")
    return int(hours)*60+ int(minutes)


def get_cost(spend_time, fees):
    if spend_time <= fees[0]:
        return fees[1]
    else:
        if (spend_time-fees[0])%fees[2] == 0:
            return fees[1] + int((spend_time-fees[0])/fees[2]) * fees[3]
        else:
            return fees[1] + (int((spend_time-fees[0])/fees[2])+1) * fees[3]