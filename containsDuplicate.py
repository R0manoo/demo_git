def containsDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    checked=[]
    for elem in nums:
        if elem in checked:
            return True
        else:
            checked.append(elem)
    return False
arr=[1,2,3,4]
print(containsDuplicate(arr))
