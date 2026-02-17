class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        diff = 0

        for price in prices:
            buy = min(buy, price)          # track minimum
            diff = max(diff, price - buy)  # track best profit

        return diff
