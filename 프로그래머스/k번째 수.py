def solution(array, commands):
    answer = []
    
    for ijk in commands:
        temp_array = array[ijk[0]-1:ijk[1]]
        temp_array.sort()
        answer.append(temp_array[ijk[2]-1])
    
    return answer