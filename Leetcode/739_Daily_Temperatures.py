from typing import List


class Solution:
    """This is to find the temparature day difference using Monotonic Decreasing Stack"""

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []  # store in pair [index, temp]
        res = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][1]:
                temp_index, temp = stack.pop()
                res[temp_index] = i - temp_index
            stack.append([i, t])
        return res


s = Solution()
print(s.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [1,1,4,2,1,1,0,0])  # output [1,1,4,2,1,1,0,0]
print(s.dailyTemperatures([30, 40, 50, 60]) == [1,1,1,0])  # output [1,1,1,0]
print(s.dailyTemperatures([30, 60, 90]))  # output [1,1,0]
