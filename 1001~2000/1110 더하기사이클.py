#1 정수로 풀이하는 방법
n = int(input())  # 68
num = n
cnt = 0 # 사이클 수

while True:
    a = num // 10 # 6
    b = num % 10 # 8
    c = (a+b) % 10 # 6 + 8 = 1"4"
    num = (b * 10) + c # 80 + 4 = 84

    cnt = cnt + 1 # 사이클 수 + 1
    if (num==n): # num에서 입력된 n과 같은 숫자가 나오면 멈춤
        break

print(cnt)

#2 문자형으로 풀이하는 방법
"""
n = input()
num = n
cnt = 0

while 1:
    if len(num) == 1:
        num = "0" + num
    plus = str(int(num[0]) + int(num[1]))
    num = num[-1] + plus[-1]
    cnt += 1
    if num == n:
        print(cnt)
        break 
"""

