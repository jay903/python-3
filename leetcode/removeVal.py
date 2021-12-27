l=[0,1,2,2,3,0,4,2]


def removeElement( nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    k=len(nums)
    for i in range(k):
        if nums[i] == val:
            nums[i]="_"

    for j in range(k-2):
        if nums[j]=="_":
            if nums[j+1]=="_":
                nums[j],nums[j+2]=nums[j+2],nums[j]
            else:
                nums[j],nums[j+1]=nums[j+1],nums[j]
    return nums

print(removeElement(l , 2))