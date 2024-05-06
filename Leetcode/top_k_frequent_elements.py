class Solution(object):
    '''
    This will return the top most k elements, if there is only k number of elements no need to check just return them all
    '''
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        if (len(nums) == k):
            return nums
        elif(k > len(nums)):
            return null

        num_hash = {}
        top_k_number = []

        for num in nums:
            if num_hash.get(num) == None:
                num_hash[num] = 1
            else:
                num_hash[num] += 1

        sorted_values = sorted([value for value in num_hash.values()], reverse=True)[:k]
        return [key for key, value in num_hash.items() if value in sorted_values]



solution = Solution()
print(solution.topKFrequent([1,1,1,2,2,3], 2))
print(solution.topKFrequent([1,2,2,3], 2))