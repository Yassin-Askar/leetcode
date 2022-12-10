class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        points = sorted(points, key=lambda x: x[1])
        end = -float("inf")
        res = 0
        for point in points:
            if point[0] > end:
                res += 1
                end = point[1]
        return res


points = [[10, 16], [2, 8], [1, 6], [7, 12]]
print(Solution(). findMinArrowShots(points=points, ))
