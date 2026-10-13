class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(perm, used):
            if len(perm) == len(nums):
                res.append(perm.copy())
                return

            # choose one element to put in the current position
            for i in range(len(used)):
                if not used[i]:
                    # mark as used and add to the path
                    used[i] = True
                    perm.append(nums[i])
                    dfs(perm, used)

                    # backtrack: unmark and remove to try the next available number
                    used[i] = False
                    perm.pop()


        dfs([], [False] * len(nums))
        return res


        