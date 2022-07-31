class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        res = 0
        for nums in grid:
            print("=============")

            low = 0
            height = len(nums)-1
            if nums[-1] >= 0:
                continue
            while low <= height:
                mid = (low + height) // 2
                print(f"low = {low} height = {height} mid ={mid}")
                if low == height:

                    res += (len(nums)-mid)
                    break
                if nums[mid] < 0:
                    height = mid
                else:
                    low = mid + 1

        return res


grid = [[3, 2], [1, 0]]
print(Solution().countNegatives(grid=grid))
"""[[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
[[3,2],[1,0]]
        """
