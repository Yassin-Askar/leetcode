class Solution:
    def hammingWeight(self, n: int) -> int:
        ones_sum = 0
        for b in str(bin(n)):
            if b == "1":
                ones_sum += 1
        return ones_sum
