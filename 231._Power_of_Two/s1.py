class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1 or n == 2:
            return True
        if n < 2 or n % 2 != 0:
            return False
        return self.isPowerOfTwo(n//2)


n = 5
print(Solution(). isPowerOfTwo(n=n, ))
