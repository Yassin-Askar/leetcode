"""! Status: Time Limit Exceeded
    """


class Solution:
    """42. Trapping Rain Water"""

    def trap(high: list[int]) -> int:  # type: ignore
        """trap func

        Args:
            high (list[int]): list of high

        Returns:
            int: max trapped rain
        """
        trapped = 0

        for i, h in enumerate(high):
            if high[:i] == []:
                max_left = 0
            else:
                max_left = max(high[:i])
            if high[i+1:] == []:
                max_right = 0
            else:
                max_right = max(high[i+1:])

            rain = min(max_left, max_right)-h
            if rain > 0:
                trapped += rain

        return trapped


high = [0, 0, 0, 0, 0, 0]
print(Solution.trap(high=high))  # type: ignore  # type: ignore)
