m,n,k = map(int,input().split())

graph = [[0] * n for _ in range(m)]
visited = [[False] * n for _ in range(m)]

for i in range(k):
    x1,y1,x2,y2 = map(int,input().split())
    for j in range(x1,x2):
        for l in range(y1,y2):
            graph[l][j] = 1


# 상하좌우 이동용
dx = [-1,1,0,0]
dy = [0,0,-1,1]

result = []

def DFS(x,y,cnt):
    visited[x][y] = True
    cnt += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0<=nx<n) and (0<=ny<m):
            if visited[ny][nx] == False:
                if graph[ny][nx] == 0:
                    DFS(ny,nx,cnt)

for i in range(m):
    for j in range(n):
        cnt = 0
        if visited[i][j] == False:
            DFS(i,j,cnt)
            result.append(cnt)

result.sort()
print(result)
print("HI")
