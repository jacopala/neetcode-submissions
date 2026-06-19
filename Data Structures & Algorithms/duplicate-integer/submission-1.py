class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ndict = {}
        for n in nums:
            if n in ndict:
                return True
            else:
                ndict[n] = True
        return False