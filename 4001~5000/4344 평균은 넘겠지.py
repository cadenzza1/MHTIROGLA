c = int(input())

score = [0] * c
pyunggyun = [0] * c

for i in range(c):
    score[i] = list(map(int,input().split()))

for j in range(c):
    sum = 0
    for k in range(1,len(score[j])):
        sum += score[j][k]
        if k == len(score[j]-1):
            pyunggyun[j] = sum / score[j][0]
            
