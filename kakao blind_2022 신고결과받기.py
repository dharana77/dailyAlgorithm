def solution(id_list, report, k):
    answer = []
    final_reported_dict = {id:0 for id in id_list}
    final_banned_list = {id:0 for id in id_list}
    report.sort()
    #id_list에 존재하는 id마다
    for target in id_list:
        #첫번째 모든 횟수를 구하고
        report_dict = {id:0 for id in id_list}
        for re in report:
            reporter, reported = re.split(" ")
            if target == reporter:
                report_dict[reported]+=1
        #report횟수가 1회이상이면 report_list에 해당 id 추가
        report_list = []
        for reported, number in report_dict.items():
            if number>0:
                report_list.append(reported)
        
        #최종 신고된 리스트에 해당 아이디값 1씩 추가
        for reported in report_list:
            final_reported_dict[reported]+=1
        
    
    for reported, reported_number in final_reported_dict.items():
        print(reporter, reported)
        if reported_number >=k:
            final_banned_list[reported]+=1
    
    for target in id_list:
        answer.append(0)
        
        for re in report:
            reporter, reported = re.split(" ")
            if target == reporter:
                if final_banned_list[reported]>0:
                    answer[-1]+=1
        
    return answer