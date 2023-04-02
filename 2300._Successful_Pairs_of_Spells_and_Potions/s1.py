class Solution:
	def successfulPairs(self, spells: list[int], potions: list[int], success: int) :
		potions.sort()
		res = []
		for n in spells:
			l = 0
			r = len(potions)-1
			start_point = float("inf")

			while l < r:
				mid = (l + r) //2
				if potions[mid] * n >= success:
					start_point = min(start_point,mid)
					r = mid -1
				elif potions[mid] * n < success:
					l = mid +1
			res.append( len(potions) - start_point ) if start_point != float("inf") else res.append(0)
		return res











spells = [3,1,2]
potions = [8,5,8]
success = 16
print(Solution(). successfulPairs(spells = spells , potions = potions , success = success , ))