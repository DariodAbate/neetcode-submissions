class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_prod = 1
        output = []
        
        i = 0
        while i < len(nums):
            output.append(left_prod)
            left_prod *= nums[i]

            i += 1

        right_prod = 1
        i = len(nums) - 1
        while i >= 0:
            output[i] *= right_prod 
            right_prod *= nums[i]

            i -= 1
        
        return output

        