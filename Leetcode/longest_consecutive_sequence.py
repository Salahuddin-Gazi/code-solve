# 128 Longest Consecutive Sequence
from typing import List


class Solution:
    '''
    This is to find the longest consecutive sequence of an array. basically 1234 length
    '''

    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in numSet:
            length = 0
            if num-1 not in numSet:
                while num+length in numSet:
                    length += 1

            if length > longest:
                longest = length

        return longest


s = Solution()
print(s.longestConsecutive([100, 4, 200, 1, 3, 2]))
