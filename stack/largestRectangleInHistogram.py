from typing import List

'''
You are given an array of integers heights where heights[i] represents the height of a bar. The width of each bar is 1.

Return the area of the largest rectangle that can be formed among the bars.

Input: heights = [7,1,7,2,2,4]

Output: 8

Input: heights = [1,3,7]

Output: 7

'''

def largestRectangleArea(heights: List[int]) -> int:
    maxArea = 0
    stack=[]

    for i,h in enumerate(heights):
        start = i 
        while stack and stack[-1][1] > h:
            index,height = stack.pop()
            maxArea = max(maxArea,(height * (i - index)))
            start = index
        stack.append([start,h])

    for i,h in stack:
        maxArea = max(maxArea,h * (len(heights) - i))
    
    return maxArea

print(largestRectangleArea([7,1,7,2,2,4]))
