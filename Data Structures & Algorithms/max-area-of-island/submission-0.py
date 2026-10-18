class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = [[False for i in range(len(grid[0]))] for i in range (len(grid))]

        max_size = 0
        for r in range(0, len(grid)):
            for c in range(0, len(grid[0])):
                if grid[r][c] == 1 and not visited[r][c]:
                    size = self.explore(grid, visited, r, c)
                    max_size = max(max_size, size)
        return max_size

    def explore(self, grid: List[List[int]], visited: List[List[bool]], r: int, c: int) -> int:
        q = deque([[r, c]])
        visited[r][c] = True
        cells = 1
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while q:
            curr_r, curr_c = q.popleft()
            
            for dr, dc in directions:
                nr = curr_r + dr 
                nc = curr_c + dc 
                
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                    if grid[nr][nc] == 1 and not visited[nr][nc]:
                        visited[nr][nc] = True
                        cells += 1
                        q.append([nr, nc])

        return cells
            