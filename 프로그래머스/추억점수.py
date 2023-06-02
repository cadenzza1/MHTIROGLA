def solution(name, yearning, photo):
    answer = []
    dictionary = {}
    for i in range(len(name)):
            dictionary[name[i]] = yearning[i]
    for j in range(len(photo)):
        tmp = 0
        for k in range(len(photo[j])):
            if photo[j][k] in dictionary:
                tmp += dictionary[photo[j][k]]
        answer.append(tmp)
        
        
    return answer