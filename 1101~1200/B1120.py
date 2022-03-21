x, y = input().split()

if len(x) == len(y):
    cnt = 0
    for i in range(len(x)):
        if x[i] == x[j]:
            continue
        else:
            cnt+=1

    
