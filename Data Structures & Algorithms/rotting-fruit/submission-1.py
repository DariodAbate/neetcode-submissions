class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        EMPTY = 0
        FRESH = 1
        ROTTEN = 2

        # find all the initial rotten fruits
        mr = len(grid)
        mc = len(grid[0])
        rotten_fruits = deque()
        num_fresh_fruits = 0
        time = 0
        for r in range(mr):
            for c in range(mc):
                if grid[r][c] == ROTTEN:
                    rotten_fruits.append([r, c, time])
                elif grid[r][c] == FRESH:
                    num_fresh_fruits +=1

        # expand in parallel the rot
        dirs = [[0,1], [0, -1], [1, 0], [-1, 0]]
        while rotten_fruits:
            curr_r, curr_c, curr_time  = rotten_fruits.popleft()
            curr_time += 1


            for dir_r, dir_c in dirs:
                new_r = curr_r + dir_r
                new_c = curr_c + dir_c
                if (
                    0 <= new_r < mr and 0 <= new_c < mc
                    and grid[new_r][new_c] == FRESH
                ):
                    grid[new_r][new_c] = ROTTEN
                    rotten_fruits.append([new_r, new_c, curr_time])
                    time = curr_time
                    num_fresh_fruits -= 1
        return time if num_fresh_fruits <= 0 else -1


        