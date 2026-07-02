class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub=[]
        res=nums[0]
        for n in nums:
            maxSub=[x+n for x in maxSub]+[n]
            res=max(res,max(maxSub))
        return res