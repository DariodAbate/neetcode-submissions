class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        IMPOSSIBLE = amount + 1

        memo = {}

        # min number of coins to reach total
        def dfs(total: int) -> int:
            if total == amount:
                return 0
            elif total > amount:
                return IMPOSSIBLE
            if total in memo:
                return memo[total]
            
            best = IMPOSSIBLE
            for coin in coins:
                best = min(
                    best,
                    1 + dfs(total + coin),
                )
            memo[total] = best
            return memo[total]

        ret = dfs(0)

        return ret if ret <= amount else -1