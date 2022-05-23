def is_hansu(n : int):
    hansu_cnt = 0
    for i in range(1,n+1):
        num_list = list(map(int,str(i)))
        if i < 100:
            hansu_cnt += 1
        elif num_list[0] - num_list[1] == num_list[1] - num_list[2]:
            hansu_cnt += 1
    return hansu_cnt

n = int(input())
print(is_hansu(n))

