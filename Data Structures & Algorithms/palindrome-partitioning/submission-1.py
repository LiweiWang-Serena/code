class Solution:
    def partition(self, s: str) -> List[List[str]]:
        '''
        res = []
        edge case: if s >= res ,return res
       
        '''
        res = []
        substr = []
        def backtracking(i):
            if i >= len(s):
                res.append(substr.copy())
                return

            for j in range(i, len(s)):
                segment = s[i:j + 1]
                if segment == segment[::-1]:
                    substr.append(segment)
                    backtracking(j + 1)
                    substr.pop()
        backtracking(0)
        return res



            
        






                
        