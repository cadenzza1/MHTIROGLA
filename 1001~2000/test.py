n = int(input())
num = n
cnt = 0

while 1:
    a = num // 10
    b = num % 10
    c = (a+b) % 10
    num = (b*10) + c

    cnt += 1
    if num==n:
        break

print(cnt)

print("For Everyday Commit")