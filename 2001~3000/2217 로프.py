import sys
input = sys.stdin.readline
n = int(input())

rope = []
for i in range(n):
    rope.append(int(input()))

rope.sort(reverse=True)

# 로프를 1개 쓸 때부터 n개 쓸 때가지의 들 수 있는 무게를 구해서 그 중 최댓값을 리턴하면 된다.
weight = []
for i in range(n):
    weight.append((i+1)*rope[i])

print(max(weight))
