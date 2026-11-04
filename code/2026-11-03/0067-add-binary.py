# LeetCode 67. Add Binary (Easy)
# Mock OA 2026-11-03: all tests passed
# Time: 27:48

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        x = len(a) - 1
        y = len(b) - 1
        carry = 0
        res = []
        while x >= 0 or y >= 0 or carry:
            l = int(a[x]) if x >= 0 else 0
            m = int(b[y]) if y >= 0 else 0
            total = l + m + carry
            digit = total % 2
            carry = total // 2
            res.append(str(digit))
            x -= 1
            y -= 1
        return"".join(reversed(res))
