class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        mem = {}
        mem1 = 1
        mem2 = 2
        for i in range(3, n + 1):
            mem1, mem2 = mem2, mem1 + mem2 # at each step I can progress either by 1 or 2
        return mem2
        