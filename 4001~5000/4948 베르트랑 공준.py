def isPrime(n):
    if n == 1: return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0: return False
    else:
        return True

sosu_list = []
all_list = [i for i in range(2,246912)]
for i in all_list:
    if isPrime(i) == True:
        sosu_list.append(i)

while True:
    num = int(input())
    if num == 0: break
    cnt = 0
    
    for i in sosu_list: # 소수 리스트중에서
        if num < i <= 2*num: # 입력한 값의 범위 내에서 값이 있으면
            cnt += 1 # 있을 때마다 카운트 +1
    print(cnt)