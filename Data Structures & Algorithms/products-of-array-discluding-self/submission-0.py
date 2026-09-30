class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod_all = 1
        zeros = []

        i = 0
        while i < len(nums):
            if nums[i] != 0:
                prod_all *= nums[i]
            else:
                zeros.append(i)

            i += 1
        
        output = []

        i = 0
        while i < len(nums):
            if len(zeros) == 1 and i == zeros[0]:
                output.append(prod_all)
            elif len(zeros) == 0:
                output.append(prod_all // nums[i])
            else:
                output.append(0)
            
            i += 1


        return output
        