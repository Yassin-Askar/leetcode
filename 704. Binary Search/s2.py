class Solution:
    def search(self, nums: list[int], target: int) -> int:
        low = mid = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low+high)//2
            guess = nums[mid]
            if guess == target:
                return mid
            if guess > target:
                high = mid - 1
            else:
                low = mid + 1

        return -1
