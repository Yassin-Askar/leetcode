import math


class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        height = max(piles)
        mid = 0
        low = 1
        k = mid

        while low <= height:
            mid = (height + low)//2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile/mid)

            if hours <= h:
                k = mid
                height = mid - 1
            else:
                low = mid + 1

        return k


piles = [30, 11, 23, 4, 20]
h = 6
print(Solution().minEatingSpeed(piles=piles, h=h))
