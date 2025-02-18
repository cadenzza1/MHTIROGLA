# 이것저것 손으로 적어보니 결국 고르게 큰 수들로 이루어진 집합이 곱셈의 결과도 가장 크다
# 고르게 큰 수들로 이루어진 집합을 끄집어내는 방법을 생각해내자
# -> s가 n으로 나누어 떨어진다면 해당 몫으로만 answer를 구성하는 것이 가장 고른 수들의 분포이므로 최고의 집합이다.
# -> 그러나 나누어 떨어지지 않는다면, 해당 나머지만큼의 answer 배열의 값들을 +1씩 해준 것이 최고의 집합이다.

def solution(n, s):
    answer = []
    
    if(n>s):
        return [-1]
    else:
        for i in range(n):
            answer.append(s//n)
        
    for i in range(s%n):
        answer[i] += 1
        
    answer.sort()
    
    return answer