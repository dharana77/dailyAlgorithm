#21:53 ~10:03 효율성 fail
def solution(board, skill):
    answer = 0
    temp = [[0] * (len(board[0])+1) for i in range(len(board[0]) +1)]
    
    for types, r1, c1, r2, c2, degree in skill:
        if types==1:
            degree=-degree
        # print(types, r1,c1, r2,c2, degree)
        temp[r1][c1]+=degree
        temp[r1][c2+1]-=degree
        temp[r2+1][c1]-=degree
        temp[r2+1][c2+1]+=degree
    # print(temp)
    # print(temp)
    for i in range(len(board)):
        for j in range(len(board[0])):
            temp[i][j+1] += temp[i][j]
    # print(temp)
    
    for j in range(len(board[0])):
        for i in range(len(board)):
            temp[i+1][j] += temp[i][j]
    
    # print(temp)
    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j]+=temp[i][j]
            if board[i][j]>=1:
                answer+=1
                
    # print(board)
    return answer