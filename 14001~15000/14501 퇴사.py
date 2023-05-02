n = int(input())
t = [0]
p = [0]
dp = [0 for i in range(n+2)]

for _ in range(n):
    tTmp, pTmp = map(int,input().split())
    t.append(tTmp)
    p.append(pTmp)

for i in range(n,-1,-1):
    if t[i] + i > n+1:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], p[i] + dp[i+t[i]])
print(dp[1])


