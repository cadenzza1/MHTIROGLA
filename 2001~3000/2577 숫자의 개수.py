a = int(input())
b = int(input())
c = int(input())

res = a*b*c
res = str(res)
arr = [0] * 10

for i in range(len(res)):
    tmp = res[i]
    arr[int(tmp)] += 1

for j in range(10):
    print(arr[j])