class Solution:
    def lastStoneWeight(stones: list[int]) -> int:
        while len(stones) > 1:
            stones.sort()
            if stones[-1] == stones[-2]:
                stones.pop()
                stones.pop()
            else:
                stones[-1] -= stones[-2]
                stones.pop()
        return stones[0] if stones else 0


print(Solution.lastStoneWeight(stones=[2, 2]))
