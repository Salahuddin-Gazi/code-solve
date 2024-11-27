from typing import List


class Solution:
    """This is to find the indices of two numbers whose sum equal to target"""

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # num_hash = {}

        # for i in range(len(nums)):
        #     remain = target - nums[i]
        #     if remain in nums:
        #         if num_hash.get(nums[i]) is not None:
        #             return [num_hash[nums[i]], i]
        #         else:
        #             num_hash[remain] = i
        #     else:
        #         num_hash[nums[i]] = i
        num_hash = {}
        for i, v in enumerate(nums):
            diff = target - v
            if v in num_hash:
                return [num_hash[v], i]
            else:
                num_hash[diff] = i

        return []


s = Solution()

print(s.twoSum(nums=[2, 7, 11, 15], target=9))  # output [0, 1]
print(s.twoSum(nums=[3, 2, 4], target=6))  # output [1, 2]
print(s.twoSum(nums=[3, 3], target=6))  # output [0, 1]
