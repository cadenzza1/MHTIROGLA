def hansu(num):
    cnt = 0
    for i in range(1,int(num)+1):
        if i < 100:
            cnt += 1
        elif int((str(i))[0])-int((str(i))[1]) == int((str(i))[1]) - int((str(i))[2]):
            cnt += 1
    return cnt

num = input()
print(hansu(num))
    