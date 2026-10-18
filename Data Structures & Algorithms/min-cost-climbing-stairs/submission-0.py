class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        mem = {}
        for i, c in enumerate(cost):
            if i == 0 :
                mem[i] = c
            elif i == 1:
                mem[i] = min(c, c + cost[0])
            else:
                mem[i] = c + min(mem[i-1],  mem[i-2])

        return min(mem[len(cost) - 1], mem[len(cost) - 2]) 
        