m = int(input())
n = int(input())

sosu_list = []

for i in range(m,n+1):
    if i == 1:
        pass
    elif i == 2:
        sosu_list.append(i)
    else:
        for j in range(2,i):
            if i % j == 0:
                break
        else:
            sosu_list.append(i)

if len(sosu_list) == 0:
    print(-1)
else:    
    print(sum(sosu_list))
    print(min(sosu_list))