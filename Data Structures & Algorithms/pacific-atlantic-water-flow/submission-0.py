class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])

        pacific_sources = []
        for c in range(n):
            pacific_sources.append([0, c])
        for r in range(m):
            pacific_sources.append([r, 0])
        pacific_visited = self.reachable_from(pacific_sources, heights)
        
        atlantic_sources = []
        for c in range(n):
            atlantic_sources.append([m - 1, c])
        for r in range(m):
            atlantic_sources.append([r, n - 1])
        atlantic_visited = self.reachable_from(atlantic_sources, heights)

        res = []
        for r in range(m):
            for c in range(n):
                if pacific_visited[r][c] and atlantic_visited[r][c]:
                    res.append([r, c])
        return res

    def reachable_from(self, reach: List[List[int]], heights: List[List[int]]) -> List[List[bool]]:
        m = len(heights)
        n = len(heights[0])

        queue = deque()

        visited = [[False for _ in range(n)] for _ in range(m)]
        for r, c in reach:
            visited[r][c] = True
            queue.append([r, c])
        
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while queue:
            r, c = queue.popleft()
            for r_dir, c_dir in dirs:
                nr = r + r_dir
                nc = c + c_dir

                if (
                    0 <= nr < m and 0 <= nc < n and
                    not visited[nr][nc] and
                    heights[r][c] <= heights[nr][nc]
                ):  
                    visited[nr][nc] = True
                    queue.append([nr, nc])

        return visited



        