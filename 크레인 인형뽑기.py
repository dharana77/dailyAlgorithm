def solution(board, moves):
    answer = 0
    q = []
    for move in moves:
        target = -1
        height = len(board)
        width = len(board[0])
        
        for i in range(height):
            if board[i][move-1] !=0:
                target = board[i][move-1]
                board[i][move-1]=0
                break
                
        # print(move, target, q)
        
        if target!=-1:
            q.append(target)
        else:
            if len(q)>0 and q[-1]==target:
                q.pop()
                answer+=2
        while len(q)>=2 and q[-1]==q[-2]:
            q.pop()
            q.pop()
            answer+=2
            
    return answer