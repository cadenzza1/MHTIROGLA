sugar = int(input())

bag = 0
while sugar >= 0 :
    if sugar % 5 == 0 :  # 5의 배수이면
        bag += (sugar // 5)  # 5로 나눈 몫을 구해야 정수가 됨
        print(bag)
        break
    sugar -= 3  # 5의 배수가 아니면 설탕을 3kg씩 빼서!
    bag += 1  # 5의 배수가 될 때까지 설탕-3, 봉지+1
else : # 설탕의 무게가 음수가 돼버리면! (3과 5의 조합으로 수가 표현이 안되면)
    print(-1)

