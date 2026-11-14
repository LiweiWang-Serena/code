# LeetCode 2054. Two Best Non-Overlapping Events (Medium)
# Mock OA 2026-11-13: all tests passed
# Time: 23:42
#
# 1. Understand the problem: max value without overlap between events index
# 2. Data structures: events[0][1] < events[1][0]

class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        best = 0
        n = len(events)
        for i in range(n):
            s1, e1, v1 = events[i]
            best = max(best, v1)             # 只选这一个区间
            for j in range(i + 1, n):
                s2, e2, v2 = events[j]
                if e1 <s2 or e2 < s1:                       # 两个区间不重叠
                    best = max(best, v1 + v2)     # 两个一起选
        return best
