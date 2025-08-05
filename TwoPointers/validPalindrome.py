'''
Given a string s, return true if it is a palindrome, otherwise return false.

A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

Note: Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9).

TC : O(n)
SC : O(n)
'''
def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1
        while left < right :
            while left < right and not self.isAlphaNum(s[left]):
                left+=1
            while left < right and not self.isAlphaNum(s[right]):
                right-=1
            if(s[left].lower() != s[right].lower()):
                return False
            left+=1
            right-=1
        return True
            
    
def isAlphaNum(self,inp_char):
    return  (ord('A') <= ord(inp_char) <= ord('Z') or 
            ord('a') <= ord(inp_char) <= ord('z') or 
            ord('0') <=ord(inp_char) <=ord('9'))