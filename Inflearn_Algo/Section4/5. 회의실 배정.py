from collections import deque

n = int(input())
li = []
for i in range(n):
    li.append(list(map(int,(input().split()))))

li.sort(key=lambda x: x[1])

dq = deque(li)

res = 1
li = []
li.append(dq.popleft())

while(dq):
    if li[-1][1] <= dq[0][0]:
        res += 1
        li.append(dq.popleft())
    else:
        dq.popleft()
    

print(res)