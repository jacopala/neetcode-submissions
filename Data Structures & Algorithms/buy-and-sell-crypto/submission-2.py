class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProf=0
        minBuy=prices[0]
        for p in prices:
            profit=p-minBuy
            maxProf=max(maxProf,profit)
            minBuy=min(minBuy,p)
        return maxProf