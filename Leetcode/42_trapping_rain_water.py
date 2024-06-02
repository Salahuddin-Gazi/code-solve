# 42

from typing import List


class Solution:
    '''This is to calculate the trapping rain water block on given heights'''

    def trap(self, height: List[int]) -> int:
        if len(height) == 0:
            return 0

        l, r = 0, len(height) - 1
        maxLeft, maxRight = height[l], height[r]
        res = 0

        while l < r:
            if maxLeft < maxRight:
                l += 1
                maxLeft = max(maxLeft, height[l])
                res += maxLeft - height[l]
            else:
                r -= 1
                maxRight = max(maxRight, height[r])
                res += maxRight - height[r]

        return res


s = Solution()
print(s.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))  # 6
print(s.trap([4, 2, 0, 3, 2, 5]))  # 9
