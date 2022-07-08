class Solution:
    def trap(height: list[int]) -> int:  # type: ignore
        trapped = 0
        left = 0
        right = len(height)-1
        left_max = 0
        right_max = 0

        while left < right:

            if height[left] < height[right]:
                if height[left] > left_max:
                    left_max = height[left]
                else:
                    trapped += (left_max - height[left])
                left += 1
            else:
                if height[right] > right_max:
                    right_max = height[right]
                else:
                    trapped += (right_max - height[right])
                right -= 1

        return trapped


height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

print(Solution.trap(height=height))  # type: ignore  # type: ignore)
