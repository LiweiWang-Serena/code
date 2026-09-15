class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        l = 0
        r = (ROWS * COLS) - 1
        while l <= r:
            mid = (l + r) // 2
            row = mid // col
            col = mid % col
            val = matrix[row][col]
            if target == val:
                return True
            elif target < val:
                r = mid - 1
            else:
                l = mid + 1
        return False