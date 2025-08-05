from typing import List
'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, 
and the indices i, j and k are all distinct.
The output should not contain any duplicate triplets.
You may return the output and the triplets in any order
TC - O(n)
SC - O(1)
'''

def threeSum(self, nums: List[int]) -> List[List[int]]:
    '''
        [-1,0,1,2,-1,-4]
        sort the list
        [-4,-1,-1,-1,0,1,2,2]
        i=1,j=5,k=4
                
        [-4,2,2][-1,-1,2][-1,0,1]
    '''
    ans = []
    nums.sort()
    for index,num in enumerate(nums):
        if(index > 0 and nums[index] == nums[index -1]):
            continue
        j=index+1
        k=len(nums)-1
        
        while(j<k):
            threeSum = num + nums[j] + nums[k]
            if(threeSum > 0):
                k = k-1
            elif(threeSum < 0):
                j = j+1
            else:
                ans.append([num,nums[j],nums[k]])
                while(j+1 < len(nums) and nums[j]==nums[j+1]):
                    j = j+1
                k-=1
                j+=1
    return ans
