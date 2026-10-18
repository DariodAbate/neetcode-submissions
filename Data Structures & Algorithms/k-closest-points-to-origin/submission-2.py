import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        heap = []
        for point in points:
            dist = point[0] * point[0] + point[1] * point[1]
            heapq.heappush_max(heap, [dist, point])

            if len(heap) > k:
                heapq.heappop_max(heap)
        
        res = []
        for dist, p in heap:
            res.append(p)
        return res
        
        