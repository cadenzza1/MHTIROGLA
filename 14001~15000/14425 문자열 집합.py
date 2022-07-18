import sys
input = sys.stdin.readline

n,m = map(int,input().split())

cnt = 0
s = []

for i in range(n): # 집합 S에 들어있는 문자열들 입력받기
    s.append(input())

s = set(s)
s = list(s)

for i in range(m):
    if input() in s:
        cnt += 1

print(cnt)
    
