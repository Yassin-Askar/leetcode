class Solution:
    def findMiddleIndex(self, nums: list[int]) -> int:
        left_sum = 0
        right_sum = sum(nums)

        for i in range(len(nums)):
            if left_sum == right_sum - nums[i]:
                return i
            left_sum += nums[i]
            right_sum -= nums[i]

        return -1


nums = [2, 3, -1, 8, 4]
print(Solution(). findMiddleIndex(nums=nums, ))
