def isPrime(num):
    end = int(num**(1/2))
    for i in range(2,end+1):
        if(num%i == 0):
            return False
    return True

def solution(n):
    answer = 0
    for num in range(2,n+1):
        if isPrime(num):
            answer += 1
            
    return answer