n = int(input())
num = 0
cnt = 0

while True:
    num += 1
    
    if '666' in str(num):
        cnt += 1
    if cnt == n:
        print(num)
        break

# 숫자를 하나씩 키워가며 숫자 안에 666이 들어있으면 cnt를 증가시킨다.
# 그렇게 cnt를 증가시키다가 cnt가 입력받은 값과 동일해지면 num값이 n번째로 작은 666이 포함된 수라는 뜻이다!