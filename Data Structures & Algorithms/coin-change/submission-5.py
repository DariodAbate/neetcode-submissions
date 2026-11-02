class Solution:
    # top down
    # def coinChange(self, coins: List[int], amount: int) -> int:
    #     # at each step i consider to take each coin

    #     # min coins needed for changing total
    #     def coins_needed(total: int) -> int:
    #         if total == 0:
    #             return 0
    #         if total < 0:
    #             return float('inf')
            
    #         min_coins = float('inf')
    #         for coin in coins:
    #             min_coins = min(min_coins, 1 + coins_needed(total - coin))
    #         return min_coins

    #     res = coins_needed(amount)
    #     return res if res < float('inf') else -1

    # top down + memo
    # def coinChange(self, coins: List[int], amount: int) -> int:
    #     # at each step i consider to take each coin
    #     memo = {}
    #     # min coins needed for changing total
    #     def coins_needed(total: int) -> int:
    #         if total == 0:
    #             return 0
    #         if total < 0:
    #             return float('inf')
    #         if total in memo:
    #             return memo[total]
            
    #         min_coins = float('inf')
    #         for coin in coins:
    #             min_coins = min(min_coins, 1 + coins_needed(total - coin))
    #         memo[total] = min_coins
    #         return memo[total]

    #     res = coins_needed(amount)
    #     return res if res < float('inf') else -1

    # bottom up
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[t] = min coins needed for changing total t
        # last coin used is one of coins, so dp[t] = 1 + min(dp[t - coin])
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        
        for i in range(amount + 1):
            for coin in coins:
                if i + coin <= amount:
                    dp[i + coin] = min(dp[i + coin], 1 + dp[i])
        res = dp[-1]
        if res < float('inf'):
            return res
        else:
            return -1

    
