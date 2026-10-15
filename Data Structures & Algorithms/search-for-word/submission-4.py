class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        visited = [[False for _ in range(n)] for _ in range(m)]

        for r in range(m):
            for c in range(n):
                if self.explore(r, c, board, word, visited):
                    return True
        return False
    
    def explore(self, r: int, c: int, board: List[List[str]], word: str, visited: List[List[bool]]) -> bool:
        m = len(board)
        n = len(board[0])
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def dfs(r, c, i) -> bool:
            if board[r][c] != word[i]:
                return False
            if i == len(word) - 1:
                return True

            visited[r][c] = True
            found = False            
            for dir_r, dir_c in dirs:
                nr = r + dir_r
                nc = c + dir_c
                if (
                    0 <= nr < m and 0 <= nc < n 
                    and not visited[nr][nc]
                    and dfs(nr, nc, i + 1)
                ):
                    found = True
                    break

            visited[r][c] = False
            return found
        
        return dfs(r, c, 0)





        