class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        visited = [[False for i in range(len(grid[0]))] for i in range (len(grid))]

        num_islands = 0
        for r in range(0, len(grid)):
            for c in range(0, len(grid[0])):
                if grid[r][c] == "1" and not visited[r][c]:
                    num_islands += 1
                    self.explore(grid, visited, r, c)
        return num_islands

    def explore(self, grid: List[List[str]], visited: List[List[bool]], r: int, c: int) -> None:
        q = deque([[r, c]])
        visited[r][c] = True
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while q:
            curr_r, curr_c = q.popleft()
            
            for dr, dc in directions:
                nr = curr_r + dr 
                nc = curr_c + dc 
                
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                    if grid[nr][nc] == "1" and not visited[nr][nc]:
                        visited[nr][nc] = True
                        q.append([nr, nc])
            


        