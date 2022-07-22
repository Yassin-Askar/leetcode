

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        prod = 1
        sum_nums = 0
        for num in str(n):

            prod *= int(num)
            sum_nums += int(num)
        return prod - sum_nums


num = 184
print(Solution().subtractProductAndSum(num))
