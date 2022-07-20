class Solution:
    def search(self, nums: list[int], target: int) -> int:

        for n in range(len(nums)):
            if nums[n] == target:
                return n

        return -1
