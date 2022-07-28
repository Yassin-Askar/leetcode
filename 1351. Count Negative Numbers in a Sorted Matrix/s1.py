class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        res = 0
        for nums in grid:

            low = 0
            hight = len(nums)-1
            while low <= hight:

                mid = (low + hight) // 2

                if nums[low] < 0:
                    res += (len(nums)-low)
                    break
                elif nums[hight] > 0:
                    hight = mid - 1
                else:
                    low = low + 1
        return res
