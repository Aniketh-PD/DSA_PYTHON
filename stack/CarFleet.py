from typing import List

'''
There are n cars traveling to the same destination on a one-lane highway.

You are given two arrays of integers position and speed, both of length n.

position[i] is the position of the ith car (in miles)
speed[i] is the speed of the ith car (in miles per hour)
The destination is at position target miles.

A car can not pass another car ahead of it. It can only catch up to another car and then drive at the same speed as the car ahead of it.

A car fleet is a non-empty set of cars driving at the same position and same speed. A single car is also considered a car fleet.

If a car catches up to a car fleet the moment the fleet reaches the destination, then the car is considered to be part of the fleet.

Return the number of different car fleets that will arrive at the destination.

Input: target = 10, position = [4,1,0,7], speed = [2,2,1,1]
Output: 3
REVISIT THIS 
'''
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack=[]
        twoDList = [[p,s] for p,s in zip(position,speed)]
        sortedTwoDList = sorted(twoDList,key=lambda x:x[0] , reverse = True)
        print(sortedTwoDList)

        for p,s in sortedTwoDList:
            stack.append((target-p)/s)
            if(len(stack) >= 2 and stack[-1]<=stack[-2]):
                stack.pop()

        return len(stack)

car = Solution()
position = [4,1,0,7]
speed= [2,2,1,1]
car.carFleet(10,position,speed)