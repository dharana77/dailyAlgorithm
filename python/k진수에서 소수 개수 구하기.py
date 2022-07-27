from math import sqrt
def solution(n, k):
    answer = 0
    temp = ""
    while n>0:
        res = n%k
        # print(n)
        temp = str(res) + temp
        n = int(n/k)
    
    lst = temp.split("0")
    for i in lst:
        if i!='' and is_prime(int(i)):
            # print(i)
            answer+=1
    return answer

def is_prime(number: int ) -> bool:
    if number == 1:
        return False
    for i in range(2, int(sqrt(number)) + 1):
        if number%i == 0 :
            return False
    return True