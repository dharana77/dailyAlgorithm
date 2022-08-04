from itertools import permutations

def print_target(target):
    result = ""
    for idx, tar in enumerate(target):
        result+=str(tar) 
        if idx != len(target)-1:
            result+=" "
    return result


t = int(input())

for i in range(t):
    n = int(input())
    target = [i for i in range(1, n+1)]
    print(n)
    
    first = target
    target = print_target(first)
    print(target)

    #swap last and first
    temp = first[0]
    first[0] = first[-1]
    first[-1] = temp
    
    target = print_target(first)
    print(target)

    current = len(first) - 2
    while current>0:
        temp = first[current]
        first[current] = first[current+1]
        first[current+1] = temp
        target = print_target(first)
        print(target)
        current-=1
