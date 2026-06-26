class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 4:
            return n
        cache = [0,1,2]+[]*(n-2) # number of ways to climb i steps
        for i in range(3,n+1):
            cache.append(cache[i-1]+cache[i-2])
        return cache[-1]