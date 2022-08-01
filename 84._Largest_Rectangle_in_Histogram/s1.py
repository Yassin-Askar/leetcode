

class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack = []
        max_rect = 0
        for i, height in enumerate(heights):
            current_height = i
            while stack and stack[-1][1] > height:
                index, h = stack.pop()
                max_rect = max(max_rect, h * (i - index))
                current_height = index
            stack.append((current_height, height))

        for i, h in stack:
            max_rect = max(max_rect, h * (len(heights) - i))
        return max_rect


heights = [2, 1, 5, 6, 2, 3]
print(Solution(). largestRectangleArea(heights=heights, ))
