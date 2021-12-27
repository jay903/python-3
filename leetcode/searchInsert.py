nums=[1,3,4,5,6,8,17]
target=2
def searchInsert(nums,target):
    for i in range(len(nums) ):
        if nums[i] < target and nums[i + 1] > target:
                        print(i)


    return i
print(searchInsert(nums,target))