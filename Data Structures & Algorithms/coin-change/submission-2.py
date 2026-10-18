class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        IMPOSSIBLE = amount + 1

        memo = {}

        # min number of coins to reach total using coins[i:]
        def dfs(i: int, total: int) -> int:
            if total == amount:
                return 0
            elif i >= len(coins) or total > amount:
                return IMPOSSIBLE

            if (i, total) in memo:
                return memo[i, total]
            
            # can either choose to take current coin or not
            memo[i, total] = min(
                1 + dfs(i, total + coins[i]),
                dfs(i + 1, total)
            )

            return memo[i, total]

        ret = dfs(0, 0)
        return ret if ret <= amount else -1