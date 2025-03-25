# https://neetcode.io/problems/duplicate-integer
'''
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.
'''

from typing import List


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numSet = set()
        for i in nums:
            if i in numSet:
                return True
            else:
                numSet.add(i)
        return False

