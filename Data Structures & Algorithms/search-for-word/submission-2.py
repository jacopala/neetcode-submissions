class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        dirs=[(1,0),(-1,0),(0,1),(0,-1)]
        height, width =len(board),len(board[0])
        def searchFor(i: int, found: set, x: int, y: int) -> bool:
            if i==len(word):
                return True
            if x<0 or height<=x or y<0 or width<=y:
                return False
            if (x,y) in found or board[x][y]!=word[i]:
                return False
            found.add((x,y))
            for dx,dy in dirs:
                if searchFor(i+1,found,x+dx,y+dy):
                    return True
            found.remove((x,y))
            return False
            

        for x in range(height):
            for y in range(width):
                if searchFor(0, set(), x, y):
                    return True
        return False