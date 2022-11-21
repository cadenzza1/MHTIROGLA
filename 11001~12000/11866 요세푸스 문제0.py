from collections import deque
import sys
input = sys.stdin.readline

n,k = map(int,input().split())

people = deque(range(1,n+1))
ans = []

while people:
    people.rotate(-k+1)
    ans.append(people.popleft())

print("<", end = '')
for i in range(len(ans)):
    if i != len(ans)-1:
        print(ans[i], end=', ')
    else:
        print(ans[i], end = '')
print(">")
