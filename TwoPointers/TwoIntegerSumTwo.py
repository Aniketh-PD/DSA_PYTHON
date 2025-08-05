from typing import List
'''
Given an array of integers numbers that is sorted in non-decreasing order.
Return the indices (1-indexed) of two numbers, [index1, index2], such that they add up to a given target number target and index1 < index2.
Note that index1 and index2 cannot be equal, therefore you may not use the same element twice.
There will always be exactly one valid solution.
Your solution must use O(1) additional space.

TC :O(n)
SC :O(1)
'''


def twoSum(self, numbers: List[int], target: int) -> List[int]:
    left = 0
    right = len(numbers)-1
    ans = []
    while left < right:
        currSum = numbers[left] + numbers[right]
        if(currSum == target):
            ans.append(left+1)
            ans.append(right+1)
            return ans
        if(currSum > target):
            right -=1
        if(currSum < target):
            left+=1
    return ans