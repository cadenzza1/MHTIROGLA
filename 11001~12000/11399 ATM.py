import sys
input = sys.stdin.readline

n = int(input())
p_time = list(map(int,input().split()))

sum = 0
temp = 0
p_time.sort()

for i in p_time:
    temp += i
    sum += temp

print(sum)