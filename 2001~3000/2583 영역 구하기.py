import sys 
sys.setrecursionlimit(10**7) # 최대 재귀 깊이 10,000,000으로 제한

m,n,k = map(int,input().split())

graph = [[0] * n for _ in range(m)]
visited = [[False] * n for _ in range(m)]

for _ in range(k):
    x1,y1,x2,y2 = map(int,input().split())
    for i in range(y1,y2): # 2~4
        for j in range(x1,x2): # 0~4
            graph[i][j] = 1


# 상하좌우 이동용
dx = [-1,1,0,0]
dy = [0,0,-1,1]
cnt = 0
result = []

def DFS(x,y):
    global cnt
    visited[x][y] = True
    cnt += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0<=nx<m) and (0<=ny<n):
            if visited[nx][ny] == False:
                if graph[nx][ny] == 0:
                    DFS(nx,ny)
    return cnt

for i in range(m):
    for j in range(n):
        if visited[i][j] == False and graph[i][j] == 0:
            result.append(DFS(i,j))
            cnt = 0

result.sort()
print(len(result))
for i in result:
    print(i,end = ' ')
