from typing import List
'''
You are given an integer array heights where heights[i] represents the height of the 
ith bar.You may choose any two bars to form a container. Return the maximum amount of 
water a container can store.
height = [1,7,2,5,4,7,3,6]
TC : O(n)
'''
def maxArea(heights: List[int]) -> int:
        length = len(heights)
        l,r = 0,length-1
        area = 0

        while l < r:
            minHeight = min(heights[l],heights[r])
            breadth = r-l
            currArea = minHeight * breadth
            area = max(area,currArea)
            if(heights[l]<heights[r]):
                l+=1
            else:
                r-=1
    
        return area
height = [1,7,2,5,4,7,3,6]
print(maxArea(height))