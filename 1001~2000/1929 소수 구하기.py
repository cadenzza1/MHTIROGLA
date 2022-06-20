#소수판별법 = 수의 제곱근까지만 나눠보면 된다.
#약수는 대칭으로 이루어져있기 때문에
#(예) 12의 약수는 1 2 3 4 6 12 / 1*12 , 2*6, 3*4 로 대칭
#25의 약수는 1 5 25 / 1*25 , 5*5 로 대칭
#제곱근 보다 같거나 작은 수까지만 나눠보고 나누어 떨어지는게 있냐 없냐 확인하면 된다

def isPrime(num):
    if num == 1:
        return False
    else:
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                return False
        else: return True

m,n = map(int,input().split())

for i in range(m,n+1):
    if isPrime(i) == True:
        print(i)