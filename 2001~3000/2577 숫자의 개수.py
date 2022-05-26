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

# ------------------------------
# 깔끔한 코드

# a = int(input())
# b = int(input())
# c = int(input())

# result = list(str(a * b * c))
# for i in range(10):
#     print(result.count(str(i)))