class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        stack = [[0, []]] # store (idx, curr_path)
        while stack:
            i, path = stack.pop()

            if i >= len(nums): # finished to evaluate this branch
                res.append(path.copy())
            else:
                stack.append([i+1, path]) # not include i-th element
                stack.append([i+1, path + [nums[i]]]) # include

        return res