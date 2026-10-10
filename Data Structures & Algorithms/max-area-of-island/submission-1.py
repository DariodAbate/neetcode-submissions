class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_size = 0
        for r in range(0, len(grid)):
            for c in range(0, len(grid[0])):
                if grid[r][c] == 1:
                    size = self.explore(grid, r, c)
                    max_size = max(max_size, size)
        return max_size

    def explore(self, grid: List[List[int]], r: int, c: int) -> int:
        q = deque([[r, c]])
        grid[r][c] = 0
        cells = 1
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while q:
            curr_r, curr_c = q.popleft()
            
            for dr, dc in directions:
                nr = curr_r + dr 
                nc = curr_c + dc 
                
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                    if grid[nr][nc] == 1:
                        grid[nr][nc] = 0
                        cells += 1
                        q.append([nr, nc])

        return cells
            