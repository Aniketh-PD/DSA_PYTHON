from typing import List
'''
Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.
A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element.
The elements do not have to be consecutive in the original array.
You must write an algorithm that runs in O(n) time.
'''

def longestConsequence(nums:List[int]) -> int :
    numSet = set()
    if(len(nums)== 0):
        return 0
    result = 1
    for num in nums:
        numSet.add(num)
    
    for num in nums:
        prevNum = num - 1
        if prevNum in numSet:
            continue
        nextNum = num + 1
        currRes = 1
        while nextNum in numSet:
            currRes+=1
            nextNum+=1
        result = max(result,currRes)
    return result

numList = []

print(longestConsequence(numList))
        