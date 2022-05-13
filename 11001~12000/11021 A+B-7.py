t = int(input())
arr = []

for i in range(t):
    a,b = map(int,input().split())
    arr.append([a,b])

for i in range(t):
    print("Case #{}: {}".format(i+1,sum(arr[i])))