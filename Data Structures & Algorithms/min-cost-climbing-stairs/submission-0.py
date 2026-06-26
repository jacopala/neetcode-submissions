class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        twoCost=0
        oneCost=0
        for i in range(2, len(cost)+1):
            current=min(oneCost+cost[i-1], twoCost+cost[i-2])
            twoCost=oneCost
            oneCost=current
        return current