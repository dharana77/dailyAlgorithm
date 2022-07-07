def solution(files):
    answer = []
    
    lst = []
    
    for i, _ in enumerate(files):
        head, number, tail = '', '', ''
        for idx, file in enumerate(files[i]):
            
            if file.isdigit():
                
                head_idx = idx
                head = files[i][:head_idx]
                temp = files[i][head_idx:]
                # print(head,temp)
                for idf, f in enumerate(temp):
                    if not f.isdigit() or idf>=5:
                        
                        tail = temp[idf:]
                        number = temp[:idf]
                        temp = (head, number, tail)
                        lst.append(temp)
                        
                        break
                if tail=="" and number=="":
                    number = temp
                    lst.append((head, number ,tail))
                break
    
    # print(head,number,tail)
    # print(lst)
    lst = sorted(lst, key= lambda x: (x[0].lower(), int(x[1])))
    # print(lst)
    answer = ["".join(i) for i in lst]
    return answer