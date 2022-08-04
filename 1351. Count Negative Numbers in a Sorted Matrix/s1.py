class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        res = 0
        for nums in grid:

            low = 0
            high = len(nums)-1
            while low <= high:

                mid = (low + high) // 2

                if nums[low] < 0:
                    res += (len(nums)-low)
                    break
                elif nums[high] > 0:
                    high = mid - 1
                else:
                    low = low + 1
        return res
