class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        treasures = []
        m = len(grid)
        n = len(grid[0])
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    treasures.append([r, c])
        
        queue = deque() # store(treasure_coord, dist)
        dist = 0
        for treasure in treasures:
            queue.append(treasure + [dist])

        # start bfs in parallel for each treasure
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        while queue:
            curr_r, curr_c, curr_d = queue.popleft()
            curr_d += 1
            for dir_r, dir_c in dirs:

                nr = curr_r + dir_r
                nc = curr_c + dir_c

                if 0 <= nr < m and 0 <= nc < n:
                    if grid[nr][nc] == 2147483647:
                        grid[nr][nc] = curr_d
                        queue.append([nr, nc, curr_d]) 

                    

        