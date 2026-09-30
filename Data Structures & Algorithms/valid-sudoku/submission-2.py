class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = len(board)
        cols = len(board[0])
        grid = 3
        ng = 9

        # check rows
        for row in board:
           if not self.isValidSequence(row.copy()):
                return False

        # check cols
        for c in range(0, cols):
            col = []
            for r in range(0, rows):
                col.append(board[r][c])

            if not self.isValidSequence(col):
                return False

        # check grids
        for r_grid in range(0, ng, grid):
            for c_grid in range(0, ng, grid):
                #(r_grid, c_grid) is the top left elem of the grid to analize
                gr = []
                for r in range(r_grid, r_grid + grid):
                    for c in range(c_grid, c_grid + grid):
                        gr.append(board[r][c])

                if not self.isValidSequence(gr):
                    return False
        return True

        
        
    def isValidSequence(self, seq: List[str]) -> bool:
        hs = set([])

        for s in seq:
            if s != "." and s in hs:
                return False
            elif s not in hs:
                hs.add(s)
        return True