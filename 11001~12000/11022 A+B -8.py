t = int(input())

arr = []
for i in range(t):
    a,b = map(int,input().split())
    arr.append([a,b])

for j in range(t):
    print("Case #{}: {} + {} = {}".format(j+1,arr[j][0],arr[j][1],sum(arr[j])))