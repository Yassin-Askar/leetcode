class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        high = len(nums)-1
        low = 0

        while low <= high:
            mid = (high+low)//2
            num = nums[mid]
            if num == target:
                return mid
            if num > target:
                high = mid - 1
            else:
                low = mid + 1
        return low
