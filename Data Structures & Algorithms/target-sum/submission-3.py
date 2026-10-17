class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        memo = {}

        def dfs(i: int, par_sum: int):
            if (i, par_sum) in memo:
                return memo[i, par_sum]

            if i == len(nums) and par_sum == target:
                return 1

            if i == len(nums) and par_sum != target:
                return 0

            memo[i, par_sum] = dfs(i + 1, par_sum + nums[i]) + dfs(i + 1, par_sum - nums[i])
            
            return memo[i, par_sum]
    
        return dfs(0, 0)

        