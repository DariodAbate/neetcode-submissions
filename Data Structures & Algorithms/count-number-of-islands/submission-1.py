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

        while q:
            r_v, c_v = q.popleft()
            down = r_v + 1
            up = r_v - 1
            left =  c_v - 1
            right = c_v + 1

            if up >= 0 and not visited[up][c_v] and grid[up][c_v] == "1":
                visited[up][c_v] = True
                q.append([up, c_v])
            if down < len(grid) and not visited[down][c_v] and grid[down][c_v] == "1":
                visited[down][c_v] = True
                q.append([down, c_v])
            if left >= 0 and not visited[r_v][left] and grid[r_v][left] == "1":
                visited[r_v][left] = True
                q.append([r_v, left])
            if right < len(grid[0]) and not visited[r_v][right] and grid[r_v][right] == "1":
                visited[r_v][right] = True
                q.append([r_v, right])
            


        