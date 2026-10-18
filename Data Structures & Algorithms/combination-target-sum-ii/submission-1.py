class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []       
        nums = []

        candidates.sort()

        def dfs(i):
            dist = self.distance(nums, target) 
            if dist == 0:
                res.append(nums.copy())
                return
            elif i >= len(candidates) or dist < 0:
                return
            
            # can either choose to take the current or not to take it
            nums.append(candidates[i])
            dfs(i+1)

            # in the case of not taken, should skip the useless numbers
            discard = nums.pop()            
            while i + 1 < len(candidates) and candidates[i + 1] == discard:
                i += 1
            dfs(i+1)
        
        dfs(0)
        return res

    
    def distance(self, nums: List[int], target: int) -> int:
        sum = 0
        for num in nums:
            sum += num
        return target - sum
        