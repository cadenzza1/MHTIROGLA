word = input()
ans = [0 for _ in range(10)]

for i in word:
    i = int(i)
    if i == 6 or i == 9:
        if ans[6] <= ans[9]:
            ans[6] += 1
        else:
            ans[9] += 1
    else:
        ans[i] += 1

print(max(ans))