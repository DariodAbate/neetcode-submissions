class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        comb = []

        def dfs(i: int, rem: int) -> None:
            if rem == 0:
                res.append(comb.copy())
                return

            if rem < 0 or i >= len(nums):
                return

            # either take the same number
            # or the next one
            comb.append(nums[i])
            dfs(i, rem - nums[i])

            comb.pop()
            dfs(i + 1, rem)

        dfs(0, target)
        return res

        