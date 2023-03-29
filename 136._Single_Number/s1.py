class Solution:
	def singleNumber(self, nums: list[int]) -> int:
		res = 0
		for n in nums:
			res ^=n
		return res










nums = [2,2,1]
print(Solution(). singleNumber(nums = nums , ))