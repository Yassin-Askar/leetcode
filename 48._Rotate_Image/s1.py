class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        matrix_length = len(matrix)
        for i in range(matrix_length):
            for j in range(i):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
        for i in range(matrix_length):
            for j in range(matrix_length // 2):
                temp = matrix[i][j]
                matrix[i][j] = matrix[i][matrix_length - j - 1]
                matrix[i][matrix_length - j - 1] = temp


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(Solution(). rotate(matrix=matrix, ))
