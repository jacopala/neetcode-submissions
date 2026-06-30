class Solution:
    def hammingWeight(self, n: int) -> int:
        res=0
        for i in range(32):
            res+=1 if n&(1<<i)!=0 else 0
        return res