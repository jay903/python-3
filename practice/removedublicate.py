nums=[1,1,2]
def removeDuplicates( nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    k=0
    for i in nums:

        if k == 0 or i != nums[k - 1]:
            nums[k] = i

            k += 1
    return k

print(removeDuplicates(nums))