

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        sum_dict = {}
        for i in range(len(nums)):
            if target - nums[i] in sum_dict:

                return[sum_dict[target - nums[i]], i]

            sum_dict[nums[i]] = i


nums = [3, 2, 3]
target = 6
print(Solution(). twoSum(nums=nums, target=target, ))
