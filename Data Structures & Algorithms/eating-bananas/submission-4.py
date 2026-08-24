from typing import List
from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = max(piles)
        while l <= r:
            m = (l + r) // 2
            totalhour = 0
            for p in piles:

                totalhour += ceil(p / m)
            if totalhour <= h:
                res = m
                r = m - 1
            else:
                l = m + 1
        return res

        



        