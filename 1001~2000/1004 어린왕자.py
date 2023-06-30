t = int(input())
for i in range(t): # 테스트케이스 개수만큼 반복
    a,b,c,d = map(int,input().split())
    a1 = (a,b) # 출발점
    a2 = (c,d) # 도착점

    n = int(input()) # 행성계 개수
    cnt = 0
    for i in range(n):
        cx,cy,r = map(int,input().split())
        d1 = ((cx-a) ** 2 + (cy-b) ** 2) ** 0.5 # 출발점과 행성계의 중심 사이의 거리
        d2 = ((cx-c) ** 2 + (cy-d) ** 2) ** 0.5 # 도착점과 행성계의 중심 사이의 거리
        # 출발점이 원 안에 있고 도착점이 원 밖에 있거나, 출발점이 원 밖에 있고 도착점이 원 밖에 있으면 cnt 1만큼 증가
        if ( d1 < r and d2 > r) or ( d1 > r and d2 < r):
            cnt += 1
    print(cnt)