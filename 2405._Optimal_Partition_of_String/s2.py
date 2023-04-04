class Solution:
	def partitionString(self, s: str) -> int:
		res = 1
		cur_set = set()

		for c in s:
			if c in cur_set:
				res +=1
				cur_set = set()
			cur_set.add(c)
		return res







s = "ssssss"
print(Solution(). partitionString(s = s , ))

