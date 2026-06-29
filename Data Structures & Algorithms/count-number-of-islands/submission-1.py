class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dirs=[(1,0),(-1,0),(0,1),(0,-1)]
        height,width=len(grid),len(grid[0])
        def rdel(x:int, y:int):
            for dx, dy in dirs:
                newX, newY = x+dx, y+dy
                if 0<=newX<width and 0<=newY<height and grid[newY][newX]=="1":
                    grid[newY][newX]="0"
                    rdel(newX,newY)

        icount=0
        for r in range(height):
            for c in range(width):
                if grid[r][c]=="1":
                    icount+=1
                    rdel(c,r)
        return icount 