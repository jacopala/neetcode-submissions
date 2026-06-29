class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        r=0
        letters=set()
        maxlen=0
        while r<len(s):
            if s[r] in letters:
                letters.remove(s[l])
                l+=1
            else:
                letters.add(s[r])
                r+=1
                maxlen=max(maxlen,r-l)
        return maxlen