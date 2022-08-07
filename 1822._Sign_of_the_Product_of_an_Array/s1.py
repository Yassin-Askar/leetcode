class Solution:
    def arraySign(self, nums: list[int]) -> int:
        res = 1
        for num in nums:
            res *= num
        if res == 0:
            return 0
        elif res > 0:
            return 1
        return -1


nums = [-1, -2, -3, -4, 3, 2, 1]
print(Solution(). arraySign(nums=nums, ))
