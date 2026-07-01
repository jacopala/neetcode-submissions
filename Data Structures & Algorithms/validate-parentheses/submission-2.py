class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        oC = ["[","{","("]
        cC = ["]","}",")"]
        for c in s:
            if c in oC:
                stack.append(oC.index(c))
            elif c in cC and len(stack)!=0 and cC.index(c) == stack[-1]:
                stack.pop()
            else:
                return False
        return True if stack==[] else False