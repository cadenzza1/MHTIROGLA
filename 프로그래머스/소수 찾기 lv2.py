# 1 <= len(numbers) <= 7
# 0 <= numbers <= 9
# 10 * 9 * 8 * 7 * 6 * 5 * 4 -> 600,000 : 10개의 숫자 카드로 7자리의 수를 만드는 경우의 수
# 에라토스테네스의 채를 사용하면 O(n루트n)이므로 O(600,000루트(600000))이므로 시간복잡도 ok

from itertools import permutations

def isPrime(num):
    
    if num < 2:
        return False
    
    end = int(num ** (1/2))
    for i in range(2,end+1):
        if num % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    li = [] # 순열 돌리고 그걸 붙이고 int화까지 한 걸 넣는 배열
    
    for i in range(1, len(numbers)+1):
        # 1. 순열 돌린거 붙이기
        tmp = []
        for i in permutations(numbers,i):
            tmp.append(''.join(i))
        # 2. int화 해서 li배열에 넣기
        for num in tmp:
            li.append(int(num))
    li = set(li)

    for num in li:
        if isPrime(num):
            answer += 1
    
    return answer