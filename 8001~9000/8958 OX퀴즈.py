t = int(input())
arr = [None] * t

for i in range(t):
    arr[i] = input()

for j in range(t):
    res = 0
    cnt = 0
    for k in range(len(arr[j])):
        if arr[j][k] == 'O':
            cnt += 1
            res += cnt
        else:
            cnt = 0
    print(res)