from itertools import permutations

N = int(input())
data = range(1,10)
nums = list(permutations(data,3))

for _ in range(N):
    query, s, b = map(int,input().split())
    query = list(str(query))
    remove_cnt = 0

    for i in range(len(nums)):
        strike_count = ball_count = 0
        i -= remove_cnt
        for j in range(3):
            query[j] = int(query[j])
            if query[j] == nums[i][j]:
                strike_count += 1
            elif query[j] in nums[i]:
                ball_count += 1
            # if query[j] in nums[i]:
            #     if j == nums[i].index(query[j]):
            #         strike_count += 1
            #     else:
            #         ball_count += 1

        if (strike_count != s) or (ball_count != b):
            nums.remove(nums[i])
            remove_cnt += 1
            
    
print(len(nums))

# import sys
# from itertools import permutations

# n = int(input())
# num = list(permutations([1,2,3,4,5,6,7,8,9], 3)) #미리 넣어놓는다.

# for _ in range(n):
#     test, s, b = map(int, input().split())
#     test = list(str(test))
#     remove_cnt = 0

#     for i in range(len(num)):
#         s_cnt = b_cnt = 0
#         i -= remove_cnt

#         for j in range(3):
#             test[j] = int(test[j])
#             if test[j] in num[i]:
#                 if j == num[i].index(test[j]):
#                     s_cnt += 1
#                 else:
#                     b_cnt += 1
    
#         if s_cnt != s or b_cnt != b:
#             num.remove(num[i])
#             remove_cnt += 1

# print(len(num))