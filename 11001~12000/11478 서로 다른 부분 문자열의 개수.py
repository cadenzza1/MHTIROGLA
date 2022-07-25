import sys
input = sys.stdin.readline

s = input()
res_list = []

for i in range(len(s)): # parsing 시작 위치 
    for j in range(i+1,len(s)):
        temp = s[i:j]
        res_list.append(temp)

res_list = set(res_list)
print(len(res_list))
