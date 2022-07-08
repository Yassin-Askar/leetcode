class Solution:
    def maxProfit(prices: list[int]) -> int:  # type: ignore

        buy = 0

        profit = 0
        for i in range(len(prices)):

            if prices[i] - prices[buy] > profit:
                profit = prices[i] - prices[buy]

            if prices[i] < prices[buy]:
                buy = i

        return profit


prices = [7, 6, 4, 3, 1]
print(Solution.maxProfit(prices=prices))  # type: ignore
