from itertools import combinations

l,c = map(int,input().split())
c_arr = sorted(list(input().split()))

mo = ['a','e','i','o','u']

result = []

for i in combinations(c_arr,l):
    mo_cnt = 0
    ja_cnt = 0
    for j in i:
        if j in mo:
            mo_cnt += 1
        else:
            ja_cnt += 1
    i = list(i)
    flag = i == sorted(i)
    if mo_cnt >= 1 and ja_cnt >= 2 and flag:
        print("".join(i))
