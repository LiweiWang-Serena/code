

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self_list = []

        def backtrack(openN: int, closedN: int):
            if openN == n and closedN == n:
                res.append(''.join(self_list))
                return
            if openN < n:
                self_list.append('(')
                backtrack(openN + 1, closedN)
                self_list.pop()
            if closedN < openN:
                self_list.append(')')
                backtrack(openN, closedN + 1)
                self_list.pop()

        backtrack(0, 0)
        return res
