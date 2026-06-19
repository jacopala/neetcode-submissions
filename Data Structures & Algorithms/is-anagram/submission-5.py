class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charSet = {}
        for c in s:
            if c in charSet:
                charSet[c]+=1
            else:
                charSet[c]=1
        for c in t:
            if c in charSet:
                charSet[c]-=1
            else:
                return False
        for c in charSet:
            if charSet[c]!=0:
                return False
        return True