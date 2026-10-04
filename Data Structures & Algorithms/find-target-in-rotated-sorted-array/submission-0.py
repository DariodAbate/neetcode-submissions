class Solution:
    def search(self, nums: List[int], target: int) -> int:
        id = self.findCut(nums)

        left = self.find(nums, target, 0, id - 1)
        right = self.find(nums, target, id, len(nums) - 1)

        if left >= 0:
            return left
        else:
            return right
    
    def find(self, nums: List[int], target: int, l: int, r:int) -> int:
        while l <= r:
            if l == r and nums[l] == target:
                return l
            
            mid = l + (r - l) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1

        return -1 

    def findCut(self, nums:List[int]) -> int:
        l = 0
        r = len(nums) - 1

        cut = l

        while l <= r:
            if nums[l] < nums[r]:
                if nums[l] < nums[cut]:
                    cut = l
                break

            mid = l + (r - l) // 2

            
            if nums[mid] < nums[cut]:
                cut = mid

            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1

        return cut
