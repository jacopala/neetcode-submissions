class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub=[nums[0]]
        res=nums[0]
        for n in nums[1:]:
            maxSub=[x+n for x in maxSub]+[n]
            res=max(res,max(maxSub))
        return res