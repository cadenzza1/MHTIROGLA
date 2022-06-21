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

# 내가 짰던 코드보다 이게 시간이 덜 걸리는 이유를 모르겠다.
# 이 코드도 sosu_list를 겁나게 순회하는데, 이러면 얘도 시간 겁나 오래 걸리는 거 아닌가???
# 숫자 하나 검사할 때마다 for문으로 sosu_list를 한 번씩 순회하는데 그러면 굉장히 시간이 오래 걸릴 거 같은데
# 그럼에도 불구하고 나의 원래 코드보다 시간이 덜 걸리는 것인가??