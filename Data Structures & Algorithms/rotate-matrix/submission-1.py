class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        # iterate through groups and perform translation:
        # (x,y) = (y, n-x) for cw rotation
        def rot(x,y) -> None:
            hold = matrix[y][x]
            for _ in range(3):
                matrix[y][x]=matrix[n-1-x][y]
                x,y = y,n-1-x
            matrix[y][x]=hold
            return

        # 5x5
        # 1 1 1 1 2
        # 4 1 1 2 2
        # 4 4 x 2 2
        # 4 4 3 3 2
        # 4 3 3 3 3

        # 6x6
        # 1 1 1 1 1 2
        # 4 1 1 1 2 2
        # 4 4 1 2 2 2
        # 4 4 4 3 2 2
        # 4 4 3 3 3 2
        # 4 3 3 3 3 3
        for row in range(int(n/2)):
            for col in range(row, n-row-1):
                rot(row,col)
        return