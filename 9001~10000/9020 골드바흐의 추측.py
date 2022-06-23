def isPrime(num):
    if num == 1:
        return False
    else:
        for i in range(2,int(num**0.5)+1):
            if num % i == 0:
                return False
        else: return True

for _ in range(int(input())): # 입력받은 수 만큼의 테스트케이스를 입력받는당
    num = int(input())

    a,b = num//2, num//2
    while a > 0:
        if isPrime(a) and isPrime(b):
            print(a,b)
            break
            
        else:
            a -= 1
            b += 1

