class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        res = 0
        for nums in grid:

            low = 0
            height = len(nums)-1
            while low <= height:

                mid = (low + height) // 2

                if nums[low] < 0:
                    res += (len(nums)-low)
                    break
                elif nums[height] > 0:
                    height = mid - 1
                else:
                    low = low + 1
        return res
