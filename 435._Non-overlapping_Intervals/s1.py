class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort()
        end_val = intervals[0][1]
        res = 0
        for s, e in intervals[1:]:
            if s >= end_val:
                end_val = e
            else:
                res += 1
                end_val = min(e, end_val)
        return res


intervals = [[1, 100], [11, 22], [1, 11], [2, 12]]
print(Solution(). eraseOverlapIntervals(intervals=intervals, ))
