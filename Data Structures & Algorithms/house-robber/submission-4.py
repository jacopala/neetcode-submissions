class Solution:
    def rob(self, nums: List[int]) -> int:
        # either step +2 or +3 (anything larger would be combination)
        if len(nums)<3:
            return max(nums)
        if len(nums)==3:
            return max(nums[0]+nums[2],nums[1])
        mm = nums[:2] # start at either 0 or 1
        mm.append(nums[0]+nums[2])
        for i in range(3,len(nums)):
            mm.append(max(mm[i-2],mm[i-3])+nums[i])
        return max(mm[-1],mm[-2])