class Solution:
	def firstMissingPositive(self, nums: list[int]) -> int:
		for i in range(len(nums)):
			correct_spot = nums[i] - 1
			while 1 <= nums[i] <= len(nums) and nums[i] != nums[correct_spot]:
				nums [i], nums[correct_spot] = nums[correct_spot], nums[i]
				correct_spot = nums[i] - 1

		for i in range(len(nums)):
			if i + 1 != nums[i]:
				return i + 1
		return len(nums) + 1



nums = [1,0,3]
print(Solution(). firstMissingPositive(nums = nums , ))