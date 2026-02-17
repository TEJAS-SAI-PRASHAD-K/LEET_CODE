class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        diff = 0
        i = 1

        while i < len(prices):
            if prices[i] < buy:
                buy = prices[i]
            else:
                diff = max(diff, prices[i] - buy)

            i += 1

        return diff

