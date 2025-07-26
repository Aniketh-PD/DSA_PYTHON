from typing import List
'''
Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

Please implement encode and decode
time complexity:0(m+n) -> m length of each word , n length of list
space complexity:0(1)

'''
class Solution:

    def encode(self, strs: List[str]) -> str:
        '''
        ["neet","code","love","you"]
        '4#neet4#code'
        '''
        resStr=""
        for word in strs:
            resStr+= str(len(word)) + '#' + word
        return resStr

    def decode(self, s: str) -> List[str]:
        res=[]
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j+=1
            length = int(s[i:j])
            word = s[j+1:j+1+length]
            res.append(word)
            i = j+1+length
        return res
