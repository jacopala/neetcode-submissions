class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProf=0
        minBuy=prices[0]
        for p in prices:
            profit=p-minBuy
            if profit>maxProf:
                maxProf=profit
            if p<minBuy:
                minBuy=p
        return maxProf