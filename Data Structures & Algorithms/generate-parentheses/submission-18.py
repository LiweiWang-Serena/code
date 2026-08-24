

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res: List[str] = []
        st: List[str] = []

        def backtrack(openN: int, closedN: int) -> None:
            if openN == n and closedN == n:
                res.append("".join(st))
                return
            if openN < n:
                st.append('(')
                backtrack(openN + 1, closedN)
                st.pop()
            if closedN < openN:
                st.append(')')
                backtrack(openN, closedN + 1)
                st.pop()

        backtrack(0, 0)
        return res
