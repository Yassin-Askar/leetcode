class Solution:
    def search(self, nums: list[int], target: int) -> int:
        low = mid = 0
        height = len(nums) - 1

        while low <= height:
            mid = (low+height)//2
            guess = nums[mid]
            if guess == target:
                return mid
            if guess > target:
                height = mid - 1
            else:
                low = mid + 1

        return -1
