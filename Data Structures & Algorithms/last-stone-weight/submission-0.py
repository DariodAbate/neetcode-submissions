import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = stones
        heapq.heapify_max(heap)
        # pop da maxheap di na, l'altra facciamo solo peer
        while len(heap) > 1:
            x = heapq.heappop_max(heap) # remove x
            y = heap[0]

            if x == y:
                heapq.heappop_max(heap) # remove y
            else:
                heapq.heappop_max(heap)
                heapq.heappush_max(heap, abs(y - x))

        if len(heap) == 1:
            return heap[0]
        else:
            return 0
        