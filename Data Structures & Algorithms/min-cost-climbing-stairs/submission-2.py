class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        mem1 = cost[0]
        mem2 = cost[1]
        for i in range(2, len(cost)):
            mem1, mem2 = mem2, cost[i] + min(mem1,  mem2)
            
        return min(mem1, mem2) 
        