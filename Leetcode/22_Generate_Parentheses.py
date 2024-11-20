from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backTrack(openN, closeN):
            print(stack, openN, closeN)
            if openN == closeN == n:
                res.append("".join(stack))
                return

            if openN < n:
                stack.append("(")
                backTrack(openN + 1, closeN)
                stack.pop()

            if closeN < openN:
                stack.append(")")
                backTrack(openN, closeN + 1)
                stack.pop()

        backTrack(0, 0)
        return res


s = Solution()
print(s.generateParenthesis(3))  # output ["((()))","(()())","(())()","()(())","()()()"]
# print(s.generateParenthesis(1))  # output ["()"]


