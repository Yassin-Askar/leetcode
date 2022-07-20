class Solution:
    def search(self, nums: list[int], target: int) -> int:
        low = mid = 0
        hight = len(nums) - 1

        while low <= hight:
            mid = (low+hight)//2
            guess = nums[mid]
            if guess == target:
                return mid
            if guess > target:
                hight = mid - 1
            else:
                low = mid + 1

        return -1
