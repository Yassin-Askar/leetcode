class Solution:
	def singleNonDuplicate(self, nums: list[int]) -> int:
		left, right = 0, len(nums)-1
		while left < right:
			mid = (left+right) //2
			if mid % 2 == 1:
				mid -=1
			if nums[mid] == nums[mid +1]:
				left = mid +2
			else:
				right = mid
		return nums[left]










nums = [1,1,2,3,3,4,4,8,8]
print(Solution(). singleNonDuplicate(nums = nums , ))