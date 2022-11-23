def is_prime(num):
    m = int(num ** 0.5)
    if num == 1:
        return False
    
    else:
        for i in range(2,m+1):
            if num % i == 0:
                return False
        else:
            return True

m,n = map(int,input().split())
for i in range(m,n+1):
    if is_prime(i) == True:
        print(i)