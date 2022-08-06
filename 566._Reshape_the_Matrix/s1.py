class Solution:
    def matrixReshape(self, mat: list[list[int]], r: int, c: int) -> list[list[int]]:
        rows = len(mat)
        columns = len(mat[0])
        if (rows * columns) != (r*c):
            return mat
        row_num = 0
        column_num = 0
        res = [[0 for i in range(c)] for i in range(r)]

        for i in range(r):
            for j in range(c):
                res[i][j] = mat[row_num][column_num]

                if column_num+1 == len(mat[0]):
                    column_num = 0
                    row_num += 1

                else:
                    column_num += 1
        return res


mat = [[1, 2], [3, 4]]
r = 1
c = 4
print(Solution(). matrixReshape(mat=mat, r=r, c=c, ))
