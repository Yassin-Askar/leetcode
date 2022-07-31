class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        height = len(nums)-1
        low = 0

        while low <= height:
            mid = (height+low)//2
            num = nums[mid]
            if num == target:
                return mid
            if num > target:
                height = mid - 1
            else:
                low = mid + 1
        return low
