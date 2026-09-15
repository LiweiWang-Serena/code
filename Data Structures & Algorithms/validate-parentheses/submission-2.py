class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pair = {'(':')', '{':'}', '[':']'} 
        for ch in s:
            if ch in '({[':
                stack.append(ch)
            else:
                if not stack or stack[-1]  != pair[ch]:
                    return false
                stack.pop()
        return not stack

        