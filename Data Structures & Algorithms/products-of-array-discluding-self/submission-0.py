class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p=1
        oneZero=False
        for n in nums:
            if n!=0:
                p*=n
            else:
                if oneZero:
                    return [0]*len(nums)
                else:
                    oneZero=True
        return list(map(lambda x: int(p/x) if not oneZero else (0 if x!=0 else p), nums))