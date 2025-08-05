from typing import List
'''
You are given an array of non-negative integers height which represent an elevation map. 
Each value height[i] represents the height of a bar, which has a width of 1.
Return the maximum area of water that can be trapped between the bars.

Input: height = [0,2,0,3,1,0,1,3,2,1]
Output: 9
'''

def trap(self, height: List[int]) -> int:
    length = len(height)
    if(length == 1):
        return 0
    res = 0
    maxLeftHeightList = [] * length
    maxRightHeightList = [] * length
    currLeft = 0
    for i,h in enumerate(height):
        maxLeftHeightList[i] = currLeft
        currLeft = max(currLeft,h)
    
    currRight = 0
    for i in range(length-1,-1,-1):
        maxRightHeightList[i] = currRight
        currRight = max(currRight,maxRightHeightList[i])
    
    for i,h in enumerate(height):
        trappedWater = h -  min(maxLeftHeightList[i],maxRightHeightList[i])
        if(trappedWater > 0) :
            res+=trappedWater
    return res