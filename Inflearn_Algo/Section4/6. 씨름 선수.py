n = int(input())
li = []
for i in range(n):
    li.append(list(map(int,input().split())))
li.sort()
print(li)
cnt = 1
for i in range(len(li)-1):
    for j in range(i+1,len(li)):
        if li[i][1] < li[j][1]:
            break
    else:
        cnt += 1

print(cnt)