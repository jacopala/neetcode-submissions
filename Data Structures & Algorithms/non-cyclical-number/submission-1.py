class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n!=1:
            digits = str(n)
            n = sum([pow(int(d),2) for d in digits])
            if n in seen:
                return False
            seen.add(n)
        return True