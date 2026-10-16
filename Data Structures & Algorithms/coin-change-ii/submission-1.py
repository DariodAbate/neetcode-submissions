class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        memo = {}
        
        def dfs(remaining: int, coin_idx: int) -> int:
            if remaining <= 0:
                return 1

            if coin_idx >= len(coins):
                return 0

            if (remaining, coin_idx) in memo:
                return memo[remaining, coin_idx]

            nc = 0
            for i in range(coin_idx, len(coins)):
                if remaining - coins[i] >= 0:
                    nc = nc + dfs(remaining - coins[i], i)

            memo[remaining, coin_idx] = nc
            
            return memo[remaining, coin_idx]

        return dfs(amount, 0)

