def dfs(x,y):
    global cnt
    cnt += 1
    vill[x][y] = 0 # 방문 표시
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and vill[nx][ny] == 1:
            dfs(nx,ny)

n = int(input())
vill = []
for _ in range(n):
    vill.append(list(map(int,input())))

dx = [0,0,-1,1]
dy = [-1,1,0,0] # 상 하 좌 우

cnt = 0
result = []

for i in range(n):
    for j in range(n):
        if vill[i][j] == 1:
            dfs(i,j)
            result.append(cnt)
            cnt = 0

print(len(result))
result.sort()
for f in result:
    print(f)

