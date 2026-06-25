class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap=[]
        heapq.heapify(heap)
        for x,y in points:
            dist = -(x*x + y*y)
            heapq.heappush(heap, (dist,[x,y]))
            while len(heap)>k:
                heapq.heappop(heap)
        return [coord for _, coord in heap]