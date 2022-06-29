n,m = map(int,input().split())
nums = list(map(int,input().split()))

l = len(nums)
res = 0

for i in range(0,l-2):
    for j in range(i+1,l-1):
        for k in range(j+1,l):
            if nums[i]+nums[j]+nums[k] > m:
                continue
            else:
                res = max(res,nums[i]+nums[j]+nums[k])

print(res)