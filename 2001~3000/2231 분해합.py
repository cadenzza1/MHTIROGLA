n = int(input()) # 216
# arr = list(map(int,input()))

for i in range(1,n+1):
    # 125
    sum_small = sum(list(map(int,str(i))))
    res = i + sum_small
    if res ==  n:
        print(i)
        break
else:
    print(0)
