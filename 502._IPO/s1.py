from heapq import heappop, heappush


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: list[int], capital: list[int]) -> int:
        current_capital = w
        capitals_min_heap = []
        profits_max_heap = []

        for x in range(0, len(capital)):
            heappush(capitals_min_heap, (capital[x], x))

        for _ in range(k): 

            while capitals_min_heap and capitals_min_heap[0][0] <= current_capital:
                c, i = heappop(capitals_min_heap)
                heappush(profits_max_heap, (-profits[i], i))

            if not profits_max_heap:
                break

            j = -heappop(profits_max_heap)[0]
            current_capital = current_capital + j
        return current_capital
k = 2
w = 0
profits = [1, 2, 3]
capital = [0, 1, 1]
print(Solution(). findMaximizedCapital(
    k=k, w=w, profits=profits, capital=capital, ))
