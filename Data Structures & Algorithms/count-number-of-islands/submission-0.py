class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def rdel(r:int, c:int):
            if r<0 or len(grid)<=r:
                return
            if c<0 or len(grid[0])<=c:
                return
            if grid[r][c]=='0':
                return
            grid[r][c]='0'
            rdel(r-1,c)
            rdel(r+1,c)
            rdel(r,c-1)
            rdel(r,c+1)
        icount=0
        for r, row in enumerate(grid):
            for c in range(len(row)):
                if grid[r][c]=='1':
                    rdel(r,c)
                    icount+=1
        return icount 