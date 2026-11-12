# LeetCode 70. Climbing Stairs (Easy)
# Mock OA 2026-11-12: all tests passed
# Time: 18:28

class Solution:
    def climbStairs(self, n: int) -> int:
        if 0 < n <= 2:
            return n
        a = 1
        b = 2
        for i in range(3, n + 1):
            new = a + b
            a = b
            b = new
        return b
