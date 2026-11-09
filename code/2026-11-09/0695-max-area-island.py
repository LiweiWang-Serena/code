# LeetCode 695. Max Area of Island (Medium)
# Mock OA 2026-11-09: all tests passed
# Time: 56:59

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        visited = set()
        def dfs(i, j):
            if i < 0 or i > row - 1 or j < 0 or j > col - 1:
                return 0
            if grid[i][j] == 0 or (i, j) in visited:
                return 0
            visited.add((i, j))

            area = 1
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for dr, dc in directions:
                nr = dr + i
                nc = dc + j
                area += dfs(nr, nc)
            return area
        
        
        maxArea = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1 and grid[i][j] not in visited:
                    maxArea = max(maxArea, dfs(i, j))
        return maxArea
