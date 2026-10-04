class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = self.search_row(matrix, target, 0, len(matrix) - 1)
        if row >= 0:
            return self.search_idx(matrix[row], target, 0, len(matrix[row]) - 1) >= 0
        else:
            return False


    def search_row(self, nums: List[List[int]], target: int, l:int, r: int) -> int:
        if l > r:
            return -1
        if r == l:
            return l if nums[l][0] <= target and nums[l][-1] >= target else -1
        
        d = int((r - l) / 2)
        idx = l + d

        if nums[idx][0] <= target and nums[idx][-1] >= target:
            return idx
        elif nums[idx][0] > target:
            return self.search_row(nums, target, l, idx - 1)
        else:
            return self.search_row(nums, target, idx + 1, r) 
 
    
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
            return self.search_idx(nums, target, l, idx - 1)
        else:
            return self.search_idx(nums, target, idx + 1, r) 
        