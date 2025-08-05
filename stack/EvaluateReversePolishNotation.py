'''
You are given an array of strings tokens that represents a 
valid arithmetic expression in Reverse Polish Notation.
Return the integer that represents the evaluation of the expression.
The operands may be integers or the results of other operations.
The operators include '+', '-', '*', and '/'.
Assume that division between integers always truncates toward zero.
'''

from typing import List


def evalRPN(self, tokens: List[str]) -> int:
    stack=[]
    if(len(tokens) == 1):
        return int(tokens[0])
    for char in tokens:
        if char!= '+' and char!='-' and char!='*' and char!='/':
            stack.append(int(char))
        else:
            match char:
                case '+':
                    res = stack.pop()+stack.pop()
                    stack.append(res)
                case '-':
                    a,b = stack.pop(),stack.pop()
                    res = b - a
                    stack.append(res)
                case '*':
                    res = stack.pop() * stack.pop()
                    stack.append(res)
                case '/':
                    a,b = stack.pop(),stack.pop()
                    stack.append(int(float(b)/a))
    return int(stack[-1])