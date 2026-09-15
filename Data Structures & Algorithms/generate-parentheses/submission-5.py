class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
       res = []
       st = []
       def backtrack(openN, closedN):
        if oepnN == n and closedN == n:
            res.append(''.join(stack))
            return
        if openN < n:
            res.append('(')
            backtrack.append(openN + 1, closedN)
            st.pop()
        if closedN < openN:
            res.append(')')
            backtrack.append(openN, closedN + 1)
            st.pop()
        backtrack(0, 0)
        return res

