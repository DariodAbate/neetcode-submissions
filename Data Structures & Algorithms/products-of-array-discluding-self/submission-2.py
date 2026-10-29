class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        n = len(nums)
        left_prod = 1
        for num in nums:
            res.append(left_prod)
            left_prod *= num
            
        right_prod = 1
        for i in range(n-1, -1, -1):
            res[i] *= right_prod
            right_prod *= nums[i]

        return res


        