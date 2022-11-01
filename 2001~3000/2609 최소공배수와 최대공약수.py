import sys
input = sys.stdin.readline

a,b = map(int,input().split())

a_num = []
b_num = []

for i in range(1,a+1):
    if a % i == 0:
        a_num.append(i)

for j in range(1,b+1):
    if b % j == 0:
        b_num.append(j)

set1 = set(a_num)
set2 = set(b_num)

sol1 = max(set1 & set2) # 최대공약수
sol2 = sol1 * (a/sol1) * (b/sol1) # 최소공배수

print(sol1) # 최대공약수 출력
print(int((sol2)))