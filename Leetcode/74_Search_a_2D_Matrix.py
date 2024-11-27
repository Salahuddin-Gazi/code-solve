import math
from typing import List


class Solution:
    """This is to find target from the ascending 2D matrix, using Binary search o(lon(m * n))"""

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1

        while l <= r:
            m = math.floor((r + l) / 2)
            if matrix[m][0] <= target <= matrix[m][-1]:
                target_list = matrix[m]
                il, ir = 0, len(target_list) - 1
                while il <= ir:
                    im = math.floor((il + ir) / 2)
                    if target == target_list[im]:
                        return True
                    if target_list[im] > target:
                        ir = im - 1
                    else:
                        il = im + 1

                return False

            elif matrix[m][0] > target:
                r = m - 1
            else:
                l = m + 1

        return False


s = Solution()
print(
    s.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3)
)  # output True
print(
    s.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13)
)  # output False
