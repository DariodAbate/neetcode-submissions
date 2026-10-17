class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        memo = {}

        def dfs(i: int, par_sum: int):
            if (i, par_sum) in memo:
                return memo[i, par_sum]

            if i == len(nums):
                return 1 if par_sum == target else 0

            memo[i, par_sum] = (
                dfs(i + 1, par_sum + nums[i]) + 
                dfs(i + 1, par_sum - nums[i])
            )
            return memo[i, par_sum]
    
        return dfs(0, 0)

        