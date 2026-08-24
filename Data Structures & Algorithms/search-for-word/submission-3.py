class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        '''
        output bool
        edge case: if the length of word equal word , return true.
        if r < 0 or > rows - 1 or if c < 0 or > cols - 1, return false
        timecom O(M*N*4L)
        cell not more than once use set
        
        '''
        row = len(board)
        col = len(board[0])
        path = set()

        def dfs(r, c, i):
            if i == len(word):
                return True
        
            if (r < 0 or r > row - 1 or c < 0 or c > col - 1 or word[i] != board[r][c] or (r, c) in path):
                return False

            path.add((r, c))
            res = (dfs(r - 1, c, i + 1) or dfs(r + 1, c, i + 1) or dfs(r, c - 1, i + 1) or dfs(r, c + 1, i + 1))
            path.remove((r, c))
            return res

        for r in range(row):
            for c in range(col):
                if dfs(r, c, 0):
                    return True
        return False



    


        
        



        



      

     




        