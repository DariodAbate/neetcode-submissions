class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        return max(
            self.rob_straight(nums[1:]), 
            self.rob_straight(nums[:-1])
        )


    def rob_straight(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])

        prev2 = nums[0]
        prev1 = max(nums[1], nums[0])
        for i in range(2, len(nums)):
            prev2, prev1 = prev1 , max(prev1, prev2 + nums[i])

        return prev1
        