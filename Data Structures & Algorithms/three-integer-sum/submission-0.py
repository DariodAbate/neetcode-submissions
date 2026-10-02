class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        hs = set()
        for i in range(0, len(nums) - 2):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                if nums[l] + nums[r] + nums[i] == 0:
                    hs.add((nums[i], nums[l], nums[r]))
                    l += 1 # might also be decrease r
                elif nums[l] + nums[r] + nums[i] < 0:
                    l += 1
                else:
                    r -= 1
            
        return [list(triple) for triple in hs]
        