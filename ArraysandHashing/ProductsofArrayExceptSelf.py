from typing import List
'''
Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

Each product is guaranteed to fit in a 32-bit integer.

Follow-up: Could you solve it in 
O(n)
O(n) time without using the division operation?
TC:O(n)
SC:O(1)
'''
'''
    [1,2,4,6]
    [48,24,12,8]

    postfix = 24
    [1,24,12,8]
'''
def productExceptSelf(self, nums: List[int]) -> List[int]:
    res = [1] * len(nums)

    prefix = 1
    for i in range(len(nums)):
        res[i] = prefix
        prefix = prefix * nums[i]
    
    postfix = 1
    for i in range(len(nums)-1,-1,-1):
        res[i] = postfix * res[i]
        postfix = postfix * nums[i] 
    return res