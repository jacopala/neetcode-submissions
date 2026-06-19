class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        inverted = {}
        for i, n in enumerate(nums):
            if target-n in inverted:
                return list((inverted[target-n], i))
            else:
                inverted[n]=i
        return False