class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])

        # mem[i] is the max loot I can collect after considering to rob
        # houses till the i-th

        mem = [0] * len(nums)
        mem[0] = nums[0]
        mem[1] = max(nums[1], nums[0])
        for i in range(2, len(nums)):
            # either choose to rob this house and take the loot of 2 houses before
            # or do not rob this house and collec the loot of the previous house
            mem[i] = max(mem[i-1], mem[i-2] + nums[i])

        return max(mem[-1], mem[-2])

        