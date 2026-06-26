class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [0,1,2]+[None]*(n-2) # number of ways to climb i steps
        i=3
        while cache[n]==None:
            cache[i]=cache[i-1]+cache[i-2]
            i+=1
        return cache[n]