from collections import defaultdict
from typing import List

"""
Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.
An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
Example 1:
Input: strs = ["act","pots","tops","cat","stop","hat"]

Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

Example 2:
Input: strs = ["x"]

Example 3:
Output: [["x"]]
Input: strs = [""]

Output: [[""]]


"""

def groupAnagrams(strs:List[str]):
    res= defaultdict(list)
    # print(res,ord('a'))

    for word in strs :
        # way to intialize list of 0's length 26 
        count = [0] * 26
        
        for char in word:
            # ord('a') return ascii value 97
            count[ord(char) - ord('a')] +=1
    
        res[tuple(count)].append(word)
        # print(res)
    return res.values()

print(groupAnagrams(["act","pots","tops","cat","stop","hat"]))
    

    