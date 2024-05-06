class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums_len = len(nums)
        total_prod = 1
        prod_arr = []
        # print(prod_arr)

        for num in nums:
            if num != 0:
                total_prod *= num

        for i in range(nums_len):
            if nums[i] != 0:
                prod_arr.insert(i,int(total_prod / nums[i]))

        return prod_arr

s = Solution()
print(s.productExceptSelf([1,2,3,4]))
# Output: [24,12,8,6]

print(s.productExceptSelf([-1,1,0,-3,3]))
# Output: [0,0,9,0,0]
