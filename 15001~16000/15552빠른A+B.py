t = int(sys.stdin.readline())

arr = []

for i in range(t):
    a,b = map(int,sys.stdin.readline().split())
    arr.append([a,b])

for j in range(t):
    print(sum(arr[j]))