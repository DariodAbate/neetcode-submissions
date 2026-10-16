class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        memo = {}

        def maxFutureProf(day: int, canBuy: bool) -> int:
            if day >= len(prices):
                return 0 # in the future cannot obtain anything

            if (day, canBuy) in memo:
                return memo[day, canBuy]
            

            # each day I can either buy, sell or do nothing
            if canBuy:
                memo[day, canBuy] = max(
                    # do nothing
                    maxFutureProf(day + 1, canBuy),
                    # buy
                    - prices[day] + maxFutureProf(day + 1, False)
                )
            else:
                memo[day, canBuy] = max(
                    # do nothing
                    maxFutureProf(day + 1, canBuy),
                    # sell
                    prices[day] + maxFutureProf(day + 2, True)
                )
            return memo[day, canBuy]

        return maxFutureProf(0, True)


        