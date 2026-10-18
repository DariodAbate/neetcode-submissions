class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        mem1 = 0
        mem2 = 0
        for i, c in enumerate(cost):
            if i == 0 :
                mem1 = c
            elif i == 1:
                mem2 = c
            else:
                tmp = mem1
                mem1 = mem2
                mem2 = c + min(tmp,  mem1)

        return min(mem1, mem2) 
        