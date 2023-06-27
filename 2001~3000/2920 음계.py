li = list(map(int,input().split()))

if li[0] == 1:
    for i in range(1,len(li)):
        if (li[i]-1) == li[i-1]:
            continue
        else:
            print("mixed")
            break
    else:
        print("ascending")
elif li[0] == 8:
    for i in range(1,len(li)):
        if (li[i]+1) == li[i-1]:
            continue
        else:
            print("mixed")
            break
    else:
        print("descending")
else:
    print("mixed")

