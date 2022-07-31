from pickle import HIGHEST_PROTOCOL


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        low, height = 0, num

        while low <= height:
            mid = (low+height)//2
            if (mid*mid) == num:
                return True
            if (mid * mid) < num:
                low = mid + 1
            else:
                height = mid - 1
        return False


print(Solution().isPerfectSquare(16))
