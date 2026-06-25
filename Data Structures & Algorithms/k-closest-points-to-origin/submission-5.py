import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = []
        for x,y in points:
            d=(x**2)+(y**2)
            dist.append((d,[x,y]))
        heapq.heapify(dist)
        res = []
        for i in range(k):
            res+=[heapq.heappop(dist)[1]]
        return res