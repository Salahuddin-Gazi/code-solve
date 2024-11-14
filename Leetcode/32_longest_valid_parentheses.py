# 32. Longest Valid Parentheses [https://leetcode.com/problems/longest-valid-parentheses/description/]


# class Solution:
#     """This is to find the longest valid parenthesis which related to 20_valid_parenthesis"""

#     def longestValidParentheses(self, s: str) -> int:
#         stack = [-1]
#         max_length = 0

#         for i, p in enumerate(s):
#             if p == ")":
#                 stack.pop()
#                 if not stack:
#                     stack.append(i)
#                 else:
#                     length = i - stack[-1]
#                     max_length = max(max_length, length)
#             else:
#                 stack.append(i)

#         return max_length


# gg = Solution()
# print(gg.longestValidParentheses("(()"))  # 2
# print(gg.longestValidParentheses(")()())"))  # 4
# print(gg.longestValidParentheses(""))  # 0


def longestValidParentheses(s) -> int:
     # """This is to find the longest valid parenthesis which related to 20_valid_parenthesis"""

    stack = [-1]
    max_length = 0

    for i, p in enumerate(s):
        if p == ")":
            stack.pop()
            if not stack:
                stack.append(i)
            else:
                length = i - stack[-1]
                max_length = max(max_length, length)
        else:
            stack.append(i)

    return max_length


print(longestValidParentheses("(()"))  # 2
print(longestValidParentheses(")()())"))  # 4
print(longestValidParentheses(""))  # 0