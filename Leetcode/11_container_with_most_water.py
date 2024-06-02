# 11
from typing import List


class Solution:
    '''This is to find the maximum water area using length * height formula. Height will be the lowest of the two and lengthr will be the index difference.'''

    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_area = 0

        while l < r:
            area = (r - l) * min(height[l], height[r])
            max_area = max(max_area, area)

            if height[l] > height[r]:
                r -= 1
            else:
                l += 1

        return max_area


s = Solution()
print(s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))  # 49
print(s.maxArea([1, 8, 20, 9, 18, 30, 8, 3, 7]))  # 49
print(s.maxArea([1, 1]))  # 1
