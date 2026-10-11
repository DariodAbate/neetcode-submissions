class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])

        prev2 = nums[0]
        prev1 = max(nums[1], nums[0])
        for i in range(2, len(nums)):
            # either choose to rob this house and take the loot of 2 houses before
            # or do not rob this house and collect the loot of the previous house
            prev2, prev1 = prev1 , max(prev1, prev2 + nums[i])

        return prev1

        