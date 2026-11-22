class Solution:
    def hammingWeight(self, n: int) -> int:
        iters = 0
        while n > 0:
            n = n & (n - 1)
            iters += 1

        return iters
    