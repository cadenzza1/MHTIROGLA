import sys
sys.setrecursionlimit(10**7)

n = int(input())

graph = [[] for _ in range(n+1)]
parent = [None for _ in range(n+1)]

def DFS(graph, v, visited):
    for i in graph[v]:
        if not visited[i]:
            visited[i] = v
            DFS(graph,i,visited)

for _ in range(n-1):
    a,b  = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

DFS(graph,1,parent)

for i in range(2,n+1):
    print(parent[i])
