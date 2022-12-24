class Solution:
	def solveNQueens(self, n: int) -> list[list[str]]:

		def generate_board(row):
			if row == n:
				board = ["".join(r) for r in chess_board]
				res.append(board)
			for c in range(n):
				if c in col or (row + c ) in main_diagonal or (row -c) in counter_diagonal:
					continue
				chess_board[row][c]="Q"
				col.add(c)
				main_diagonal.add(row+c)
				counter_diagonal.add(row-c)
				generate_board(row+1)
				# clean sets
				chess_board[row][c]="."
				col.remove(c)
				main_diagonal.remove(row+c)
				counter_diagonal.remove(row-c)
		res = []
		chess_board = [["."]*n for i in range(n) ]
		col =set()
		main_diagonal = set()
		counter_diagonal = set()
		generate_board(0)
		return res














n = 4
print(Solution(). solveNQueens(n = n , ))