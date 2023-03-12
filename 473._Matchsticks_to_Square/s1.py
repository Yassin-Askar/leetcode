class Solution:
    def makesquare(self, matchsticks: list[int]) -> bool:
        length = sum(matchsticks) // 4
        if sum(matchsticks) / 4 != length:
            return False
        sides = [0]*4
        matchsticks.sort(reverse=True)

        def backtrack(i):
            if i == len(matchsticks):
                return True
            for j in range(4):
                if sides[j] + matchsticks[i] <= length:
                    sides[j] += matchsticks[i]
                    if backtrack(i+1):
                        return True
                    sides[j] -= matchsticks[i]
            return False
        return backtrack(0)


matchsticks = [1, 1, 2, 2, 2]
print(Solution(). makesquare(matchsticks=matchsticks, ))
