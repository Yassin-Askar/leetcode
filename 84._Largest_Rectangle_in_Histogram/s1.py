

class Solution:
    def largestRectangleArea(self, highs: list[int]) -> int:
        stack = []
        max_rect = 0
        for i, high in enumerate(highs):
            current_high = i
            while stack and stack[-1][1] > high:
                index, h = stack.pop()
                max_rect = max(max_rect, h * (i - index))
                current_high = index
            stack.append((current_high, high))

        for i, h in stack:
            max_rect = max(max_rect, h * (len(highs) - i))
        return max_rect


highs = [2, 1, 5, 6, 2, 3]
print(Solution(). largestRectangleArea(highs=highs, ))
