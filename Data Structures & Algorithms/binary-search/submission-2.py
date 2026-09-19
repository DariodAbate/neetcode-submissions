class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.search_idx(nums, target, 0, len(nums) - 1)
    
    def search_idx(self, nums: List[int], target: int, l:int, r:int) -> int:
        if l > r:
            return -1
        if r == l:
            return l if target == nums[l] else -1

        d = int((r - l) / 2)
        idx = l + d

        if nums[idx] == target:
            return idx
        elif nums[idx] > target:
            return self.search_idx(nums, target, l, l + d - 1)
        else:
            return self.search_idx(nums, target, l + d + 1, r) 






        