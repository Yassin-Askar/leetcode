class Solution:
	def partitionString(self, s: str) -> int:
		res = 0

		i = 0

		while  i < len(s):
			sub = ""
			while i < len(s) and s[i] not in sub :
				sub = sub + s[i]
				i +=1
			res +=1
		return res













s = "ssssss"
print(Solution(). partitionString(s = s , ))