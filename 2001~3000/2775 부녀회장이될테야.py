t = int(input())

for i in range(t):
    floor = int(input()) # 층
    num = int(input()) # 호실
    people = [x for x in range(1,num+1)]

    for x in range(1,floor+1):
        for y in range(1, num):
            people[y] += people[y-1]
    print(people[-1])
    