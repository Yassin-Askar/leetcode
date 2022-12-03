class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        my_dict = {}
        for i, n in enumerate(nums):
            my_dict[n] = 0
        for i in range(len(nums)+1):
            if i not in my_dict:
                return i


nums = [3, 0, 1]
print(Solution(). missingNumber(nums=nums, ))
