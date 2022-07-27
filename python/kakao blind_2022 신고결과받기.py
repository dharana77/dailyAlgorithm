def solution(id_list, report, k):
    answer = []
    reported_dict = {id:[] for id in id_list}
    reported_final_result = {id:0 for id in id_list}
    banned_list = {id:0 for id in id_list}
    # report.sort()
    
    for report_info in report:
        #신고자, 신고당한 사람
        reporter, reported = report_info.split(" ")
        reported_dict[reporter].append(reported)
    
    #각 추가한 결과를 set으로 중복제거후 다시 list로 변환해 넣어줌
    for reporter, reported  in reported_dict.items():
        reported_dict[reporter] = list(set(reported))
        # print(reported_dict[reporter])
    
    #신고자별 중복제거 신고ID dict값 얻어오기 완료후
    #ID별 최종 신고당한 횟수로 정지여부 확인
    
    for reporter, reporteds in reported_dict.items():
        for reported in reporteds:
            reported_final_result[reported]+=1
    
    for id in id_list:
        if reported_final_result[id]>=k:
            banned_list[id]=1
    
    for id in id_list:
        answer.append(0)
        reporteds = reported_dict[id]
        # print(reporter, reporteds)
        for reported in reporteds:
            if banned_list[reported]==1:
                answer[-1]+=1
    return answer