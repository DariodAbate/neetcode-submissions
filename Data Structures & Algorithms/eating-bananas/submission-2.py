import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        mb = piles[-1]

        l = 1
        r = mb

        min_k = mb
        while l <= r:
            mid = l + (r - l) // 2
            t = self.tot_time(piles, mid)

            if t <= h:
                min_k = min (min_k, mid)
                r = mid - 1
            else: 
                l = mid + 1

        return min_k

    
    def tot_time(self, piles: List[int], k: int) -> int:
        time = 0
        for pile in piles:
            time += math.ceil(pile/k)
        return time 


        
        