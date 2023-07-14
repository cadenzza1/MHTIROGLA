def solution(a, b, n):
    answer = 0
    
    while(n>=a):
        trade = (n // a) * b
        answer += trade
        n = (n % a) + trade
        
    return answer

# hello