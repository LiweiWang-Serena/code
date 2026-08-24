class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitToChar  = {'2': 'abc', '3': 'def', '4':'ghi', '5': 'jkl', '6':'mno', '7':'pqrs', '8': 'tuv', '9' : 'wxyz'}
        if not digits:
            return []
        def backtrack(i, letter):
            if i == len(digits):
                res.append("".join(letter))
                return

            for char in digitToChar[digits[i]]:
                letter.append(char)
                backtrack(i + 1, letter)
                letter.pop()
        backtrack(0, [])
        return res




       

