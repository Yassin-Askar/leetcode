class Solution:
	def reverseBits(self, n: int):
		res =0
		i=0
		for i in range(32):
			bit = (n >> i) &1
			res  =res | (bit<<(31-i))
		return res








n = 5
print(Solution(). reverseBits(n = n , ))