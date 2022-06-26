def solution(places):
    answer = []
    
    for _, place in enumerate(places):
        con = True
        for i, row in enumerate(place):
            for j, value in enumerate(row):
                if place[i][j] == "P":
                    #바로 밑이 P인경우
                    if (i+1)<5 and place[i+1][j] == "P":
                        con = False
                        break
                    #바로 오른쪽이 P인경우
                    if (j+1)<5 and place[i][j+1] == "P":
                        con = False
                        break
                    #오른쪽 대각선 혹은 두칸너머가 P인경우
                    if (i+1)<5 and place[i+1][j]=='O':
                        if (j+1)<5:
                            if place[i+1][j+1] == 'P':
                                con = False
                                break
                        if (i+2)<5:
                            if place[i+2][j] == 'P':
                                con = False
                                break
                        if (j-1)>=0:
                            if place[i+1][j-1] == 'P':
                                con = False
                                break
                        if (i-1)>=0:
                            if place[i-1][j] == "P":
                                con = False
                                break
                    if (j+1)<5 and place[i][j+1]=='O':
                        if (i+1)<5:
                            if place[i+1][j+1] == 'P':
                                con = False
                                break
                        if (j+2)<5:
                            if place[i][j+2] == 'P':
                                con = False
                                break
                        if (i-1)>=0:
                            if place[i-1][j+1] == "P":
                                con = False
                                break
                    if (j-1)>=0 and place[i][j-1] == "O":
                        if (i+1)<5 and (j-1)>=0:
                            if place[i+1][j-1] =="P":
                                con = False
                                break
                
        if con:
            answer.append(1)
        else:
            answer.append(0)
                            
                            
    return answer