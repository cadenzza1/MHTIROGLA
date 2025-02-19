def solution(survey, choices):
    answer = []
    dic = {
        "R" : 0,
        "T" : 0,
        "C" : 0,
        "F" : 0,
        "J" : 0,
        "M" : 0,
        "A" : 0,
        "N" : 0
    }
    
    for i in range(len(survey)):
        if 1 <= choices[i] <= 3:
            dic[survey[i][0]] += 4-choices[i]    
        elif 4 <= choices[i] <= 7:
            dic[survey[i][1]] += -(4-choices[i])
    
    if dic["R"] >= dic["T"]:
        answer.append("R")
    else:
        answer.append("T")
    if dic["C"] >= dic["F"]:
        answer.append("C")
    else:
        answer.append("F")
    if dic["J"] >= dic["M"]:
        answer.append("J")
    else:
        answer.append("M")
    if dic["A"] >= dic["N"]:
        answer.append("A")
    else:
        answer.append("N")
        
    return ''.join(answer)