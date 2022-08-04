# ! two point solution (lift , right)


class Solution:
    def maxArea(high: list[int]) -> int:
        l, area, max_area = 0, 0, 0
        min_high = 0
        r = len(high) - 1
        while r > l:

            min_high = min(high[l], high[r])
            area = min_high * (r-l)

            if area > max_area:
                max_area = area
            if high[r] > high[l]:
                l += 1
            else:
                r -= 1
        return max_area


high = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(Solution.maxArea(high))
