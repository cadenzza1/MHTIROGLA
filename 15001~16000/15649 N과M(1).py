# 백트래킹의 핵심 -> 가능한 '모든'경우 실행하여 정답 찾기
# '가능한 모든 경우'를 탐색할 때는 '트리 형태'가 가장 좋다!

# 아이디어 : 백트래킹 , 재귀함수

# 시간복잡도 : N! -> 가능 , n이 10보다 작아야 하는데 8이라 가능

# 자료구조 : v[] : 방문 확인용 리스트, rs[] : 결과값 담을 리스트

import sys
input = sys.stdin.readline

n,m = map(int,input().split())
rs = []
v = [False] * (n+1)

def dfs(num):
    if num == m:
        print(' '.join(map(str,rs)))
        return
    for i in range(1,n+1):
        if v[i] == False:
            v[i] = True
            rs.append(i)
            dfs(num+1)
            rs.pop()
            v[i] = False

dfs(0)