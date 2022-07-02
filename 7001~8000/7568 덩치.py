n = int(input())
stat = []
rank = []
for i in range(n):
    stat.append(list(map(int,input().split())))

for j in stat:
    rank = 1 # 1등에서 시작해서 점점 랭킹이 낮아지는 늑낌
    for k in stat:
        if j[0] < k[0] and j[1] < k[1]:
            rank += 1
    print(rank, end = ' ')