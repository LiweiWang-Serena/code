class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        maxP = 0
        while r < len(price):
            if price[l] < price[r]:
                profit = price[r] - price[l]
                maxP = max(maxP, profit)
            else:
                l = r
            r += 1
        return maxP
            
        
        