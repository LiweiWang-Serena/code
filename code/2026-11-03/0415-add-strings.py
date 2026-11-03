# LeetCode 415. Add Strings (Easy)
# Mock OA 2026-11-03: all tests passed
# Time: 7:33
#
# 2. Data structures: str
# 3. Algorithm: linkedlist
# 4. Time and space complexity: O(N)

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        x = len(num1) - 1
        y = len(num2) - 1
        carry = 0
        res = []
        while x >= 0 or y >= 0 or carry:
            l = int(num1[x]) if x >= 0 else 0
            m = int(num2[y]) if y >= 0 else 0
            total = l + m + carry
            digit = total % 10
            carry = total // 10
            res.append(str(digit))
            x -= 1
            y -= 1
        return ''.join(reversed(res))
