# 167
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while r > l:
            if (numbers[l] + numbers[r]) == target:
                return [l+1, r+1]
            elif (numbers[l] + numbers[r]) > target:
                r -= 1
            elif (numbers[l] + numbers[r]) < target:
                l += 1
        return []


s = Solution()
print(s.twoSum([2, 7, 11, 15], 9))
