from typing import List


class Solution:
    '''This is to calculate car fleet count that reaches the target'''

    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        res = min_speed = 0
        z = sorted(zip(position, speed), reverse= True)
        
        for p, s in z:
            eta = (target - p) / s

            if eta > min_speed:
                res += 1
                min_speed = eta

        return res

s = Solution()
print(
    s.carFleet(target=12, position=[10, 8, 0, 5, 3], speed=[2, 4, 1, 1, 3])
)  # output 3
print(s.carFleet(target=10, position=[3], speed=[3]))  # output 1
print(s.carFleet(target=100, position=[0, 2, 4], speed=[4, 2, 1]))  # output 1
