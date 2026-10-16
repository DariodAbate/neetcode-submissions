class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        memo = {} 
        
        # returns the num of combinations for remaining amount using coins starting from coin_idx and afterward
        def dfs(remaining: int, coin_idx: int) -> int:
            if remaining == 0:
                return 1

            if coin_idx >= len(coins):
                return 0

            if (remaining, coin_idx) in memo:
                return memo[remaining, coin_idx]

            count = 0
            for i in range(coin_idx, len(coins)):
                if remaining - coins[i] >= 0:
                    count += dfs(remaining - coins[i], i)

            memo[remaining, coin_idx] = count

            return memo[remaining, coin_idx]

        return dfs(amount, 0)

