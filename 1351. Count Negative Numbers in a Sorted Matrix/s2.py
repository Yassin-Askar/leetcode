class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        res = 0
        for nums in grid:
            print("=============")

            low = 0
            hight = len(nums)-1
            if nums[-1] >= 0:
                continue
            while low <= hight:
                mid = (low + hight) // 2
                print(f"low = {low} hight = {hight} mid ={mid}")
                if low == hight:

                    res += (len(nums)-mid)
                    break
                if nums[mid] < 0:
                    hight = mid
                else:
                    low = mid + 1

        return res


grid = [[3, 2], [1, 0]]
print(Solution().countNegatives(grid=grid))
"""[[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
[[3,2],[1,0]]
        """
