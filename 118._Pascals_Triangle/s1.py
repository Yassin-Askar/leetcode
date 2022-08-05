class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        res = [[1]]
        for r in range(1, numRows):
            res.append([1] * (r+1))
            for c in range(1, r):
                res[r][c] = res[r-1][c] + res[r-1][c-1]
        return res
