class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        res = 0
        area = 0

        def dfs(r, c):
            if(r < 0 or r > rows - 1 or c < 0 or c > cols - 1 or grid[r][c] == 0):
                return 0

            grid[r][c] = 0
            return(1 + dfs(r - 1, c) + dfs(r + 1, c) + dfs(r, c - 1) + dfs(r, c+ 1))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    area = dfs(r, c)
                    res = max(res, area)
        return res
        