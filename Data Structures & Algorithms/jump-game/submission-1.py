class Solution:
    def canJump(self, nums: List[int]) -> bool:
        steps_left = 0 # max steps still available from the current index
        n = len(nums)

        for i in range(n - 1): # reaching the last index is enough, no need to jump from it
            steps_left = max(nums[i], steps_left)
            if steps_left == 0:
                return False
            steps_left -= 1
        return True

        
        