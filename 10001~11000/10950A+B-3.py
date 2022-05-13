t = int(input())

li = []

 

for i in range(t):

    a,b = map(int,input().split())

    li.append([a,b])

    

for j in range(t):

    print(sum(li[j]))