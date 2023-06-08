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
        if v[i] == False and rs:
            if i > rs[-1]:
                v[i] = True
                rs.append(i)
                dfs(num+1)
                v[i] = False
                rs.pop()
        if v[i] == False and not rs:
            v[i] = True
            rs.append(i)
            dfs(num+1)
            rs.pop()
            v[i]=False

dfs(0)


