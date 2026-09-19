class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0;
        j = len(nums) - 1

        nums_c = nums.copy()
        nums_c.sort()

        a = 0
        while nums_c[i] + nums_c[j] != target:
            if nums_c[i] + nums_c[j] > target:
                j -= 1
            else:
                i += 1

        found_one = False
        idx_temp = 0
        for idx, num in enumerate(nums):
            if num == nums_c[i] or num == nums_c[j]:
                if found_one == True:
                    val = [idx, idx_temp]
                    val.sort()
                    return val
                else: 
                    found_one = True
                    idx_temp = idx


        


        return [i, j]