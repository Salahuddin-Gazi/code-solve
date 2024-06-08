# 20

from typing import List


class Solution:
    '''This is to find the parenthesis is closed properly or not'''

    def isValid(self, s: str) -> bool:
        n = len(s)
        if n == 0:
            return False

        matching_parenthesis = {'}': '{', ')': '(', ']': '['}
        stack = []

        for _ in s:
            if _ in matching_parenthesis.values():
                stack.append(_)
            elif _ in matching_parenthesis:
                if not stack or stack.pop() != matching_parenthesis[_]:
                    return False
            else:
                continue

        return not stack


s = Solution()
print(s.isValid('()[]{}'))  # true
print(s.isValid('(}'))  # false


# Example 2:

# Input: s = "()[]{}"
# Output: true
