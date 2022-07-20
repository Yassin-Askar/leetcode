class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        hight = len(nums)-1
        low = 0

        while low <= hight:
            mid = (hight+low)//2
            num = nums[mid]
            if num == target:
                return mid
            if num > target:
                hight = mid - 1
            else:
                low = mid + 1
        return low
