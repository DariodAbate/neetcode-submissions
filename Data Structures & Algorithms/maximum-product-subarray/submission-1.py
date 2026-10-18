class Solution:

    def maxProduct(self, nums: List[int]) -> int:
        best = nums[0]
        n = len(nums)

        # for i in range(n):
        #     curr = 1
        #     for j in range(i, n):
        #         curr *= nums[j]
        #         best = max(best, curr)

        # return best

        # min and max product of subarrays ending at i
        prod_min = prod_max = nums[0]
        # max product seen so far, wherever it ends
        best = nums[0]

        for i in range(1, n):
            p1 = nums[i] * prod_min
            p2 = nums[i] * prod_max
            prod_min = min(nums[i], p1, p2)
            prod_max = max(nums[i], p1, p2)
            best = max(best, prod_max)

        return best


        