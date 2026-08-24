class Solution:
    def partition(self, s: str) -> List[List[str]]:
        '''
        res = []
        edge case: if s == res ,return res
        possible case is : 1st, split the string , thn output.
        2ed, if the substring is duplicated , then output
        '''

        res = []
        substr = []
        def dfs(i):
            if i >= len(s):
                res.append(substr.copy())
                return

            for j in range(i, len(s)):
                segment = s[i:j + 1]
                if segment == segment[::-1]:
                    substr.append(segment)
                    dfs(j + 1)
                    substr.pop()



        dfs(0)
        return res


            
        






                
        