class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        phone  = {'2': 'abc', '3': 'def', '4':'ghi', '5': 'jkl', '6':'mno', '7':'pqrs', '8': 'tuv', '9' : 'wxyz'}
        if not digits:
            return []
        def backtrack(i, letter):
            if i == len(digits):
                res.append(letter)
                return

            for char in phone[digits[i]]:
                backtrack(i + 1, letter + char)

        backtrack(0, '')
        return res



        
        




       

