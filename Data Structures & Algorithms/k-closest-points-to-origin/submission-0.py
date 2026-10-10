import math
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        heap = []
        for point in points:
            dist = math.sqrt(point[0] * point[0] + point[1] * point[1] )
            heap.append([dist, point])
        
        heapq.heapify_max(heap)

        while len(heap) > k:
            heapq.heappop_max(heap)
        
        res = []
        for dist, p in heap:
            res.append(p)
        return res
        
        