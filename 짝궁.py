
def solution(X, Y):
    answer = ''
    x_number_count = {key:0 for key in range(0,10)}
    y_number_count = {key:0 for key in range(0,10)}
    # print(x_number_count)

    for i in X:
        x_number_count[int(i)]+=1
    for i in Y:
        y_number_count[int(i)]+=1

    can_be_used = []
    for i in range(0,10):
        key = i
        value = min(x_number_count[i], y_number_count[i])
        for k in range(value):
            can_be_used.append(str(key))
    can_be_used.sort(reverse=True)

    answer = ''.join(can_be_used)
    if answer == '':
        return "-1"
    answer = str(int(answer))
    return answer