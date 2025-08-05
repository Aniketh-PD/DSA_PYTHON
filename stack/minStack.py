'''
Design a stack class that supports the push, pop, top, and getMin operations.
MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
Each function should run in 
O(1) time.
TC -  O(1) for all methods
'''
class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        

    def push(self, val: int) -> None:
        if(type(val) in (int,float,complex)):
            self.stack.append(val)
            if(len(self.minStack) <= 0):
                self.minStack.append(val)
                return
            if(self.minStack and val <= self.minStack[-1]):
                self.minStack.append(val)

    def pop(self) -> None:
        if(len(self.stack) <= 0):
            return
        
        removedValue = self.stack.pop()
        if(removedValue == self.minStack[-1]):
            self.minStack.pop()

    def top(self) -> int:
        if(len(self.stack) > 0):
            return self.stack[-1]

    def getMin(self) -> int:
        if len(self.minStack) > 0 :
            return self.minStack[-1]
