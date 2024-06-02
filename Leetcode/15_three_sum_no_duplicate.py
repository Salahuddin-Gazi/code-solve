# 15

from typing import List


class Solution:
    '''This it to find the three sum'''

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        threeSum = []

        i = 0
        while i < len(nums):
            if i > 0 and nums[i - 1] == nums[i]:
                i += 1
                continue

            l = i+1
            r = len(nums) - 1

            # implementing two sum here
            while l < r:
                currentSum = nums[i] + nums[l] + nums[r]
                if currentSum == 0:
                    threeSum.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

                elif currentSum > 0:
                    r -= 1
                else:
                    l += 1
            i += 1

        return threeSum


s = Solution()
print(s.threeSum([-1, 0, 1, 2, -1, -4]))
print(s.threeSum([-3, 3, 4, -3, 1, 2]))
# -3 -3 1 2 3 4
