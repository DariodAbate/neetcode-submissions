class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        m = nums[0]
        while l <= r:
            mid = (l + (r - l) // 2) 

            if nums[mid] > nums[r]: 
                m = min (m, nums[mid])
                l = mid + 1
            elif nums[mid] <= nums[r]: 
                m = min (m, nums[mid])
                r = mid - 1
            
        return m

            
        