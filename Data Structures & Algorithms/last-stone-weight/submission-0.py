class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [w*-1 for w in stones]
        heapq.heapify(max_heap)
        while(len(max_heap)>1):
            w1 = -heapq.heappop(max_heap)
            w2 = -heapq.heappop(max_heap)
            if w1!=w2:
                heapq.heappush(max_heap, -(max(w1,w2)-min(w1,w2)))
        return 0 if len(max_heap)==0 else -heapq.heappop(max_heap)