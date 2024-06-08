# 155

from typing import List


class MinStack:
    '''This is to find the stack operation in O(1)'''

    def __init__(self):
        self.stack = []
        self.min_value_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.min_value_stack[-1]
                  if self.min_value_stack else val)
        self.min_value_stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_value_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_value_stack[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.getMin())  # return -3
minStack.pop()
print(minStack.top())   # return 0
print(minStack.getMin())  # return -2


# Example 1:

# Input
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]

# Output
# [null,null,null,null,-3,null,0,-2]

# Explanation
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin(); // return -3
# minStack.pop();
# minStack.top();    // return 0
# minStack.getMin(); // return -2
