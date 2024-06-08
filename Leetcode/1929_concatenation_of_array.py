# 1929

from typing import List


class Solution:
    '''this is to concate array'''

    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0]*2*n

        for i in range(n):
            ans[i] = nums[i]
            ans[i+n] = nums[i]
        return ans
        # return nums + nums


s = Solution()
print(s.getConcatenation([1, 2, 1]))  # [1,2,1,1,2,1]

# Input: nums = [1,2,1]
# Output: [1,2,1,1,2,1]
# Explanation: The array ans is formed as follows:
# - ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]
# - ans = [1,2,1,1,2,1]
