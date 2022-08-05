class Solution:
    def hammingWeight(self, n: int) -> int:
        if n == 0:
            return 0
        return 1 + (self.hammingWeight(n & (n-1)))


n = 0x0110001
print(Solution().hammingWeight(n))
