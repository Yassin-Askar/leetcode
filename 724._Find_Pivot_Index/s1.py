class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        nums_sum = sum(nums)
        leftmost = 0
        for pivot, n in enumerate(nums):
            if leftmost == (nums_sum - leftmost - n):
                return pivot
            leftmost += n
        return -1


nums = [1, 7, 3, 6, 5, 6]
print(Solution(). pivotIndex(nums=nums, ))
