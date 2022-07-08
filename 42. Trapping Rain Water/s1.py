"""! Status: Time Limit Exceeded
    """


class Solution:
    """42. Trapping Rain Water"""

    def trap(height: list[int]) -> int:  # type: ignore
        """trap func

        Args:
            height (list[int]): list of height

        Returns:
            int: max trapped rain
        """
        trapped = 0

        for i, h in enumerate(height):
            if height[:i] == []:
                max_left = 0
            else:
                max_left = max(height[:i])
            if height[i+1:] == []:
                max_right = 0
            else:
                max_right = max(height[i+1:])

            rain = min(max_left, max_right)-h
            if rain > 0:
                trapped += rain

        return trapped


height = [0, 0, 0, 0, 0, 0]
print(Solution.trap(height=height))  # type: ignore  # type: ignore)
