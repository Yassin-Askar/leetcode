class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()
        res = [intervals[0]]
        for s, e in intervals[1:]:
            end = res[-1][1]
            if s <= end:
                res[-1][1] = max(e, end)
            else:
                res.append([s, e])
        return res


intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(Solution(). merge(intervals=intervals, ))
