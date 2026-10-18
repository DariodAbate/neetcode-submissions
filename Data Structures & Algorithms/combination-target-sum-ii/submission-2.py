class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []       
        nums = []

        candidates.sort()

        def dfs(i, rem):
            if rem == 0:
                res.append(nums.copy())
                return
            elif i >= len(candidates) or rem < 0:
                return
            
            # can either choose to take the current or not to take it
            nums.append(candidates[i])
            dfs(i+1, rem - nums[-1])

            # in the case of not taken, should skip the useless numbers
            discard = nums.pop()            
            while i + 1 < len(candidates) and candidates[i + 1] == discard:
                i += 1
            dfs(i+1, rem)
        
        dfs(0, target)
        return res