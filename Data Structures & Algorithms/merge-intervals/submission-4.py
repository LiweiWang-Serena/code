class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort()
        res.append(intervals[0]) #save first interval for compare
        for interval in intervals[1:]: #compare from index 1
            curr = res[-1] 
            if curr[1] >= interval[0]:
                curr[1] = max(curr[1], interval[1]) # if overlap need merge
            else:
                res.append(interval) # no overlap dont need merge
        return res

        #time complexity cause of sort o(nlog(n))
        #space complexity o(n) cause of list
        #data structure list use as stack
        #algorithm sort interval merge

      










        