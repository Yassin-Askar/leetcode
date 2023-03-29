class Solution:
	def singleNumber(self, nums: list[int]) -> int:
		seen_once = 0
		seen_twice = 0
		for num in nums:
				seen_once = (seen_once ^ num) & ~seen_twice
				seen_twice = (seen_twice ^ num) & ~seen_once
		return seen_once
nums = [1, 1, 7, 4, 5, 5, 8, 8]
print(Solution(). singleNumber(nums = nums , ))