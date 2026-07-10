class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sn = set(nums)
        longest=0
        def countDown(n: int) -> int:
            return 1+countDown(n-1) if n in sn else 0
        for n in nums:
            longest=max(longest,countDown(n))
        return longest