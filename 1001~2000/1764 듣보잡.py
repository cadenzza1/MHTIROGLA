import sys
input = sys.stdin.readline

n,m = map(int,input().split())
no_listen = []
no_watch = []

for _ in range(n):
    no_listen.append(input())

for _ in range(m):
    no_watch.append(input())

no_listen = set(no_listen)
no_watch = set(no_watch)
res = no_listen & no_watch
res = list(res)

print(len(res))
res.sort()

for j in res:
    print(j, end = '')
