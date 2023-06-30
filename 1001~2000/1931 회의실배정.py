from collections import deque

n = int(input())
li = []
for i in range(n):
    li.append(list(map(int,input().split())))

li.sort(key=lambda x : (x[1], x[0]))
dq = deque(li)

cnt = 1
rs = []
rs.append(dq.popleft())
for i in range(len(dq)):
    if dq[0][0] >= rs[-1][1]:
        cnt += 1
        rs.append(dq.popleft())
    else:
        dq.popleft()
print(cnt)