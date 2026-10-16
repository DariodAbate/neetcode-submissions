class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m = len(board)
        n = len(board[0])

        # mark the elements that should not be captured
        for r in [0, m - 1]:
            for c in range(n):
                if board[r][c] == "O":
                    self.exclude_bfs(board, r, c)
        
        for  c in [0, n - 1]:
            for r in range(m):
                if board[r][c] == "O":
                    self.exclude_bfs(board, r, c)

        for r in range(m):
            for c in range(n):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "#":
                    board[r][c] = "O"

    def exclude_bfs(self, board: List[[str]], start_r: int, start_c: int):
        queue =  deque()
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        m = len(board)
        n = len(board[0])

        queue.append([start_r, start_c])

        while queue:
            r, c = queue.popleft()
            board[r][c] = "#"

            for dir_r, dir_c in dirs:
                nr = r + dir_r
                nc = c + dir_c
                if 0 <= nr < m and 0 <= nc < n and board[nr][nc]== "O":
                    queue.append([nr, nc])






        

    
        
        