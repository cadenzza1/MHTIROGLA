global result
result = 0

def dfs(visited, num, network):
    global result
    result += 1
    visited[num] = True

    for i in network[num]:
        if not visited[i]:
            dfs(visited, i, network)

    

n = int(input())
m = int(input())

network = [[] for i in range(n+1)]
for i in range(m):
    a,b = map(int,input().split())
    network[a].append(b)
    network[b].append(a)

visited = [False] * (n+1)
dfs(visited, 1, network)
print(result-1)
