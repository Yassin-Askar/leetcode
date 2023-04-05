import math
class Solution:
	def minimizeArrayValue(self, nums: list[int]) -> int:
		res = 0
		prefix_sum = 0
		for i in range(len(nums)):
			prefix_sum +=nums[i]
			res = max (res,math.ceil(prefix_sum/(i+1)))
		return res










nums = [3,7,1,6]
print(Solution(). minimizeArrayValue(nums = nums , ))