

class Solution:
    def specialArray(self, nums: list[int]) -> int:

        nums = sorted(nums, reverse=True)
        x = -1

        for i in range(len(nums) - 1):
            if nums[i] >= i+1 and nums[i + 1] < i+1:
                x = i + 1

        if nums[-1] >= len(nums):
            x = len(nums)

        return x


nums = [0, 4, 3, 0, 4]
print(Solution().specialArray(nums=nums))
