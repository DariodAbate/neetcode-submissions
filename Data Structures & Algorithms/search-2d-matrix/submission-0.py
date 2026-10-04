class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        vec = []
        for row in matrix:
            vec.extend(row)
        return self.search_idx(vec, target, 0, len(vec) -1) >= 0

    
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
        