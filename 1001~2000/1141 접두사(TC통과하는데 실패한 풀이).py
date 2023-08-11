n = int(input())
words = []
for _ in range(n):
    words.append(input())

promising = []
for _ in range(n):
    promising.append(list())

for i in range(n): # 단어의 개수만큼 반복 -> 단어 하나씩 찝어서 알맞은 집합에 넣기 위함
    for j in range(n): # 부분집합의 개수만큼 반복 -> 찝은 단어를 어떤 부분집합에 넣을 지 결정하기 위한 반복
        if len(promising[j]) == 0:
            promising[j].append(words[i])
            break
        for k in range(len(promising[j])): # 선택된 부분집합의 원소의 개수만큼 반복 -> 선택된 부분집합의 원소의 개수와 찝은 단어를 비교
            if len(words[i]) <= len(promising[j][k]):
                if words[i] == promising[j][k][:len(words[i])]:
                    break
            else:
                if promising[j][k] == words[i][:len(promising[j][k])]:
                    break
        else:
            promising[j].append(words[i])

maxi = 0
for i in range(len(promising)):
    if maxi < len(promising[i]):
        maxi = len(promising[i])

print(maxi)