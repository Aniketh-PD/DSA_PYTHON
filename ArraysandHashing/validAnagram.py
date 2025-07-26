# https://neetcode.io/problems/is-anagram
'''
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
time-complexity : 
space-complexity :
'''

class Solution:
    def getCharFrequencyMap(self,word:str):
        freqMap = {}
        for char in word:
            if char in freqMap:
                freqMap[char] += 1
            else:
                freqMap[char] = 1
        return freqMap
    
    def isAnagram(self, s: str, t: str) -> bool:
        '''create two hashmaps storing the frequency of each
        character occurenece within string
        compare the maps false conds - if value does not match
                                       if value matchses but freq does not            
        '''
        if len(s) != len(t):
            return False
        sMap = self.getCharFrequencyMap(s)
        tMap = self.getCharFrequencyMap(t)
        for key in sMap.keys():
            if key not in tMap.keys():
                return False
            sCharCount = sMap[key]
            tCharCount = tMap[key]
            if sCharCount != tCharCount :
                return False
        return True

        