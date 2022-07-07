# ! two point solution (lift , right)


class Solution:
    def maxArea(height: list[int]) -> int:
        l, area, max_area = 0, 0, 0
        min_height = 0
        r = len(height) - 1
        while r > l:

            min_height = min(height[l], height[r])
            area = min_height * (r-l)

            if area > max_area:
                max_area = area
            if height[r] > height[l]:
                l += 1
            else:
                r -= 1
        return max_area


height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(Solution.maxArea(height))
