class Solution:
	def removeDuplicates(self, s: str) -> str:
		res = []
		for i in range(len(s)):
			if res and  res[-1] == s[i]:
				res.pop()

			else:
				res.append(s[i])



		return "".join(res)











s = "abbaca"
print(Solution(). removeDuplicates(s = s , ))