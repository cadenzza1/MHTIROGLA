n = int(input())
student_stat = []

for _ in range(n):
    student_stat.append(list(map(int,input().split())))

for i in student_stat:
    rank = 1
    for j in student_stat:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end = ' ')
