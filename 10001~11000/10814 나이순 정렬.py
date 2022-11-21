n = int(input())

info = []

for i in range(n):
    info.append(input().split())
    info[i][0] = int(info[i][0])

info = sorted(info, key = lambda x : x[0])

for x,y in info:
    print(x,y)