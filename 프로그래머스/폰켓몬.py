def solution(nums):
    answer = 0
    
    dic = {}
    for key in nums:
        dic[key] = 1
        
    if len(dic) < len(nums) / 2:
        answer = len(dic)
    else:
        answer = len(nums) / 2
    
    return answer