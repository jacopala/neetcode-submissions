class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k=k
        self.nums=nums
        self.pq=nums

    def add(self, val: int) -> int:
        self.pq.append(val)
        while len(self.pq)>self.k:
            self.pq.remove(min(self.pq))
        return min(self.pq)