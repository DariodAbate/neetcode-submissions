class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        elems = []

        def dfs(i):
            dist = self.distance(elems, target)

                
            if dist == 0: # victory
                res.append(elems.copy())
                return
            elif dist < 0 or i >= len(nums): # check other paths
                return
            
            # either take the same number
            # or the next one
            elems.append(nums[i])
            dfs(i)
            elems.pop()
            dfs(i+1)

        dfs(0)
        return res
            


    
    def distance(self, nums: List[int], target: int) -> int:
        sum = 0
        for num in nums:
            sum += num
        return target - sum
        