# 682

from typing import List


class Solution:
    """This is to calculate total sum of an array after doing operations to the array, it's uses LIFO or Stack"""

    def calPoints(self, operations: List[str]) -> int:
        n = len(operations)
        if n == 0:
            return 0

        stack = []
        for i in range(n):
            val = operations[i]
            if (not stack) and (val == 'C' or val == 'D' or val == '+'):
                continue

            match val:
                case 'C':
                    stack.pop()
                case 'D':
                    stack.append(2 * stack[-1])
                case "+":
                    stack.append(stack[-1] + stack[-2])
                case _:
                    stack.append(int(val))
        return sum(stack)


s = Solution()
print(s.calPoints(["5", "-2", "4", "C", "D", "9", "+", "+"]))  # 27
print(s.calPoints(["1", "C", "+"]))  # 27

# Example 2:

# Input: ops = ["5","-2","4","C","D","9","+","+"]
# Output: 27
# Explanation:
# "5" - Add 5 to the record, record is now [5].
# "-2" - Add -2 to the record, record is now [5, -2].
# "4" - Add 4 to the record, record is now [5, -2, 4].
# "C" - Invalidate and remove the previous score, record is now [5, -2].
# "D" - Add 2 * -2 = -4 to the record, record is now [5, -2, -4].
# "9" - Add 9 to the record, record is now [5, -2, -4, 9].
# "+" - Add -4 + 9 = 5 to the record, record is now [5, -2, -4, 9, 5].
# "+" - Add 9 + 5 = 14 to the record, record is now [5, -2, -4, 9, 5, 14].
# The total sum is 5 + -2 + -4 + 9 + 5 + 14 = 27.
