# LeetCode 66. Plus One (Easy)
# Mock OA 2026-11-03: all tests passed
# Time: 6:52

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = []
        carry = 1
        s = len(digits) - 1
        while s >= 0 or carry:
            l = digits[s] if s >= 0 else 0
            total = l + carry
            d = total % 10
            carry = total // 10
            res.append(d)
            s -= 1
        return res[::-1]
