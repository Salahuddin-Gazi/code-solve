from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        obj = {}
        isDuplicate = False
        for num in nums:
            # print('num', num)
            # print('isFound', obj.get(num) != None)
            if obj.get(num) is not None:
                isDuplicate = True
                break
            else:
                obj[num] = True

        return isDuplicate


s = Solution()
print(s.containsDuplicate([1, 2, 3, 1, 6, 7]))
