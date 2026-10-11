class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        subsets = []

        # sort so that duplicated elements are contiguous
        nums.sort()

        def dfs(i):
            if i >= len(nums):
                res.append(subsets.copy())
                return 
            
            # can either choose to take or not to take
            subsets.append(nums[i])
            dfs(i+1)

            # skip the cloned elements
            discarded = subsets.pop()
            while i + 1 < len(nums) and discarded == nums[i + 1]:
                i += 1
            dfs(i+1) 

        dfs(0)
        return res
        