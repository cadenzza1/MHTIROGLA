arr = []
for i in range(10):
    tmp = int(input())
    arr.append(tmp%42)

print(len(set(arr)))
