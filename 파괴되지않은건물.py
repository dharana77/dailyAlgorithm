#21:53 ~10:03 효율성 fail
def solution(board, skill):
    answer = 0
    for sk in skill:
        types = sk[0] #1은 공격, 2는 회복
        r1 = sk[1] #r1,c1부터 r2,c2까지 직사각형 범위 건물 내구도에 영향
        c1 = sk[2]
        r2 = sk[3]
        c2 = sk[4]
        degree = sk[5] #degree만큼 영향
        if types==1:
            degree=-degree
        for i in range(r1,r2+1):
            for j in range(c1,c2+1):
                board[i][j]+=degree
        # print(board)
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j]>=1:
                answer+=1
        
    return answer