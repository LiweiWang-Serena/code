class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pair = {'(':')', '{':'}', '[':']'} 
        for ch in s:
            if c in '({[':
                stack.append(c)
            else:
                if not stack or stack[-1]  != pair[c]:
                    return false
                stack.pop()
        return not stack

        