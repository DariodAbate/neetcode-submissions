class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(0, len(nums) - 2):
            # avoid duplicates
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l = i + 1
            r = len(nums) - 1

            while l < r:
                if nums[l] + nums[r] + nums[i] == 0:
                    res.append( [nums[i], nums[l], nums[r]] )
                    l += 1 
                    # the sum will always be > 0 because of fixed i and increased l
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                    while nums[r + 1] == nums[r] and l < r:
                        r -= 1

                elif nums[l] + nums[r] + nums[i] < 0:
                    l += 1

                else:
                    r -= 1
            
        return res
        