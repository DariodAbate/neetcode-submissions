import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        l = 1
        r = piles[-1]

        k = r
        while l < r:
            mid = l + (r - l) // 2
            if self.hoursAtRate(piles, mid) <= h:
                k = min(k, mid)
                r = mid
            else:
                l = mid + 1 
        return k

    
    def hoursAtRate(self, piles: List[int], k: int) -> int:
        h = 0
        for pile in piles:
            h += math.ceil(pile / k)
        return h
        