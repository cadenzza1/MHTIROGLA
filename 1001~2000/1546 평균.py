n = int(input())
score = list(map(int,input().split()))

maxx = max(score)
res = 0

for i in range(len(score)):
    score[i] = (score[i] / maxx) * 100

res = sum(score) / n
print(res)