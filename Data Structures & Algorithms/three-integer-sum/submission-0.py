class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def twoSum(nums: List[int],goal:int)->List[List[int]]:
            seen=set()
            subres=[]
            for n in nums:
                m=goal-n
                if m in seen:
                    subres.append([m,n])
                seen.add(n)
            return subres

        res = []
        for i, n in enumerate(nums):
            for r in twoSum(nums[i+1:],-n):
                sr = sorted([n]+r)
                if sr not in res:
                    res.append(sr)
        return res