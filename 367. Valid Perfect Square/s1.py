from pickle import HIGHEST_PROTOCOL


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        low, hight = 0, num

        while low <= hight:
            mid = (low+hight)//2
            if (mid*mid) == num:
                return True
            if (mid * mid) < num:
                low = mid + 1
            else:
                hight = mid - 1
        return False


print(Solution().isPerfectSquare(16))
