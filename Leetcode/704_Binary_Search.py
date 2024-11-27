import math
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while r >= l:
            m = math.floor((l + r) / 2)

            if nums[m] == target:
                return m

            elif target > nums[m]:
                l = m + 1

            else:
                r = m - 1

        return -1


s = Solution()
print(s.search([-1, 0, 3, 5, 9, 12], 9))  # target -> 9, output 4
print(s.search([-1, 0, 3, 5, 9, 12], 2))  # target -> 2, output -1
print(s.search([5], 5))  # target -> 2, output -1
