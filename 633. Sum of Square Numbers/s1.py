

from math import sqrt


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left = 0
        right = int(sqrt(c))
        while left <= right:
            guess = left**2 + right**2
            if guess == c:
                return True
            if guess < c:
                left += 1
            else:
                right -= 1
        return False


print(Solution().judgeSquareSum(5))
