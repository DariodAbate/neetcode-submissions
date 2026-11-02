class Solution:
    # top down
    # def rob(self, nums: List[int]) -> int:
    #     # at each step I can decide to either rob or not the house
    #     # in the case I rob It I need to skip one

    #     def dfs(i: int, curr_loot: int) -> int:
    #         if i >= len(nums):
    #             return curr_loot
    #         return max(
    #             dfs(i + 1, curr_loot),
    #             dfs(i + 2, nums[i] + curr_loot)
    #         )
    #     return dfs(0, 0)

    # top down + memo
    # def rob(self, nums: List[int]) -> int:
    #     # at each step I can decide to either rob or not the house
    #     # in the case I rob It I need to skip one
    #     memo = {}

    #     def dfs(i: int, curr_loot: int) -> int:
    #         if i >= len(nums):
    #             return curr_loot
    #         key = (i, curr_loot)

    #         if key in memo:
    #             return memo[key]

    #         memo[key] = max(
    #             dfs(i + 1, curr_loot),
    #             dfs(i + 2, nums[i] + curr_loot)
    #         )
    #         return memo[key]

    #     return dfs(0, 0)
    
    # bottom up
    def rob(self, nums: List[int]) -> int:
        # at each step i consider either to rob or not the current house, retaining the max loot
        # obtained till that house.
        # if I rob this house I need ti consider the loop of two times ago 
        # if I do not this, I can consider the loot of the previous one
        n = len(nums)
        if n == 1:
            return nums[0]
        dp = [0] * n

        dp[0] = max(nums[0], 0)
        dp[1] = max(nums[1], dp[0])
        for i in range(2, n):
            dp[i] = max(
                # rob
                nums[i] + dp[i - 2],
                # skip 
                dp[i -1]
            )
        return dp[-1]
