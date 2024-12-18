from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_set = set()

        for i in nums:
            if i in num_set:
                return True
            
            num_set.add(i)

        return False