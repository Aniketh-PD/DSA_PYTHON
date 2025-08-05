'''
You are given a string s consisting of the following 
characters: '(', ')', '{', '}', '[' and ']'.
The input string s is valid if and only if:
Every open bracket is closed by the same type of close bracket.
Open brackets are closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
Return true if s is a valid string, and false otherwise.
TC : O(n)
SC : O(n)
'''
def isValid(self, s: str) -> bool:
    hm = {'}' : '{',']':'[',')':'('}
    stack = []
    for char in s :
        if char in hm:
            if stack and stack[-1] == hm.get(char):
                stack.pop()
            else:
                return False
        else:
            stack.append(char)
    if stack :
        return False
    else:
        return True