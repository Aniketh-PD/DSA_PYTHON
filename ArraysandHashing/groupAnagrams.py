# https://neetcode.io/problems/anagram-groups
'''
Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

time-complexity : 
space-complexity :
'''

from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_map= defaultdict(list)
        for word in strs:
            char_list = [0] * 26
            for char in word:
                char_list[ord(char) - ord('a')] +=1
            word_map[tuple(char_list)].append(word)

        return word_map.values()
        