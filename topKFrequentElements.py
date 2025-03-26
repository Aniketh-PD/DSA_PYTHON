from typing import List
'''
Given an integer array nums and an integer k, return the k most frequent elements within the array.

The test cases are generated such that the answer is always unique.

You may return the output in any order.

time-complexity : 
space-complexity :
'''
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = {}
        kList=[[] for i in range(0,len(nums)+1)]
        ans=[]

        for num in nums:
            freqMap[num] = 1 + freqMap.get(num,0)

        for key,value in freqMap.items():
            ind = freqMap.get(key)
            kList[ind].append(key)
        
        for i in range(len(kList)-1,-1,-1):
            ele = kList[i]
            if len(ele) > 0:
                for j in ele:
                    ans.append(j)
                    if len(ans) == k:
                        return ans
        return ans
        
        