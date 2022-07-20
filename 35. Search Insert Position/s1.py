# don't ask me how


class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        low = 0
        h = len(nums)-1
        hin = nums[h]
        mid = 0

        while h > low:

            mid = (h+low)//2

            if nums[mid] == target:
                return nums.index(target)
            if nums[mid] > target:
                h -= 1
                continue
            if nums[mid] < target:
                low += 1
                continue
        if target > hin:
            return low+1
        return low
