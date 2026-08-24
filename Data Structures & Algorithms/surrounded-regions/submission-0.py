class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])
        directions = ([1, 0], [-1, 0], [0, -1], [0, 1])
        q = deque()

        def capture():
            for r in range(rows):
                for c in range(cols):
                    if (r == 0 or r == rows - 1 or c == 0 or c == cols - 1 ) and board[r][c] == 'O':
                        q.append((r, c))

            while q:
                r, c = q.popleft()
                if board[r][c] == 'O':
                    board[r][c] = 'temp'
                    for dr, dc in directions:
                        nr, nc = dr + r, dc + c
                        if (0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == 'O'):
                            q.append((nr, nc))

        capture()
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'temp':
                    board[r][c] = 'O'
                        









        