from typing import List


class Solution:
    """This is to find the maximum rectangular area can be formed by the array heights"""

    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []  # pair (index, height)

        for i, h in enumerate(heights):
            start_index = i

            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                area = height * (i - index)
                max_area = max(max_area, area)
                start_index = index

            stack.append((start_index, h))

        for i, h in stack:
            area = h * (len(heights) - i)
            max_area = max(max_area, area)

        return max_area


s = Solution()
print(s.largestRectangleArea([2, 1, 5, 6, 2, 3]))  # output 10
print(s.largestRectangleArea([2, 4]))  # output 10
