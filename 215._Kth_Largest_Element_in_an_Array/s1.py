from heapq import heappop,heappush

class Solution:
	def findKthLargest(self, nums: list[int], k: int) -> int:
		maxHeap = []
		for n in nums:
			heappush(maxHeap,n)
			if len(maxHeap) > k:
				heappop(maxHeap)
		return maxHeap[0]










nums = [3,2,3,1,2,4,5,5,6]
k = 4
print(Solution(). findKthLargest(nums = nums , k = k , ))