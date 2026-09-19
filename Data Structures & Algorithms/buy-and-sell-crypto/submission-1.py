class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0

        best_profit = 0

        for i, price_buy in enumerate(prices[:-1]):
            for price_sell in prices[i+1:]:
                if price_sell - price_buy > best_profit:
                    best_profit = price_sell - price_buy

        return best_profit

