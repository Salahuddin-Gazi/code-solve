import operator
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.truediv,
        }
        stack = []

        for c in tokens:
            if c in operands:
                a = stack.pop()
                b = stack.pop()
                stack.append(int(operands[c](b, a)))
            else:
                stack.append(int(c))

        return stack.pop()


s = Solution()
print(s.evalRPN(["2", "1", "+", "3", "*"]))  # output 9
print(s.evalRPN(["4", "13", "5", "/", "+"]))  # output 9
print(
    s.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"])
)  # output 22
