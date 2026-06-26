class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(remain: int, comb: List[int], start: int):
            if remain == 0:
                res.append(list(comb))
                return
            elif remain < 0:
                return
            for i, n in enumerate(nums[start:]):
                comb.append(n)
                backtrack(remain-n, comb, i+start)
                comb.pop()
        backtrack(target, [], 0)
        return res