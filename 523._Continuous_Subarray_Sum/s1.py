class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        prefix_remainder = {0: -1}
        sum = 0
        right, left = 0, 1
        for i, v in enumerate(nums):
            sum += v
            r = sum % k
            if r not in prefix_remainder:
                prefix_remainder[r] = i
            elif i - prefix_remainder[r] > 1:
                return True
        return False


nums = [23, 2, 4, 6, 7]
k = 6
print(Solution(). checkSubarraySum(nums=nums, k=k, ))
