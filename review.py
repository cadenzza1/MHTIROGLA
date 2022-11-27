from collections import deque

lis = list(range(3))
li = [1,2,3,4]
dd = deque()
test = deque(list(range(3)))
test2 = deque()
test2.append(list(range(3)))

print(*lis)
print(li)
print(dd)
print(test)
print(test2)
print(*test)
print(*test2)