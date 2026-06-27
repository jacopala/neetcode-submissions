class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # there will be n rows and n columns
        # solution is correct when each row and column has exactly one queen

        # there will be two 2n-1 diagonal lanes (top left and top right)
        # tlDiag indexed by col-row+(n-1)
        # trDiag indexed by col+row
        # each of the lanes can only have at most one queen, but not required for solution
        combs = []
        def dp(comb: List[List[str]], opC: List[bool], opTLD: List[bool], opTRD: List[bool]):
            r=len(comb)
            # base case: all rows filled out
            if r==n:
                combs.append(comb)
                return
            for c, col in enumerate(opC):
                # find open column in the next row
                # diagonals must also be open
                if col and opTLD[c-r+(n-1)] and opTRD[c+r]:
                    newRow = "."*c + "Q" + "."*(n-c-1)
                    newComb=comb + [newRow]

                    newOpC = opC.copy()
                    newOpC[c]=False

                    newOpTLD=opTLD.copy()
                    newOpTLD[c-r+(n-1)]=False
                    newOpTRD=opTRD.copy()
                    newOpTRD[c+r]=False

                    dp(newComb, newOpC, newOpTLD, newOpTRD)

            
        dp([],[True]*n,[True]*(2*n-1),[True]*(2*n-1))
        return combs