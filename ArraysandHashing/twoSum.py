# https://neetcode.io/problems/two-integer-sum
'''
Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

Return the answer with the smaller index first.
time-complexity : 
space-complexity :
'''

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ind_map = {}
        for index,num in enumerate(nums):
            ind_map[num] = index
        
        for index,num in enumerate(nums):
            numToFind = target-num
            if numToFind in ind_map and index != ind_map[numToFind]:
                return [index,ind_map[numToFind]]
    
        return[0,0]
        