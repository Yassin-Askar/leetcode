class Solution:
    def trap(high: list[int]) -> int:  # type: ignore
        trapped = 0
        left = 0
        right = len(high)-1
        left_max = 0
        right_max = 0

        while left < right:

            if high[left] < high[right]:
                if high[left] > left_max:
                    left_max = high[left]
                else:
                    trapped += (left_max - high[left])
                left += 1
            else:
                if high[right] > right_max:
                    right_max = high[right]
                else:
                    trapped += (right_max - high[right])
                right -= 1

        return trapped


high = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

print(Solution.trap(high=high))  # type: ignore  # type: ignore)
