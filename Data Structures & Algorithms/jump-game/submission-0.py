class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_jump = nums[0]
        
        for j, jump in enumerate(nums):
            max_jump = max(jump, max_jump)
            if j < len(nums) - 1 and max_jump == 0:
                return False
            max_jump -= 1
        return True

        
        