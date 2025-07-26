from typing import List
'''
You are given an integer n. Return all well-formed parentheses strings that you 
can generate with n pairs of parentheses.
Example 1:

Input: n = 1

Output: ["()"]
Example 2:

Input: n = 3

Output: ["((()))","(()())","(())()","()(())","()()()"]
'''

# my version of solution 
class Solution:
    res =[]
    def generateRecursively(self,op:int,cb:int,bracketStr:str,n:int):
        if(len(bracketStr) == (n*2)):
            self.res.append(bracketStr)
            return
        if(op<n):
            bracketStr+="("
            self.generateRecursively(op+1,cb,bracketStr,n)
            bracketStr = bracketStr[:-1]
        if(cb<op):
            bracketStr+=")"
            self.generateRecursively(op,cb+1,bracketStr,n)
            bracketStr = bracketStr[:-1]


    def generateParenthesis(self, n: int) -> List[str]:
        self.res = []
        self.generateRecursively(0,0,"",n)
        return self.res
    
# easier solution using stack
class Solution:        
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        stack=[]
        def backTrack(openN,closeN):
            if(openN == closeN and closeN == n):
                res.append("".join(stack))
                return
            if(openN<n):
                stack.append("(")
                backTrack(openN + 1,closeN)
                stack.pop()
            if(closeN<openN):
                stack.append(")")
                backTrack(openN, closeN + 1)
                stack.pop()
        backTrack(0,0)
        return res
