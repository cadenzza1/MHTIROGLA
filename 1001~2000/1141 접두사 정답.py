n = int(input())
words = [input() for _ in range(n)]

words.sort(key=len)
res = 0

for i in range(n):
    flag = False
    for j in range(i+1,n):
        if words[i] == words[j][:len(words[i])]:
            flag = True

    if flag != True:
        res +=1

# print(res)