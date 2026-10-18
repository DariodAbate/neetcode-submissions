class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        IMPOSSIBLE = amount + 1

        # dp[i] is the min coins to make amount i
        dp = [IMPOSSIBLE] * (amount + 1) # understand this

        dp[0] = 0 

        for a in range(1, amount + 1): #for every amount
            for c in coins: # for every coin
                if a - c >= 0:
                    # one extra coin to make amount from min coins of a - c
                    dp[a] = min(dp[a], 1 + dp[a - c])
        return dp[amount] if dp[amount] <= amount else -1