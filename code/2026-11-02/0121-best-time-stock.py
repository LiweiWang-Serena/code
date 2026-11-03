# LeetCode 121. Best Time to Buy and Sell Stock (Easy)
# Mock OA 2026-11-02: all tests passed
# Time: 15:34

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = float('inf')
        best = 0
        for p in prices:
            l = min(l, p)
            best = max(best, p - l)
        return best
