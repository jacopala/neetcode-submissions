class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        charCount=[]
        res=[]
        for s in strs:
            count={}
            for l in s:
                if l in count:
                    count[l]+=1
                else:
                    count[l]=1
            if count in charCount:
                res[charCount.index(count)].append(s)
            else:
                charCount.append(count)
                res.append([s])

        return res