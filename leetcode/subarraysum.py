def maxSofar(nums):
    max_so_far, curr_sum = max(nums), 0
    for i in range(len(nums)):
        if curr_sum + nums[i] < 0:
            curr_sum = 0
        else:
            curr_sum, max_so_far = curr_sum + nums[i], max(max_so_far, curr_sum + nums[i])
    return max_so_far

nums=[-2,1,-3,4,-1,2,1,-5,4]
print(maxSofar(nums))