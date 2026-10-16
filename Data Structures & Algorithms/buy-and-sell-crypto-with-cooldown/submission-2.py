class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 1:
            return 0

        hold = [0 for _ in range(n)] # maximum profit till day i having the coin
        free = [0 for _ in range(n)] # maximum profit till day i without the coin 

        hold[0] = -prices[0]
        free[0] = 0

        hold[1] = max(hold[0], -prices[1])
        free[1] = max(free[0], prices[1] + hold[0])

        for i in range(2, n):
            # each day I can either buy, sell or do nothing

            hold[i] = max(
                # do nothing
                hold[i - 1],
                # buy
                -prices[i] + free[i - 2]
            )
            
            free[i] = max(
                # do nothing
                free[i - 1],
                # sell
                prices[i] + hold[i - 1]
            )

        return  free[n - 1]


        