class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort()
        res.append(intervals[0])
        for interval in intervals[1:]:
            curr = res[-1]
            if curr[1] >= interval[0]:
                curr[1] = max(curr[1], interval[1])
            else:
                res.append(interval)
        return res

#data structure list, used as stack. algorithm sort interval merge. time complexity: o(nlog(n)) dominated by sort, space complexity o(n) result in list






        