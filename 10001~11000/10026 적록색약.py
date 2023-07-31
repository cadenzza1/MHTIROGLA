import sys
sys.setrecursionlimit(10**7)

n = int(input())
graph = [list(input()) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

# 정상 시야, 적록색약 시야 그룹 개수
goodEye, ngEye = 0,0

#상하좌우 탐색용
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def DFS(x,y):
    # 현재 노드 방문 처리
    visited[x][y] = True

    # 상하좌우 탐색 시작
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 상하좌우로 이동한 노드가 그래프의 내부에 있다면
        if (0<= nx < n) and (0<= ny < n): 
            # 이동할 노드가 현재 노드의 색과 같다면
            if graph[nx][ny] == graph[x][y]:
                if visited[nx][ny] == False:
                    DFS(nx,ny)

# 정상 시야 탐색 시작
for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            DFS(i,j)
            goodEye += 1

# 방문 여부 초기화
visited = [[False] * n for _ in range(n)]

# 붉은색을 초록색으로 바꾸기
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'R':
             graph[i][j] = 'G'

# 색약 시야 탐색 시작
for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            DFS(i,j)
            ngEye += 1        

print(goodEye,ngEye)
