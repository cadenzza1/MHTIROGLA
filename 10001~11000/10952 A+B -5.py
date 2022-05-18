arr = []
while(1):
    a,b = map(int,input().split())
    if (a,b) == (0,0):
        break
    else:
        arr.append([a,b])

for i in range(len(arr)):
    print(sum(arr[i]))
